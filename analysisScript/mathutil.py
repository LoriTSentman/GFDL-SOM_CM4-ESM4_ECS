# Filename: mathutil.py

"""
General mathematical routines
"""

import numpy as np


__all__ = ['globalAveAtmos']


def globalAveAtmos(var,lat):
    """
    Global area-weighted atmosphere variable average
    Parameters
    ----------
    var : float
        Atmos variable to global average
    lat : float
        Latitude array for area-weighting
    Returns
    -------
    weights : float
        Latitude area weights
    var_gave : float
        Global average
    """
    weights = np.cos(np.deg2rad(lat))
    var_latave = np.average(var[:][:][:],weights=weights,axis=(1)) 
    var_gave = np.average(var_latave[:],axis=(1))
    return(weights,var_gave)
