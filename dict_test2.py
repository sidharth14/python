# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).

inp = input('Enter the file name: ')

try:
    opn = open(inp)
except:
    print(inp,'File not found')
    exit()

dic = dict()
for line in opn:
    words = line.split()
    for word in words:
        if words[0] != 'From' or words[0] == ' ':continue
        elif words[2] not in dic:
            dic[words[2]] = 1
        else:
            dic[words[2]] = dic[words[2]] +1

print(dic)
