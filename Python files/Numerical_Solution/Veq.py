import numpy as np
def Veq(V,W,W_S):
    Veq = V*0.514444444*np.sqrt(W_S*W**-1)
    return Veq