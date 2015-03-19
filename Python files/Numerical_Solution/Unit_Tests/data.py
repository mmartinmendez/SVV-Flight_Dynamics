__author__ = 'myth'

from numpy import*

V = 1
S = 1

def change(v,s):
    global V
    V=v
    global S
    S=s

change(5,5)
print V*S
#changeV(5)
#changeS(5)
