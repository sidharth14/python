count = 0
total = 0
while True:
    value = input('Enter a number: ' )
    if value == 'done':
        break
    try:
        val = int(value)
    except:
        print('Enter a valid number')

    count = count +1
    total = total + val
    avg = total/count

print(total, count, avg)
