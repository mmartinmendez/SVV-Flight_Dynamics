__author__ = 'myth'

from numpy import*

def inputFile(filename1,filename2):
    raw_data = open(filename1, "r")
    data = (row.strip().split() for row in raw_data )
    col_data = zip(*data)
    col_data1 = array(col_data)

    raw_weights = open(filename2,'r')
    weights = (row.strip().split() for row in raw_weights )
    col_weights = zip(*weights)
    col_weights1 = array(col_weights)
    col_weights1 = col_weights1[0]
    print col_weights1


    return col_data1 , col_weights1

