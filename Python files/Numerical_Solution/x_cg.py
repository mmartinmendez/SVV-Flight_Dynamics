import numpy as np

def x_cg(W_S,W,W_fuel,fuelmoment,arm,W_tot,g):
    fuelweight = (np.ones(2)*W[-1]-W_fuel)
    #moment1 in lbs*inch
    moment1 = fuelmoment[int(round(fuelweight[0]/100.,0))-1,1]+sum(W[:-1]*2.20462262*arm[:-1])+W_S/g*2.20462262*arm[-1]      
    moment1 = moment1*4.44822162825*0.0254 #[Nm]
    x_cg1 = moment1/W_tot[0] #[m]
    arm2 = arm
    arm2[-2] = arm[2]
    #moment2 in lbs*inch
    moment2 = fuelmoment[int(round(fuelweight[1]/100.,0))-1,1]+sum(W[:-1]*2.20462262*arm2[:-1])+W_S/g*2.20462262*arm[-1]
    moment2 = moment2*4.44822162825*0.0254 #[Nm]
    x_cg2 = moment2/W_tot[1] #[m]
    dx_cg = x_cg1-x_cg2
    return dx_cg