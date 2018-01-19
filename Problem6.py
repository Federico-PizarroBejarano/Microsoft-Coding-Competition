closefile = open('Moon-Box_InputForSubmission_1.txt')
infile = closefile.read().splitlines()
counts = []

for i in range(5):
    counts.append(infile.count(infile[i]))

idx = counts.index(max(counts))

print(infile[idx])
print(counts[idx])

closefile.close()