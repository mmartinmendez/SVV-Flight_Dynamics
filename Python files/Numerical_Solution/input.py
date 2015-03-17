__author__ = 'myth'

from numpy import*

def inputFile(filename1,filename2,filename3,filename4,filename5):

    # Filename1 -- with all the aircraft parameters -- Dynamic measurements
    results_data = []
    new_results_data = []
    with open(filename1,'r') as inputfile:
        for line in inputfile:
            results_data.append(line.strip().split())
    for i in range(len(results_data)):
        new_results_data.append(list(convert(results_data[i])))

    #results_data = loadtxt(filename1,skiprows=2,usecols=None)
    results_W = loadtxt(filename2)
    results_shift = loadtxt(filename3,skiprows=2,usecols=(0,2,3,4,5,6,7,8,9,10,11))
    results_CL = loadtxt(filename4,skiprows=3,usecols=(0,2,3,4,5,6,7,8,9))
    results_det = loadtxt(filename5,skiprows=3,usecols=(0,2,3,4,5,6,7,8,9,10,11))
    return new_results_data , results_W, results_shift, results_CL, results_det

def convert( someList ):
    for item in someList:
        try:
            yield float(item)
        except ValueError:
            yield item

