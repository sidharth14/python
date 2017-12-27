
def pay(hr, rt):

 try:
    hr = float(hours)
    rt = float(rate)
    if hr >40:
        rt=1.5*rt
    pay = hr*rt
    print(pay)
 except:
    print('Enter valid hours and rate')
hours = input('Enter number of hours:')
rate = input('Enter rate:')
pay(hours,rate)
