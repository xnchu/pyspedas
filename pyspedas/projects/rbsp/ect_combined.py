import logging

from pytplot import cdf_to_tplot
from pytplot import time_clip as tclip

from pyspedas.projects.rbsp.config import CONFIG
from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download import download


def ect_combined(trange=["2015-11-5", "2015-11-6"], probe="a", level="l3", prefix="", suffix="", force_download=False, get_support_data=False, varformat=None, varnames=[], downloadonly=False, notplot=False, no_update=False, time_clip=False):
    """
    This function loads combined data from the Energetic Particle, Composition, and Thermal Plasma Suite (ECT) from https://rbsp-ect.newmexicoconsortium.org/rbsp_ect.php
    The combined data is not available from the NASA SPDF data portal.
    The l2 data files are available at
       https://rbsp-ect.newmexicoconsortium.org/data_pub/rbspa/ECT/level2/2015/rbspa_ect-elec-L2_20150101_v2.1.0.cdf
    The l3 data files are available at
        https://rbsp-ect.newmexicoconsortium.org/data_pub/rbspa/ECT/level3/2015/rbspa_ect-elec-L3_20150103_v1.0.0.cdf

    Parameters
    ----------
        trange : list of str, default=['2015-11-5', '2015-11-6']
            time range of interest [starttime, endtime] with the format
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        probe : str or list of str, default='a'
            Spacecraft probe name: 'a' or 'b'

        level : str, default='l3'
            Data level. Valid options: 'l2', 'l3'

        prefix : str, optional
            The tplot variable names will be given this prefix. By default, no prefix is added.

        suffix: str, optional
            The tplot variable names will be given this suffix.  By default,
            no suffix is added.

        force_download : bool, default=False
            Download file even if local version is more recent than server version.

        get_support_data: bool, default=False
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a
            "VAR_TYPE" attribute of "data".

        varformat: str, optional
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        varnames: list of str, optional
            List of variable names to load (if not specified,
            all data variables are loaded)

        downloadonly: bool, default=False
            Set this flag to download the CDF files, but not load them into
            tplot variables

        notplot: bool, default=False
            Return the data in hash tables instead of creating tplot variables

        no_update: bool, default=False
            If set, only load data from your local cache

        time_clip: bool, default=False
            Time clip the variables to exactly the range specified in the trange keyword

    Returns
    -------
    tvars : dict or list
        List of created tplot variables or dict of data tables if notplot is True.

    Examples
    --------
    >>> hope_vars = pyspedas.projects.rbsp.hope(trange=['2018-11-5', '2018-11-6'], level='l2')
    >>> tplot('Ion_density')
    """

    if not isinstance(probe, list):
        probe = [probe]

    out_files = []

    if notplot:
        tvars = {}
    else:
        tvars = []

    if prefix is None:
        prefix = ""

    if suffix is None:
        suffix = ""

    for prb in probe:

        if level == "l2":
            pathformat = f"rbsp{prb}/ECT/level2/%Y/rbsp{prb}_ect-elec-L2_%Y%m%d_v*.cdf"
        elif level == "l3":
            pathformat = f"rbsp{prb}/ECT/level3/%Y/rbsp{prb}_ect-elec-L3_%Y%m%d_v*.cdf"
        else:
            raise ValueError(f"Invalid level: {level}")

        # find the full remote path names using the trange
        remote_names = dailynames(file_format=pathformat, trange=trange)

        remote_path = "https://rbsp-ect.newmexicoconsortium.org/data_pub/"
        files = download(remote_file=remote_names, remote_path=remote_path, local_path=CONFIG["local_data_dir"], no_download=no_update, force_download=force_download)
        if files:
            out_files.extend(files)

        if not downloadonly:
            tvars_o = cdf_to_tplot(sorted(out_files), prefix=prefix, suffix=suffix, get_support_data=get_support_data, varformat=varformat, varnames=varnames, notplot=notplot)

            if notplot:
                tvars.update(tvars_o)
            else:
                tvars.extend(tvars_o)

    if downloadonly:
        return sorted(out_files)

    if notplot:
        return tvars

    if time_clip:
        for new_var in tvars:
            tclip(new_var, trange[0], trange[1], suffix="")

    return tvars


if __name__ == "__main__":
    ect_combined(trange=["2015-11-5", "2015-11-6"], level="l2")
    from pytplot import tplot_names

    print(tplot_names())
