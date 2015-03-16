import numpy as np
def Ve(V,W,W_S):
    Ve = V*np.sqrt(W_S/W)
    return 0