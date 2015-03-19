import subprocess

def T_p(h_p,M,T,FFL,FFR,T_0):
    thrust = open('thrusst.txt','w')
    for i in [10000,11000,12100,13100,14200,15800,18500,21650,22200,23400,24200,24850,25600,26600,28100]:
        thrust.write(str(h_p[i])+'\t'+str(M)+'\t'+str(abs(T-T_0))+'\t'+str(FFL)+'\t'+str(FFR)+'\n')
        thrust.write(str(h_p)+'\t'+str(M)+'\t'+str(abs(T-T_0))+'\t'+str(0.048)+'\t'+str(0.048)+'\n')
    thrust.close()
    
    process = subprocess.Popen(['thrust.exe','thrusst.txt'], bufsize = -1 ,stderr = subprocess.PIPE, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
    process.wait()
    thrust = open('thrust.dat','r')
    
    Tlist = []
    Tlists = []
    thrustd = thrust.readlines()
    i = 0
    for line in thrustd:
        line = line.strip('\n').split('\t')
        if i%2 == 0:
            Tlist.append(float(line[0])+float(line[1]))
        else:
            Tlists.append(float(line[0])+float(line[1]))
        i+=1
    thrust.close()
    os.remove('thrusst.txt')
    os.remove('thrust.dat')