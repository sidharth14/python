#Exercise 5: This program records the domain name (instead of the address) where the message was sent from
#instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

inp = input('Enter the file name: ')

try:
    opn = open(inp)
except:
    print('File ',opn,' not found')
    exit()
fin=0
dic3=dict()
for line in opn:
    words = line.split()
    if len(words)==0 : continue
    elif words[0] != 'From' :continue
#    delimiter = '@'
    word = words[1].split('@')
#    print(word[1])
    elif word[1] not in dic3:
        dic3[word[1]]=1
    else:
        dic3[word[1]]=dic3[word[1]]+1
print(dic3)
