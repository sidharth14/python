grade = input('Enter the score between 0 and 1 :')

def score(gr):
    try:
        gr = float(grade)
        if gr>=0.9 and gr<1:
         print ('Grade : A')
        elif gr>=0.8 and gr<=1:
         print ('Grade : B')
        elif gr>=0.7 and gr<=1:
         print ('Grade : C')
        elif gr<6:
         print('Grade : F')
        else:
            print('Invalid input')

    except:
        print('Enter valid points between 0 and 1')
score(grade)
