import numpy as np
def weight(W_S,W_pf,W_fuel,g):
    W = np.zeros(len(W_fuel[:,0])-2)
    for i in range(len(W_fuel[:,0])-2):
        W[i] = (W_S+sum(W_pf[0:-1])*g+W_pf[-1]*g*0.45359237-sum(W_fuel[i+2,:]))
    return W

#=================test=================
#W_S = 100
#W_pf = np.arange(7)
#W_fuel = np.transpose(np.vstack((np.arange(10),np.arange(10))))
#g = 9.81
#W = weight(W_S,W_pf,W_fuel,g)
#print W