# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.

inp = input('Enter the file name:  ')
try:
     opn = open(inp)
except:
     print(inp,'file not found')
     exit()

dic2=dict()

for line in opn:
    words = line.split()
    for word in words:
        if words[0] != 'From' or words[0]==' ':continue
        
        elif words[1] not in dic2:
            dic2[words[1]] = 1
        else:
            dic2[words[1]] = dic2[words[1]] + 1
print(dic2)

# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
maxi = 0
maxik = ''
for ele in dic2:
    if dic2[ele] > maxi:
        maxi=dic2[ele]
        maxik = ele
print(maxi,maxik)
