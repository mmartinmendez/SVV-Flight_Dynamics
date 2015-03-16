__author__ = 'myth'

def inputFile(filename1,filename2):
    raw_data = open(filename1, "r")
    data = (row.strip().split() for row in raw_data )
    col_data = zip(*data)

    raw_weights = open(filename2,'r')
    weights = (row.strip().split() for row in raw_weights )
    col_weights = zip(*weights)

    return col_data , col_weights

