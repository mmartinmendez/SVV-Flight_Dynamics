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



    # Filename2 -- with the aircraft,fuel and payload weights
    results_W = []
    new_results_W = []
    with open(filename2,'r') as inputfile:
        for line in inputfile:
            results_W.append(line.strip().split())
    for i in range(len(results_W)):
        new_results_W.append(list(convert(results_W[i])))
    new_results_W = array(zip(*new_results_W))


    # Filename3 -- with the data for the shift in center of gravity -- first stationary measurement series
    results_shift = []
    new_results_shift = []
    with open(filename3,'r') as inputfile:
        for line in inputfile:
            results_shift.append(line.strip().split())
    for i in range(len(results_shift)):
        new_results_shift.append(list(convert(results_shift[i])))


    # Filename4 -- data for calculation of CL-CD -- first stationary measurement series
    results_CL = []
    new_results_CL = []
    with open(filename4,'r') as inputfile:
        for line in inputfile:
            results_CL.append(line.strip().split())
    for i in range(len(results_CL)):
        new_results_CL.append(list(convert(results_CL[i])))

    # Filename5 -- elevator trim values -- second stationary measurement series
    results_det = []
    new_results_det = []
    with open(filename5,'r') as inputfile:
        for line in inputfile:
            results_det.append(line.strip().split())
    for i in range(len(results_det)):
        new_results_det.append(list(convert(results_det[i])))

    return new_results_data , new_results_W[0], new_results_shift, new_results_CL, new_results_det

def convert( someList ):
    for item in someList:
        try:
            yield float(item)
        except ValueError:
            yield item

