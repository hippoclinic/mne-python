Glossary
========

.. currentmodule:: mne

The Glossary provides short definitions of vocabulary specific to MNE-Python and
general neuroimaging concepts. If you think a term is missing, please consider
`creating a new issue`_ or `opening a pull request`_ to add it.

.. glossary::
    :sorted:


    annotations
        An annotation is defined by an onset, a duration, and a textual
        description. It can contain information about the experiment, but
        also details on signals marked by a human such as bad data segments,
        sleep stages, sleep events (spindles, K-complex), and so on.
        An :class:`Annotations` object is a container for multiple annotations,
        which is available as the ``annotations`` attribute of :class:`~io.Raw`
        objects. See :class:`Annotations` for the class definition and
        :ref:`tut-events-vs-annotations` for a short tutorial.
        See also :term:`events`.

    beamformer
        A beamformer is a popular source estimation approach that uses a set of
        spatial filters (beamformer weights) to compute time courses of sources
        at predefined locations. See :class:`beamformer.Beamformer` for the class
        definition. See also :term:`LCMV`.

    BEM
    boundary element model
    boundary element method
        BEM is the acronym for boundary element method or boundary element
        model. Both are related to the definion of the conductor model in the
        forward model computation. The boundary element model consists of surfaces
        such as the inner skull, outer skull, and outer skin (scalp) that define
        compartments of tissues of the head. You can compute the BEM surfaces with
        :func:`bem.make_watershed_bem` or :func:`bem.make_flash_bem`.
        See :ref:`tut-forward` for a usage demo.

    channels
        Channels refer to MEG sensors, EEG electrodes or other sensors such as
        EOG, ECG, sEEG, ECoG, etc. Channels usually have
        a type (such as gradiometer), and a unit (such as T/m) used e.g. for
        plotting. See also :term:`data channels`.

    data channels
        Many functions in MNE-Python operate on "data channels" by default. These
        are channels that contain electrophysiological data from the brain,
        as opposed to other channel types such as EOG, ECG, stimulus/trigger,
        or acquisition system status data. The set of channels considered
        "data channels" in MNE contains the following types (together with scale
        factors for plotting):

        .. mne:: data channels list

    DC
    direct current
        The part of a signal that stays constant over time. The "DC offset"
        of electrophysiological signals is often dealt with by high-pass
        filtering or by subtracting some suitable baseline.

    DICS
    dynamic imaging of coherent sources
        Dynamic Imaging of Coherent Sources is a method for computing source
        power in different frequency bands. See :ref:`ex-inverse-source-power`
        and :func:`beamformer.make_dics` for more details.

    digitization
        Digitization is a procedure of recording the head shape and locations of
        fiducial coils (or :term:`HPI`) and/or EEG electrodes on the head. They
        are represented as a set of points in 3D space.
        See :ref:`reading-dig-montages` and :ref:`dig-formats`.

    dipole
    ECD
    equivalent current dipole
        An equivalent current dipole (ECD) is an approximate representation of
        post-synaptic activity in a small cortical region. The intracellular
        currents that give rise to measurable EEG/MEG signals are thought to
        originate in populations of cortical pyramidal neurons aligned
        perpendicularly to the cortical surface. Because the length of such
        current sources is very small relative to the distance between the
        cortex and the EEG/MEG sensors, the fields measured by these techniques
        are well approximated by (i.e., equivalent to) fields generated by
        idealized point sources (dipoles) located on the cortical surface.

    dSPM
    dynamic statistical parametric mapping
        Dynamic statistical parametric mapping (dSPM) gives a noise-normalized
        minimum-norm estimate at a given source location. It is calculated by
        dividing the activity estimate at each source location by the baseline
        standard deviation of the noise.

    eLORETA
    sLORETA
        eLORETA and sLORETA (exact and standardized low resolution brain
        electromagnetic tomography) are linear source estimation techniques
        like :term:`dSPM` and :term:`MNE`. sLORETA outputs
        standardized values (like dSPM), while eLORETA generates normalized
        current estimates. See :func:`minimum_norm.apply_inverse`,
        :ref:`tut-inverse-methods`, and :ref:`example-sLORETA`.

    epochs
        Epochs (sometimes called "trials" in other software packages) are
        equal-length segments of data extracted from continuous data. Usually,
        epochs are extracted around stimulus events or responses,
        though sometimes sequential or overlapping epochs are used (e.g.,
        for analysis of resting-state activity). See :class:`Epochs` for the
        class definition and :ref:`tut-epochs-class` for a narrative overview.

    events
        Events correspond to specific time points in raw data, such as triggers,
        experimental condition events, etc. MNE-Python represents events with
        integers stored in NumPy arrays of shape ``(n_events, 3)``. The first
        column contains the event onset (in samples) with :term:`first_samp`
        included. The last column contains the event code. The second
        column contains the signal value of the immediately preceding sample,
        and reflects the fact that event arrays sometimes originate from
        analog voltage channels ("trigger channels" or "stim channels"). In
        most cases, the second column is all zeros and can be ignored.
        Event arrays can be created with :func:`mne.make_fixed_length_events`,
        :func:`mne.read_events`, and :func:`mne.find_events`.
        See :ref:`tut-events-vs-annotations` for a short tutorial.
        See also :term:`annotations`.

    evoked
        Evoked data are obtained by averaging epochs. Typically, an evoked object
        is constructed for each subject and each condition, but it can also be
        obtained by averaging a list of evoked objects over different subjects.
        See :class:`EvokedArray` for the class definition and
        :ref:`tut-evoked-class` for a narrative overview.

    fiducial
    fiducial point
    anatomical landmark
        Fiducials are objects placed in the field of view of an imaging system
        to act as known spatial references that are easy to localize.
        In neuroimaging, fiducials are often placed on anatomical landmarks
        such as the nasion (NAS) or left/right preauricular points (LPA and
        RPA).

        These known reference locations are used to define a coordinate system
        for localizing sensors (hence NAS, LPA and RPA are often
        called "cardinal points" because they define the cardinal directions of
        the head coordinate system). The cardinal points are also useful when
        co-registering measurements in different coordinate systems (such as
        aligning EEG sensor locations to an MRI of the head).

        Due to the common neuroimaging practice of placing fiducial objects on
        anatomical landmarks, the terms "fiducial", "anatomical landmark", and
        "cardinal point" are often (erroneously) used interchangeably.

    first_samp
        The :attr:`~io.Raw.first_samp` attribute of :class:`~io.Raw`
        objects is an integer representing the number of time samples that
        passed between the onset of the hardware acquisition system and the
        time when data recording started. This approach to sample
        numbering is a peculiarity of VectorView MEG systems, but for
        consistency it is present in all :class:`~io.Raw` objects
        regardless of the source of the data. In other words,
        :attr:`~io.Raw.first_samp` will be ``0`` in :class:`~io.Raw`
        objects loaded from non-VectorView data files. See also
        :term:`last_samp`.

    forward
    forward solution
        The forward solution is a linear operator capturing the
        relationship between each dipole location in the :term:`source space`
        and the corresponding field distribution measured by the sensors
        (the "lead field matrix"). Calculating a forward solution requires a
        conductivity model of the head, which encapsulates the geometries and
        electrical conductivities of the different tissue compartments (see
        :term:`boundary element model` and :class:`bem.ConductorModel`).
        For information about the Forward object and the data it stores, see
        :class:`mne.Forward`.

    GFP
    global field power
        Global Field Power (GFP) is a measure of the (non-)uniformity
        of the electromagnetic field at the sensors. It is typically calculated
        as the standard deviation of the sensor values at each time point. Thus,
        it is a one-dimensional time series capturing the spatial variability
        of the signal across sensor locations.

    HED
    hierarchical event descriptors
        Hierarchical event descriptors (HED) are tags that use
        keywords separated by slashes (/) to describe different types of
        experimental events (for example, ``stimulus/circle/red/left`` and
        ``stimulus/circle/blue/left``). These tags can be used to group
        experimental events and select event types for analysis.

    HPI
    cHPI
    head position indicator
        Head position indicators (HPI, sometimes cHPI for
        *continuous* head position indicators) are small coils attached to a
        subject's head during MEG acquisition. Each coil emits a sinusoidal
        signal of a different frequency, which is picked up by the MEG sensors
        and can be used to infer the head position. With cHPI, the sinusoidal
        signals are typically set at frequencies above any neural signal of
        interest, and thus can be removed after head position correction via
        low-pass filtering. See :ref:`tut-head-pos`.

    info
    measurement info
        A "measurement info" (or short "info") object is a collection of metadata
        related to :class:`~io.Raw`, :class:`Epochs`, or :class:`Evoked`
        objects. It contains channel locations and types, sampling frequency,
        preprocessing history such as filters, etc.
        See :ref:`tut-info-class` for a narrative overview.

    inverse
    inverse operator
        The inverse operator is an :math:`M \times N` matrix (:math:`M` source
        locations by :math:`N` sensors) that, when applied to the sensor
        signals, yields estimates of the brain activity that gave rise to the
        observed sensor signals. Inverse operators are available for the linear
        inverse methods :term:`MNE`, :term:`dSPM`, :term:`sLORETA`, and
        :term:`eLORETA`. See :func:`minimum_norm.apply_inverse`.

    label
        A :class:`Label` refers to a defined region in the cortex, often called
        a region of interest (ROI) in the literature. Labels can be defined
        anatomically (based on the physical structure of the cortex) or functionally
        (based on cortical responses to specific stimuli). See also :term:`ROI`.

    last_samp
        The :attr:`~io.Raw.last_samp` attribute of :class:`~io.Raw`
        objects is an integer representing the number of time samples that
        passed between the start and end of data recording. This approach to sample
        numbering is a peculiarity of VectorView MEG systems, but for
        consistency it is present in all :class:`~io.Raw` objects
        regardless of the source of the data. See also :term:`first_samp`.

    layout
        A :class:`~channels.Layout` gives sensor positions in two
        dimensions (defined by ``x``, ``y``, ``width``, and ``height`` values for
        each sensor). It is primarily used for illustrative purposes (i.e., making
        diagrams of approximate sensor positions in cartoons of the head,
        so-called topographies or topomaps). See also :term:`montage`.

    LCMV
    LCMV beamformer
        Linearly constrained minimum variance beamformer attempt to
        estimate activity for a given source while suppressing cross-talk from
        other regions (:func:`beamformer.make_lcmv`). See also
        :term:`beamformer`.

    FreeSurfer LUT
    LUT
        A FreeSurfer lookup table (LUT) provides a mapping between a given
        volumetric atlas or surface label name, its integer value
        (e.g., in ``aparc+aseg.mgz``), and its standard color (see the
        `FreeSurfer wiki <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT>`__
        for more information). Custom LUTs can be also be created from different
        surface parcellations, see for example `this comment about HCPMMP
        <https://github.com/mne-tools/mne-python/pull/7639#issuecomment-625907891>`__.

    maximum intensity projection
        A method to display pixel-wise activity within some volume by
        finding the maximum value along a vector from the viewer to the pixel
        (i.e., along the vector pependicular to the view plane).

    MNE
    minimum-norm estimate
    minimum-norm estimation
        Minimum-norm estimation (MNE) can be used to generate a distributed
        map of activation on a :term:`source space` (usually on a cortical surface).
        MNE uses a linear :term:`inverse operator` to project sensor measurements
        into the source space. The :term:`inverse operator` is computed from the
        :term:`forward solution` for a subject and an estimate of the
        :term:`noise covariance` of sensor measurements.

    montage
        EEG channel names and relative positions of sensors on the scalp.
        While layouts are 2D locations, montages are 3D locations. A montage
        can also contain locations for HPI points, fiducial points, or
        extra head shape points.
        See :class:`~channels.DigMontage` for the class definition. See also
        :term:`layout`.

    morphing
        Morphing refers to the operation of transferring source estimates from
        one anatomy to another. It is known as realignment in the fMRI
        literature. This operation is necessary for group studies to get the
        data into a common space for statistical analysis.
        See :ref:`ch_morph` for more details.

    OPM
    optically pumped magnetometer
        An optically pumped magnetometer (OPM) is a type of magnetometer
        that uses a laser passing through a gas (e.g., rubidium) to sense
        magnetic fluctuations. OPMs can operate near room temperature.

    noise covariance
        The noise covariance is a matrix that contains the covariance between data
        channels. It is a square matrix with shape ``n_channels`` :math:`\times`
        ``n_channels``. It is especially useful when working with multiple sensor
        types (e.g. EEG and MEG). In practice, the matrix is estimated from baseline
        periods or empty room measurements, and it also provides a noise model
        that can be used for subsequent analysis (like source imaging).

    path-like
        Something that acts like a path in a file system. This can be a `str`
        or a `pathlib.Path`.

    pick
        An integer that is the index of a channel in the :term:`measurement info`.
        It allows to obtain the information on a channel in the list of channels
        available in ``info['chs']``.

    projector
    SSP
        A projector, also referred to as Signal Space
        Projection (SSP), defines a linear operation applied spatially to EEG
        or MEG data. A matrix multiplication of an SSP projector with the data
        will reduce the rank of the data by projecting it to a
        lower-dimensional subspace. Such projections are typically applied to
        both the data and the forward operator when performing
        source localization. Note that EEG average referencing can be done
        using such a projection operator. Projectors are stored alongside data
        in the :term:`measurement info` in the field ``info['projs']``.

    raw
        `~io.Raw` objects hold continuous data (preprocessed or not), typically
        obtained from reading recordings stored in a file.
        See :class:`~io.RawArray` for the class definition and :ref:`tut-raw-class`
        for a narrative overview.

    RAS
        Right-Anterior-Superior, denoting the standard way to define coordinate
        frames in MNE-Python:

        R
            +X is right, -X is left
        A
            +Y is anterior (front), -Y is posterior (rear)
        S
            +Z is superior (top), -Z is inferior (bottom)

    ROI
    region of interest
        A spatial region where an experimental effect is expected to manifest.
        This can be a collection of sensors or, when performing inverse imaging,
        a set of vertices on the cortical surface or within the cortical volume.
        See also :term:`label`.

    selection
        A selection is a set of picked channels (for example, all sensors
        falling within a :term:`region of interest`).

    STC
    source estimate
    source time course
        Source estimates, commonly referred to as STC (Source Time Courses),
        are obtained from source localization methods such as :term:`dSPM`,
        :term:`sLORETA`, :term:`LCMV`, or MxNE.
        STCs contain the amplitudes of the neural sources over time.
        In MNE-Python, :class:`SourceEstimate` objects only store the
        amplitudes of activation but not the locations of the sources. The
        locations are stored separately in the :class:`SourceSpaces` object
        that was used to compute the forward operator.
        See :class:`SourceEstimate`, :class:`VolSourceEstimate`,
        :class:`VectorSourceEstimate`, and :class:`MixedSourceEstimate`.

    source space
        A source space specifies where in the brain source amplitudes are
        estimated. It corresponds to locations of a set of
        candidate :term:`equivalent current dipoles<ECD>`. MNE-Python mostly
        works with source spaces defined on the cortical surfaces estimated
        by FreeSurfer from a T1-weighted MRI image. See :ref:`tut-forward`
        to read about how to compute a forward operator in a source space.
        See :class:`SourceSpaces` for the class definition and information
        about the data it contains.

    SQUID
    superconducting quantum interference device
        A superconducting quantum interference device (SQUID) is a type of
        magnetometer that uses superconducting materials to sense magnetic
        fluctuations. Standard low-temperature SQUID sensors typically found
        in MEG systems operate at temperatures within a few degrees of
        absolute zero (e.g., below 4 K).

    stim channel
    trigger channel
        A stim channel or trigger channel is a channel that encodes
        events during the recording. It is typically a channel that is always
        zero and takes positive values when something happens (such as the
        onset of a stimulus or a subject response). Stim channels are often
        prefixed with ``STI`` to distinguish them from other channel types. See
        :ref:`stim-channel-defined` for more details.

    template montage
        An idealized EEG :term:`montage`, often provided by the manufacturer
        of the EEG system or cap. The electrode positions were not actually
        measured on the participants' heads, but rather were calculated
        assuming optimal theoretical placement on a sphere.

    tfr
        A time-frequency representation (TFR) is often a spectrogram (STFT) or
        scaleogram (wavelet) showing the frequency content as a function of
        time.

    trans
        A coordinate frame affine transformation, usually between the Neuromag head
        coordinate frame and the MRI Surface RAS coordinate frame used by Freesurfer.

    whitening
        A linear operation that transforms data with a known covariance
        structure into "whitened data", which has a covariance structure equal to
        the identity matrix. In other words, whitening creates virtual channels that
        are uncorrelated and have unit variance. This is also known as a
        sphering transformation.

        The term "whitening" comes from the fact that light with a flat
        frequency spectrum in the visible range is white, whereas
        non-uniform frequency spectra lead to perception of different colors
        (e.g., "pink noise" has a ``1/f`` characteristic, which for visible
        light would appear pink).

.. LINKS

.. _`creating a new issue`:
   https://github.com/mne-tools/mne-python/issues/new?template=glossary.md
.. _`opening a pull request`:
   https://github.com/mne-tools/mne-python/pull/new/main
