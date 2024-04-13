import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
    pmt = face * couponRate / ppy
    times = np.arange(1, m * ppy + 1)
    dfs = (1 + y / ppy) ** times
    cf = np.full(m * ppy, pmt)
    cf[-1] += face  
    
    pv = cf / dfs
    
    duration = np.sum(times * pv) / np.sum(pv)
    duration /= ppy  
    
    return duration


