num = list()
maxi=0
mini=0
while True:

    n = input('Enter number in the list and enter done to end the list: ')
    if n == 'done':
        break
    try:
        x = float(n)
    except:
        print('Enter a valid number thanks!')
        break
#    if x>maxi:
#        maxi = x
#    if x<mini:
#        mini = x
    num.append(x)
print(max(num))
print(min(num))
#print(maxi,mini)
