import math as m
def oswaldfactor(CD2_polyfit,A):
    e = (CD2_polyfit[1]*m.pi*A)**-1
    return e
    
    
#==========test==========
#CD2_polyfit = [1,1]
#A = 1
#print oswaldfactor(CD2_polyfit,A)