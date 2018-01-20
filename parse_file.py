finp = input('Enter the file name: ')
fopn = open(finp)
count = 0
for line in fopn:
    word = line.split()

    #print('Debug:'word)
    #if len(word)<2 or word[0] != 'From' : continue
    if len(word)>2 and word[0]=='From':
        count = count+1
        print(word[1])
print('There are ',count,' lines starting from From')
