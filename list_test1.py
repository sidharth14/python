inp_file = input('Enter the name of file:')
Fopen = open(inp_file)
#print('Desbug: File',Fopen,'is open')
for line in Fopen:
    #print(line)
    words = line.split()
    #print(len(words))
    #print(words)
    #if len(words) == 0: continue
    if ('/n' not in words) and words[0] == 'From:':
    #if words[0] != ' ' and words[0] == 'From':
        print(words[2])
