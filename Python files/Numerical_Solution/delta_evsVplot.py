import matplotlib.pyplot as plt
import numpy as np

def delta_evsVplot(delta_e,V, value=None):
    if len(delta_e) != len(V):
        raise IOError("arrays C_L and C_D not of equal lenght")
#    Vinv = V**-1
    de_polyfit = np.polyfit(V,delta_e,2)
    de_polyfit = np.poly1d(de_polyfit)
    plt.figure()
    x = np.linspace(min(V),max(V),100)
#    y = de_polyfit(x)**-1
#    print de_polyfit(x)
    plt.plot(V,delta_e,'.',x,de_polyfit(x),'-')
    plt.show()
    if value == None:
        return de_polyfit
    else:
        return de_polyfit(value)

#==========test==========
#delta_e = np.array([-1.2,-0.6,-0.3,0,-1.7,-2.5,-3.2])
#V = np.array([161.,171.,182.,190.,151.,139.,129.])
#print delta_evsVplot(delta_e,V)
