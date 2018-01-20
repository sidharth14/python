finp = input('enter the name of file: ')
fopn = open(finp)
final = set()
i=0
for line in fopn:
    word = line.split()
    for x in word:
        final.add(x)
    #print('Debug:',word,'this is the list')

    #for word[i] == len(word):
    #    if word[i]
#print(sorted(final))
n = list(final)
print(n)
