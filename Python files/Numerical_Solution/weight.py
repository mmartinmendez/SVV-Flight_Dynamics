
def weight(W_S,W_pf,W_fuel,i):
    W = W_S+sum(W_pf)-W_fuel[i+2]
    return W