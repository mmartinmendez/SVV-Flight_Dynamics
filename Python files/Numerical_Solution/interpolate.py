__author__ = 'myth'

def interpolate(a,b,pos):
    """

    :rtype : integer
    """
    x=0
    xa=a[pos-1]
    xb=a[pos]
    ya=b[pos-1]
    yb=b[pos]
    y=((x-xa)*(yb-ya))/(xb-xa)+ya
    return y
