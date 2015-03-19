from math import *
def TAS(P_0,a,h_p,T_0,g_0,R,gamma,V):
    TAS  = []
    #find P
    P = P_0*(1+a*h_p/T_0)**(-g_0/(a*R))
    for i in range(len(V)):
        #Find M
        M = sqrt(2./(gamma-1.)*((1.+P_0/P*((1.+(gamma-1.)/(2.*gamma)*p_0/P_0*V[i]**2.)**(gamma/(gamma-1.))-1.))**((gamma-1.)/gamma)-1.))
    
        #Find T
        T = T_m/(1+(gamma-1)/2*M**2)
    
        #Find p (rho)
        p = P/(R*T)
    
        #Find V_t
        V_t = V*sqrt(p_0/p)
        
        TAS.append(V_t)