__author__ = 'myth'


from Cit_par import*


def points1(value):
    start = 29987
    r = 413
    Time = zeros(r)
    Input1 = zeros(r)
    Input2 = zeros(r)
    Input3 = zeros(r)
    Input4 = zeros(r)
    Input5 = zeros(r)

    for i in range(r):
        Time[i] = value[start+i][23]

    start = 29987
    for j in range(r):
        Input1[j] = value[start][19]
        start+=1

    start = 29987
    for j in range(r):
        Input2[j] = value[start][0]
        start+=1

    start = 29987
    for j in range(r):
        Input3[j] = value[start][12]
        start+=1

    start = 29987
    for j in range(r):
        Input4[j] = value[start][14]
        start+=1

    start = 29987
    for j in range(r):
        Input5[j] = value[start][9]
        start+=1

    return Time,Input1,Input2,Input3,Input4,Input5

def points2(y):
    r = len(y)
    y1 = zeros(r)
    y2 = zeros(r)
    y3 = zeros(r)
    y4 = zeros(r)

    for i in range(r):
        y1[i] = y[i][0]

    for i in range(r):
        y2[i] = y[i][1]

    for i in range(r):
        y3[i] = y[i][2]

    for i in range(r):
        y4[i] = y[i][3]

    return y1,y2,y3,y4

