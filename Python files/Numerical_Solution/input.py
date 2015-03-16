__author__ = 'myth'

from numpy import*

def inputFile(filename1,filename2,filename3,filename4,filename5):

    # Filename1 -- with all the aircraft parameters
    raw_data = open(filename1, "r")
    data = (row.strip().split() for row in raw_data )
    col_data = zip(*data)
    col_data1 = array(col_data)
    s1=(float)(size(col_data1))/size(col_data1[0])
    s1=(int)(floor(s1))
    col_data2 = []
    for i in range(s1):
        col_data2.append(map(float,col_data1[i][2:]))



    # Filename2 -- with the aircraft,fuel and payload weights
    raw_weights = open(filename2,'r')
    weights = (row.strip().split() for row in raw_weights)
    col_weights = zip(*weights)
    col_weights1 = array(col_weights)
    col_weights2 = map(float,col_weights1[0])


    # Filename3 -- with the data for the shift in center of gravity
    raw_shift = open(filename3,'r')
    shift = (row.strip().split() for row in raw_shift)
    col_shift = zip(*shift)
    col_shift1 = array(col_shift)
    s = len(col_shift1)
    col_shift2 = []
    col_shift2.append(col_shift1[1][3:])
    for i in range(2,s):
        col_shift2.append(map(float,col_shift1[i][3:]))


    # Filename4 -- data for calculation of CL-CD
    raw_polar = open(filename4,'r')
    polar = (row.strip().split() for row in raw_polar)
    col_polar = zip(*polar)
    print col_polar
    col_polar1 = array(col_polar)
    print col_polar1

    # Filename5 -- elevator trim values
    raw_trim = open(filename5,'r')
    trim = (row.strip().split() for row in raw_trim)
    col_trim = zip(*trim)
    print col_trim

    return col_data2 , col_weights2, col_shift2, col_polar1

