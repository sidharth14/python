def computegrade():
    try:
        score = input ("Enter the score: ")
        sc = float(score)
    except:
        print('Enter valid numeric value')
        quit()
    if (sc < 0.6):
        print('Grade: F')
    elif (sc < 0.7):
        print('Grade: D')
    elif (sc < 0.8):
        print('Grade: C')
    elif (sc < 0.9):
        print('Grade: B')
    elif (sc <= 1.0):
        print('Grade: A')
    else:
        print('Bad score')

computegrade()
