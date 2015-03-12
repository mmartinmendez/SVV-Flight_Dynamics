import matplotlib.pyplot as plt

def CD_alpha(alpha,CD):
    plt.plot(alpha,CD)
    plt.axis([-5, 20, -0.2, 1])
    plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$C_D$')
    plt.title(r"$C_D \  -\ \alpha$")
    plt.show()
