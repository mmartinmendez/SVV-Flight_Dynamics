import matplotlib.pyplot as plt
import numpy as np

def CL_alpha(alpha,CL,value = None):
    CL_polyfit = np.polyfit(alpha,CL,1)
    CL_polyfit = np.poly1d(CL_polyfit)
    x = np.linspace(min(alpha),max(alpha),100)
    plt.figure()
    plt.plot(alpha,CL,'.',x,CL_polyfit(x),'-')
#    plt.axis([-5, 20, -0.2, 1])
    plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$C_L$')
    plt.title(r"$C_L \  -\ \alpha$")
    plt.show()
    if value == None:
        return CL_polyfit
    else:
        return CL_polyfit(value)