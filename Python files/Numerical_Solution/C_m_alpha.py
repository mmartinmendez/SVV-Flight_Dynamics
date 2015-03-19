import numpy as np
import math as m

def C_m_alpha(alpha,delta_e,C_m_delta):
    de_polyfit = np.polyfit(alpha*(m.pi/180),delta_e,1)
    de_polyfit = np.poly1d(de_polyfit)
    deda = de_polyfit[1]
    Cma = -deda*C_m_delta
    return Cma