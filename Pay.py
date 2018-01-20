
def computepay(hours,rate):

    try:
        hours=input('Enter number of hours: ')
        rate=input('Enter rate: ')
        if float(hours) > 40:
            extra = hours-40
            pay = 1.5*rate*extra
            print(40 * rate + pay)
        else:
            print(hours * rate)
    except:
        print("Enter a valid number")
computepay(20,12)
