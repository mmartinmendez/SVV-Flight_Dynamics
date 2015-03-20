clc
clear all
%-------------------------------------------------------------------------%
%%%%%%%%%%%%%%%%%%%%%%%% Change these parameters! %%%%%%%%%%%%%%%%%%%%%%%%%
%-------------------------------------------------------------------------%
FusedL = 183.1762766;  % Parameter F in Excel - Midsection of motion!
FusedR = 202.4232494;  % Parameter G in Excel - Midsection of motion!

alpha0 = 0.076822267;  % Parameter A in Excel - Startsection of motion!
th0    = 0.055971485;  % Parameter M in Excel - Startsection of motion!
hp0    = 2178.103142;  % Parameter R in Excel - Startsection of motion!
V0     = 84.80083235;  % Parameter T in Excel - Startsection of motion!
%-------------------------------------------------------------------------%
%%%%%%%%%%%%%%%%%%%%%%%% End of changing variables %%%%%%%%%%%%%%%%%%%%%%%%
%-------------------------------------------------------------------------%
m0     = 60500/9.81;
mf     = 2423*0.45359237;
mp     = 851.5;
Fused  = FusedL + FusedR;
m      = m0 + mf + mp - Fused;

e      =  0.963751922274;        %----------------------------------------%
CD0    =  0.0242883628867;       % These parameters may still change due  %
CLa    =  5.37484226789;         % to incomplete work by Twan and Juan.   %
Cma    = -0.732594717104;        % Final values are therefore temporary   %
Cmde   = -0.934024280588;        %----------------------------------------%

S      = 30.00;
Sh     = 0.2*S;
Sh_S   = Sh/S;
lh     = 0.71*5.968;
c      = 2.0569;
lh_c   = lh/c;
b      = 15.911;
bh     = 5.791;
A      = b^2/S;
Ah     = bh^2/Sh;
Vh_V   = 1;
ih     = -2*pi/180;

rho0   = 1.2250;
lam    = -0.0065;
Temp0  = 288.15;
R      = 287.05;
g      = 9.81;

rho    = rho0*((1+(lam*hp0/Temp0)))^(-((g/(lam*R))+1));
W      = m*g;

muc    = m/(rho*S*c);
mub    = m/(rho*S*b);
KX2    = 0.019;
KZ2    = 0.042;
KXZ    = 0.002;
KY2    = 1.25*1.114;

Cmac   = 0;
CNwa   = CLa;
CNha   = 2*pi*Ah/(Ah+2);
depsda = 4/(A+2);

CL     = 2*W/(rho*V0^2*S);
CD     = CD0 + (CLa*alpha0)^2/(pi*A*e);

CX0    = W*sin(th0)/(0.5*rho*V0^2*S);
CXu    = -0.02792;
CXa    = -0.47966;
CXadot = +0.08330;
CXq    = -0.28170;
CXde   = -0.03728;

CZ0    = -W*cos(th0)/(0.5*rho*V0^2*S);
CZu    = -0.37616;
CZa    = -5.74340;
CZadot = -0.00350;
CZq    = -5.66290;
CZde   = -0.69612;

Cmu    = +0.06990;
Cmadot = +0.17800;
Cmq    = -8.79415;

CYb    = -0.7500;
CYbdot =  0     ;
CYp    = -0.0304;
CYr    = +0.8495;
CYda   = -0.0400;
CYdr   = +0.2300;

Clb    = -0.10260;
Clp    = -0.71085;
Clr    = +0.23760;
Clda   = -0.23088;
Cldr   = +0.03440;

Cnb    = +0.1348;
Cnbdot =  0     ;
Cnp    = -0.0602;
Cnr    = -0.2061;
Cnda   = -0.0120;
Cndr   = -0.0939;

C1 = [-2*muc, 0, 0, 0;
      0, CZadot-2*muc, 0, 0;
      0, 0, -1, 0;
      0, Cmadot, 0, -2*muc*KY2];

C2 = [-CXu, -CXa, -CZ0, -CXq;
      -CZu, -CZa, CX0, -(CZq+2*muc);
      0, 0, 0, -1;
      -Cmu, -Cma, 0, -Cmq];
C3 = [-CXde;-CZde;0;-Cmde];
  
Matrix_A    = inv(C1)*C2;
Matrix_B    = inv(C1)*C3;

Matrix_C    = [1, 0, 0, 0];
Matrix_D    = [0];
sys         = ss(Matrix_A,Matrix_B,Matrix_C,Matrix_D);

t           = linspace(0,200,1000);
u           = -pi/180*ones(1000);
lsim(sys,u,t)







Result      = eig(inv(C1)*C2);
Num_Lambda1 = Result(1) % 1 for Short Period - 3 for Phugoid
Num_P       = (2*pi/imag(Num_Lambda1))*(c/V0)
Num_T12     = (log(0.5)/real(Num_Lambda1))*(c/V0)
Num_omega0  = sqrt(real(Num_Lambda1)^2+imag(Num_Lambda1)^2)*(V0/c)
Num_zeta    = -real(Num_Lambda1)/sqrt(real(Num_Lambda1)^2+imag(Num_Lambda1)^2)

A = 2*muc*KY2*(2*muc-CZadot);
B = -2*muc*KY2*CZa-(2*muc+CZq)*Cmadot-(2*muc-CZadot)*Cmq;
C = CZa*Cmq-(2*muc+CZq)*Cma;

Ana_Lambda1 = (-B + sqrt(B^2-4*A*C))/(2*A)
Ana_P       = (2*pi/imag(Ana_Lambda1))*(c/V0)
Ana_T12     = (log(0.5)/real(Ana_Lambda1))*(c/V0)
Ana_omega0  = sqrt(real(Ana_Lambda1)^2+imag(Ana_Lambda1)^2)*(V0/c)
Ana_zeta    = -real(Ana_Lambda1)/sqrt(real(Ana_Lambda1)^2+imag(Ana_Lambda1)^2)

Lambda1_diff_R = abs((real(Num_Lambda1)-real(Ana_Lambda1))/real(Ana_Lambda1))*100
Lambda1_diff_I = abs((imag(Num_Lambda1)-imag(Ana_Lambda1))/imag(Ana_Lambda1))*100
P_diff       = abs((Num_P-Ana_P)/Ana_P)*100
T12_diff     = abs((Num_T12-Ana_T12)/Ana_T12)*100
omega0_diff  = abs((Num_omega0-Ana_omega0)/Ana_omega0)*100
zeta_diff    = abs((Num_zeta-Ana_zeta)/Ana_zeta)*100