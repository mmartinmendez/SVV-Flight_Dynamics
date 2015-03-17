import matplotlib.pyplot as plt
import numpy as np

def CD_alpha(alpha,CD,value = None):
    CD_polyfit = np.polyfit(alpha,CD,2)
    CD_polyfit = np.poly1d(CD_polyfit)
    x = np.linspace(min(alpha),max(alpha),100)
    plt.figure()
    plt.plot(alpha,CD,'.',x,CD_polyfit(x),'-')
#    plt.axis([-5, 20, -0.2, 1])
    plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$C_D$')
    plt.title(r"$C_D \  -\ \alpha$")
    plt.show()
    if value == None:
        return CD_polyfit
    else:
        return CD_polyfit(value)