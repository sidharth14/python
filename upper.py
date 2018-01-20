inpfile = open('mbox-short.txt')

for line in inpfile:
    wospace = line.rstrip()
    print(wospace.upper())
