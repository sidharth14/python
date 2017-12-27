max = 0
min =0
while True:
    num = input('ENter a Number: ')
    if num == 'done':
        break
    try:
        val = int(num)
    except:
        print('Enter a valid number')
    if val > max:
        max = val
    if val < min:
        min = val
print (min, max)
