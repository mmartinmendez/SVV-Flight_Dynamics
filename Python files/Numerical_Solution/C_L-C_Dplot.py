import matplotlib.pyplot as plt

def C_LvsC_Dplot(CL,CD):
    plt.plot(CL,CD)
    plt.axis([-5, 20, -0.2, 1])
    plt.xlabel(r'$C_L$')
    plt.ylabel(r'$C_D$')
    plt.title(r"$C_L \  -\ C_D$")
    plt.show()