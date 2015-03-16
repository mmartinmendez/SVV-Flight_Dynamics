__author__ = 'myth'

def inputFile(filename):
    crs = open(filename, "r")
    data = (row.strip().split() for row in crs )
    col = zip(*data)
    return col

