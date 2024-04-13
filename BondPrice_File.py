import numpy as np
def getBondPrice(y, face, couponRate, m, ppy):
    dfs=(1+(y/ppy))**-np.arange(1,m*ppy+1)
    discounted_coupons=sum(face*couponRate/ppy*dfs)
    discounted_face=face*dfs[-1]
    return(discounted_coupons+discounted_face)