closefile = open('Calendar-confusion_InputForSubmission_1.txt')
infile = closefile.read().splitlines()

#infile = ["08#09#1420 mm#dd#yyyy dd\yyyy\mm"]

for i in range(len(infile)):
    line = infile[i].split()
    j = 0;
    while j<len(line[0]):
        if line[1][j] == 'y':
            year = line[0][j:j+4]
            j += 4
        elif line[1][j] == 'm':
            month = line[0][j:j+2]
            j += 2
        elif line[1][j] == 'd':
            day = line[0][j:j+2]
            j += 2
        else:
            j+= 1
    
    new_date = ''
    
    j = 0
    while j<len(line[0]):
        if line[2][j] == 'y':
            new_date += year
            j += 4
        elif line[2][j] == 'm':
            new_date += month
            j += 2
        elif line[2][j] == 'd':
            new_date += day
            j += 2
        elif line[2][j] not in ('Y', 'M', 'D'):
            new_date += line[2][j]
            j+=1
    
    print(new_date)
            
            

closefile.close()

