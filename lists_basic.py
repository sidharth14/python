def chop(t):
    del t[0]
    del t[-1]

def middle(m):
    return m[1:-1]

val = list()
while True:
    inp_t = input ('Enter numbers for list and 0 to end the list:')
    try:
        num = float(inp_t)
    except:
        print('Enter a valid number')
        exit()

    if num == 0:break

    val.append(num)
print(val)
fin = middle(val)
print(fin)
chop(val)
print(val)

#print(val)
