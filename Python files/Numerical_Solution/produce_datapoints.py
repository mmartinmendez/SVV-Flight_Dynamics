__author__ = 'myth'

from numpy import*

def points(value,m):
    Time = zeros(len(value))
    Input1 = zeros(len(value))
    Input2 = zeros(len(value))
    for i in range(len(value)):
        Time[i] = value[i][23]

    for j in range(len(value)):
        Input1[j] = value[j][9]

    for j in range(len(value)):
        Input2[j] = value[j][m]

    return Time,Input1,Input2