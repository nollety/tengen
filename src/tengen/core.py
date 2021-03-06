"""Core module."""
import xarray as xr

from .resources import coddington_2021_1
from .resources import coddington_2021_high_resolution
from .resources import coddington_2021_p005
from .resources import coddington_2021_p025
from .resources import coddington_2021_p1
from .resources import meftah_2018
from .resources import solid_2017
from .resources import thuillier_2003
from .resources import whi_2008_faculae_active
from .resources import whi_2008_quiet_sun
from .resources import whi_2008_sunspot_active


RESOURCE = {
    "thuillier_2003": thuillier_2003,
    "whi_2008_sunspot_active": whi_2008_sunspot_active,
    "whi_2008_faculae_active": whi_2008_faculae_active,
    "whi_2008_quiet_sun": whi_2008_quiet_sun,
    "solid_2017": solid_2017,
    "meftah_2018": meftah_2018,
    "coddington_2021-high_resolution": coddington_2021_high_resolution,
    "coddington_2021-p005": coddington_2021_p005,
    "coddington_2021-p025": coddington_2021_p025,
    "coddington_2021-p1": coddington_2021_p1,
    "coddington_2021-1": coddington_2021_1,
}


def make(identifier: str) -> xr.Dataset:
    """Make solar irradiance spectrum data set.

    Parameters
    ----------
    identifier: str,
        Data set identifier.

    Returns
    -------
    :class:`~xarray.Dataset`
        Solar irradiance spectrum.

    Raises
    ------
    ValueError:
        If ``identifier`` is unknown.
    """
    return RESOURCE[identifier].get()
