def convert(n,base):
   convstr = "0123456789ABCDEF"
   if n < base:
      return convstr[n]
   else:
      return convert(n//base,base) + convstr[n%base]

closefile = open('Harmony-of-Ones_InputForSubmission_1.txt')
infile = closefile.read().splitlines()

#infile = ["3", "31,65", "7,3", "7,7"]

i = 0
while i < len(infile):
    if ',' not in infile[i]:
        i += 1
    else:
        a, b = infile[i].split(',')
        a = int(a)
        b = int(b)
        A=convert(a,2)[::-1];
        B=convert(b, 2)[::-1]
    
        count = 0
        
        for j in range(min(len(A), len(B))):
            if A[j] == B[j] == '1':
                count += 1
            
        print(count)
        i += 1
closefile.close()
