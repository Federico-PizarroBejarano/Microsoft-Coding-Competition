closefile = open('PracticeInput.txt')
infile = closefile.read()[2:-2].split('), (')

#print(infile)
for i in range(len(infile)):
    if infile[i] == 'FB, F':
        infile[i] = 'H'
    elif infile[i] == 'C, S':
        infile[i] = 'Hit'
    else:
        infile[i] = 'S'

hits = 0
runs = 0
strikes = 0
outs = 0

for i in range(len(infile)):
    if infile[i] == "H":
        runs += hits + 1
        hits = 0
        strike = 0
    elif infile[i] == 'Hit':
        hits += 1
        if hits == 4:
            runs += 1
            hits -= 1
        strikes = 0
    else:
        strikes += 1
        if strikes == 3:
            outs += 1
            strikes = 0
            if outs == 3:
                break
    
    #print(i, runs, strikes)

print(runs)



closefile.close()