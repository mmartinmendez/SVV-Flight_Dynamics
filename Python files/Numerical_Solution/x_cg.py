import numpy as np

def x_cg(W_S,W,W_fuel,fuelmoment,arm,W_tot,g):
    fuelweight = (np.ones(2)*W[-1]-W_fuel)*0.45359237*g
    moment = fuelmoment[int(round(fuelweight/100.,0))]+sum(W[:-1]*arm[:-1])+W_S*W[-1]
    x_cg = moment/W_tot
    return x_cg