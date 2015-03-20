# Citation 550 - Linear simulation

# xcg = 0.25*c

# Stationary flight condition

import math
from numpy import*


hp0    =  1         	  # pressure altitude in the stationary flight condition [m]
V0     =  1         # true airspeed in the stationary flight condition [m/sec]
alpha0 =  1      	  # angle of attack in the stationary flight condition [rad]
th0    =  1      	  # pitch angle in the stationary flight condition [rad]
q0     =  0
# Aircraft mass
m      =  1        	  # mass [kg]

# Set values for the manuovres

results_data = loadtxt('input.txt')

hp0 = results_data[0]
V0 = results_data[1]
alpha0 = results_data[2]
th0 = results_data[3]
q0 = results_data[4]
m = results_data[5]

# aerodynamic properties
e      =  0.598607792739          # Oswald factor [ ]
CD0    =  0.0268891723086           # Zero lift drag coefficient [ ]
CLa    =  4.40100457224          # Slope of CL-alpha curve [ ]

# Longitudinal stability
Cma    =  -0.561377830286           # longitudinal stabilty [ ]
Cmde   =  -0.825489971065          # elevator effectiveness [ ]





#----------------Values above changed for usability---------------#

# Aircraft geometry

S      = 30.00	          # wing area [m**2]
Sh     = 0.2*S           # stabiliser area [m**2]
Sh_S   = Sh/S	          # [ ]
lh     = 0.71*5.968      # tail length [m]
c      = 2.0569	  # mean aerodynamic cord [m]
lh_c   = lh/c	          # [ ]
b      = 15.911	  # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b**2/S           # wing aspect ratio [ ]
Ah     = bh**2/Sh         # stabilser aspect ratio [ ]
Vh_V   = (Sh*lh)/(S*c)		  # [ ]
ih     = -2*math.pi/180       # stabiliser angle of incidence [rad]


# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m**3]
lam = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m**2/sec**2K]
g      = 9.81            # [m/sec**2] (gravity constant)
gamma = 1.4     #added myself (Twan)
P_0 = 101325.

rho    = rho0*((1+(lam*hp0/Temp0)))**(-((g/(lam*R))+1))   # [kg/m**3]  (air density)
W      = m*g				                        # [N]       (aircraft weight)

# Constant values concerning aircraft inertia

muc    = m/(rho*S*c)
mub    = m/(rho*S*b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.3925


# Aerodynamic constants

Cmac   = 0                     # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa   		        # Wing normal force slope [ ]
CNha   = 2*math.pi*Ah/(Ah+2)        # Stabiliser normal force slope [ ]
depsda = 4/(A+2)               # Downwash gradient [ ]

# Lift and drag coefficient

CL = 2*W/(rho*V0**2*S)               # Lift coefficient [ ]
CD = CD0 + (CLa*alpha0)**2/(math.pi*A*e)  # Drag coefficient [ ]

# Stabiblity derivatives

CX0    = W*math.sin(th0)/(0.5*rho*V0**2*S)
CXu    = -0.02792
CXa    = -0.47966
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728

CZ0    = -W*math.cos(th0)/(0.5*rho*V0**2*S)
CZu    = -0.37616
CZa    = -5.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cm0    = 0.0297
Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415
CmTc   = -0.0064

CYb    = -0.7500
CYbdot =  0
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939


