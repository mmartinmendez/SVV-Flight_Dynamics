import matplotlib.pyplot as plt

def CL_alpha(alpha,CL):
    plt.plot(alpha,CL)
    plt.axis([-5, 20, -0.2, 1])
    plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$C_L$')
    plt.title(r"$C_L \  -\ \alpha$")
    plt.show()