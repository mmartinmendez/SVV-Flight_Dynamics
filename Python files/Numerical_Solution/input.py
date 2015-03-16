__author__ = 'myth'

from numpy import*

def inputFile(filename1,filename2):
    raw_data = open(filename1, "r")
    data = (row.strip().split() for row in raw_data )
    col_data = zip(*data)
    col_data1 = array(col_data)
    s1=(float)(size(col_data1))/size(col_data1[0])
    s1=(int)(floor(s1))
    col_data2 = []
    for i in range(s1):
        col_data2.append(map(float,col_data1[i][2:]))


    raw_weights = open(filename2,'r')
    weights = (row.strip().split() for row in raw_weights)
    col_weights = zip(*weights)
    col_weights1 = array(col_weights)
    col_weights2 = map(float,col_weights1[0])


    return col_data2 , col_weights2

