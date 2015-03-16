import numpy as np
def weight(W_S,W_pf,W_fuel,i):
    W = np.zeros(len(W_fuel[0])-2)
    for i in range(len(W_fuel[0])-2):
        W[i] = (W_S+sum(W_pf)-sum(W_fuel[i+2]))