import matplotlib.pyplot as plt
import numpy as np

def FevsVplot(F_e,V, value = None):
    if len(F_e) != len(V):
        raise IOError("arrays are not of equal lenght")
    Fe_polyfit = np.polyfit(V,F_e,2)
    Fe_polyfit = np.poly1d(Fe_polyfit)
    plt.figure()
    x = np.linspace(min(V),max(V),100)
    plt.xlabel(r'$V_e$')
    plt.ylabel(r'$F_e$')
    plt.title(r"$F_e \  -\ V_e$")
    plt.plot(V,F_e,'.',x,Fe_polyfit(x),'-')
    plt.show()
    if value == None:
        return Fe_polyfit
    else:
        return Fe_polyfit(value)