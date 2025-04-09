# Filename: utils.py

"""
General purpose module containing routines:
-used in multiple notebooks; or 
-complicated and would thus otherwise clutter notebook design.
"""

import os
import sys
import re
import socket
import matplotlib.pyplot as plt

__all__ = ['systemExit','printDebug','verifyPath','getNested','getDictItemsNested','removeItemsByKeyNested','removeItemsByKeyListNested','removeItemsByValueNested','saveFig','writeStats','setFigure','setPanel']


def systemExit(m):
    """
    Stops cells running
    Parameters
    ----------
    m : str
        failure-specific message
    """
    sys.tracebacklimit = 0
    raise SystemExit(m)


def printDebug(flag, *args, **kwargs):
    """
    Prints debug information if debug_flag=True
    Parameters:
    -----------
    flag : bool
        flag to enable or disable debug printing
    *args : 
        variable length argument list to print
    **kwargs : 
        arbitrary keyword arguments to pass to print function
    """
    if flag:
        print(*args, **kwargs)


def verifyPath(p):
    """
    Checks existence of pathname.
    Parameters
    ----------
    p : str
        pathname
    """
    if os.path.exists(p):
        print(f"Path found: {p}")
    else:
        sys.tracebacklimit = 0
        raise SystemExit(f"ERROR! Path not found: {p}. Check pathname specification. Exiting...")

def getNested(data, *args):
    """
    Returns items of nested dictionary based on arguments.
    Parameters
    -----------
    data : dict
        Name of nested dictionary
    *args : (optional)
        keys of nested dictionary to get values for
    Return
    ------
    value : 
        Value of specified key arguments
    """
    if args and data:
        element  = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else getNested(value, *args[1:])

def getDictItemsNested(d):
    """
    Returns nested dictionary items in a structure order.
    Parameters
    ----------
    d : dict 
        nested dictionary name
    Returns
    -------
    ko : int
        outer key
    ki :
        inner key
    v :  
        value for inner key 
    """
    for ko, inner_dict in d.items():
        print(f"Outer Key: {ko}")
        for ki, v in inner_dict.items():
            print(f"Inner Key: {ki}, Value: {v}")
    return(ko,ki,v)


def removeItemsByKeyNested(d,k):
    """
    Returns dictionary with items matching specified key(s)
      omitted.
    Parameters
    ----------
    d : dict
        input nested dictionary
    k : float, list[optional]
        key or list of keys to match for omitting items
    Returns
    -------
    dnew : dict
        new dictionary with omitted items matching keys
    """
    if not d:
        systemExit(f"ERROR: removeItemsByKeyNested: dictionary argument must be specified.") 
    if not k:
        systemExit(f"ERROR: removeItemsByKeyNested: key or list of keys to remove must be specified as an argument.")
    dnew = {}
    for ko, inner_dict in d.items():
        dnew[ko] = {ki : v for ki, v in list(inner_dict.items()) if ki not in k or ki != k}
    return dnew

def removeItemsByKeyListNested(d,k):
    """
    Returns dictionary with items matching specified key(s)
      omitted.
    Parameters
    ----------
    d : dict
        input nested dictionary
    k : list
        list of keys to match for omitting items
    Returns
    -------
    dnew : dict
        new dictionary with omitted items matching keys
    """
    if not d:
        systemExit(f"ERROR: removeItemsByKeyListNested: dictionary argument must be specified.")
    if not k:
        systemExit(f"ERROR: removeItemsByKeyListNested: list of keys to remove must be specified as an argument.")
    dnew = {}
    for ko, inner_dict in d.items():
        dnew[ko] = {ki : v for ki, v in list(inner_dict.items()) if ki not in k}
    return dnew



def removeItemsByValueNested(d,v):
    """
    Returns dictionary with items matching specified 
      value(s) omitted.
    Parameters
    ----------
    d : dict
        input nested dictionary
    v : float, list[optional]
        value or list of values to match for omitting items
    Returns
    -------
    dnew : dict
        new dictionary with omitted items matching values
    """
    if not d:
        systemExit(f"ERROR: removeItemsByKeyNested: dictionary argument must be specified.")
    if not v:
        systemExit(f"ERROR: removeItemsByKeyNested: value or list of values to remove must be specified as an argument.")
    dnew = {}
    for ko, inner_dict in d.items():
        dnew[ko] = {ki : val for ki, val in list(inner_dict.items()) if ki not in v or ki != v}
    return dnew



def saveFig(f,dpi=300):
    """
    Saves figure in PNG and PDF format with specified dpi
        and output filename/path from notebook.
    Parameters
    ----------
    f : str
        output path/filename
    dpi : integer (default=300)
        resolution of figure
    """
    plt.savefig(f+'.png', dpi=dpi)
    plt.savefig(f+'.pdf', dpi=dpi)


def writeStats(f,m,msg):
    """
    Writes output to notebook and text file.
    Parameters
    ----------
    f : str
        output path/filename
    m : str 
        mode: 'w' write
              'a' append
              'x' exclusive creation (creates if doesn't exist)
    msg : str
        message to write/output
    """
    with open(f+'.txt', m) as fout:
        print(msg)
        print(msg, file=fout)

def setFigure(picas,aspect=(11,8),is_tight=True):
    """
    Computes plot figure size based on aspect ratio and sets up figure.
    Parameters
    ----------
    picas : integer
        used to compute figure aspect ratio and size
    aspect : integer array (default=(11,8))
        figure size to compute correct aspect ratio of figure size
    is_tight : bool (default=True)
        flag to automatically adjust parameters to fit figure area
    """
    w = picas * (1./6.)*2.
    h = w * (float(aspect[1])/float(aspect[0]))
    if is_tight:
        print("Using tight layout")
        return plt.figure(figsize=(w,h),tight_layout=True)
    else:
        return plt.figure(figsize=(w,h),tight_layout=False)

def setPanel(t,tx,ty,xt,xl,yt,yl):
    """
    Sets up figure panels including titles,x and y axis labels, limits, etc.
    Parameters
    ----------
    t : str
        Panel title
    tx : integer
        x-axis value for panel title location
    ty : integer
        y-axis value for panel title location
    xt : str
        x-axis label
    xl : array
        array of x-axis limits
    yt : str
        y-axis label
    yl : array
        array of y-axis limits
    """
    panelfont = {'family':'Noto Sans CJK JP', 'weight':'semibold', 'size':16}
    axisfont = {'family':'DejaVu Sans', 'size':18}
    return plt.tick_params(axis='both',which='major',labelsize=18), plt.text(tx,ty,t,fontdict=panelfont), plt.xlim(xl), plt.ylim(yl), plt.ylabel(yt,fontdict=axisfont), plt.xlabel(xt,fontdict=axisfont)  


"""def compute_weighted_gmean(lat,var):
  Compute area-weighted global mean

    Parameters
    ----------
    lat : float
         Data latitude to compute weights
    var : string
        Variable to compute
   
    weights = np.cos(np.deg2rad(lat))
    wvarts= np.average(var[:][:][:],weights=weights,axis=(1)) 
    wvargmts = np.average(wvarts[:],axis=(1))
    wvargmta = np.average(wvargmts[:])
    
   return: weights - area-ave weights(lat)
               wvarts - weighted lat-ave var(time,lon)
               wvargmts - weighted global mean var(time)
               wvargmta - weighted global time mean var

    return weights,wvarts, wvargmts, wvargmta"""
