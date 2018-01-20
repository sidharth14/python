fname = input('Enter the name of the file: ')
try:
    finput = open(fname)
except:
    print('File not found:',fname)
    exit()
count=0
for l in finput:
    if l.startswith('X-DSPAM-Confidence:')
    count  = count +1
    print(l)
