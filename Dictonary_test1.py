#Write a program that reads the words in words.txt and stores them as keys in a dictionary.
#It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

inp = input('Enter a name of the file: ')
opn = open('words.txt')

net = dict()

for line in opn:
    words = line.split()
    for word in words:
        if word not in net:
            net[word] = 1
        else:
            net[word]=net[word]+1
print(net)
