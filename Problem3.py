import numpy as np

closefile = open('Matrix-Symmetry_InputForSubmission_1.txt')
infile = closefile.read().splitlines()

for i in range(len(infile)):
    a = infile[i]
    b = a.split(";")
    #print(b)
    no_rows = len(b)
    c = []
    
    for i in range(len(b)):
        c.append(b[i].split(","))
    #print(c)
    
    new = np.array(c)
    trans = new.transpose()
    #print(trans)
    
    res = np.array_equal(new, trans)
    
    if res==1: 
        print("Symmetric")
    else:
        print("Not symmetric")

closefile.close()