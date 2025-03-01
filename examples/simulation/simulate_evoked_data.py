"""
.. _ex-sim-evoked:

==============================
Generate simulated evoked data
==============================

Use :func:`~mne.simulation.simulate_sparse_stc` to simulate evoked data.
"""
# Author: Daniel Strohmeier <daniel.strohmeier@tu-ilmenau.de>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
#
# License: BSD-3-Clause

# %%

import numpy as np
import matplotlib.pyplot as plt

import mne
from mne.datasets import sample
from mne.time_frequency import fit_iir_model_raw
from mne.viz import plot_sparse_source_estimates
from mne.simulation import simulate_sparse_stc, simulate_evoked

print(__doc__)

# %%
# Load real data as templates
data_path = sample.data_path()
meg_path = data_path / 'MEG' / 'sample'
raw = mne.io.read_raw_fif(meg_path / 'sample_audvis_raw.fif')
proj = mne.read_proj(meg_path / 'sample_audvis_ecg-proj.fif')
raw.add_proj(proj)
raw.info['bads'] = ['MEG 2443', 'EEG 053']  # mark bad channels

fwd_fname = meg_path / 'sample_audvis-meg-eeg-oct-6-fwd.fif'
ave_fname = meg_path / 'sample_audvis-no-filter-ave.fif'
cov_fname = meg_path / 'sample_audvis-cov.fif'

fwd = mne.read_forward_solution(fwd_fname)
fwd = mne.pick_types_forward(fwd, meg=True, eeg=True, exclude=raw.info['bads'])
cov = mne.read_cov(cov_fname)
info = mne.io.read_info(ave_fname)

label_names = ['Aud-lh', 'Aud-rh']
labels = [mne.read_label(meg_path / 'labels' / f'{ln}.label')
          for ln in label_names]

# %%
# Generate source time courses from 2 dipoles and the corresponding evoked data

times = np.arange(300, dtype=np.float64) / raw.info['sfreq'] - 0.1
rng = np.random.RandomState(42)


def data_fun(times):
    """Generate random source time courses."""
    return (50e-9 * np.sin(30. * times) *
            np.exp(- (times - 0.15 + 0.05 * rng.randn(1)) ** 2 / 0.01))


stc = simulate_sparse_stc(fwd['src'], n_dipoles=2, times=times,
                          random_state=42, labels=labels, data_fun=data_fun)

# %%
# Generate noisy evoked data
picks = mne.pick_types(raw.info, meg=True, exclude='bads')
iir_filter = fit_iir_model_raw(raw, order=5, picks=picks, tmin=60, tmax=180)[1]
nave = 100  # simulate average of 100 epochs
evoked = simulate_evoked(fwd, stc, info, cov, nave=nave, use_cps=True,
                         iir_filter=iir_filter)

# %%
# Plot
plot_sparse_source_estimates(fwd['src'], stc, bgcolor=(1, 1, 1),
                             opacity=0.5, high_resolution=True)

plt.figure()
plt.psd(evoked.data[0])

evoked.plot(time_unit='s')
