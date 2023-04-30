def basics():
    for x in range(151):
        print(x)


def multiplesOfFive():
    for x in range(0, 1001, 5):
        print(x)


def countingDojoWay():
    for x in range(101):
        if x % 10 == 0:
            print("Coding Dojo")
        elif x % 5 == 0:
            print("Coding")
        else:
            print(x)


def suckersHuge():
    sum = 0
    for x in range(500000):
        if x % 2 != 0:
            sum = sum + x
    print(sum)


def countdownByFour():
    for x in range(2018, 0, -4):
        print(x)


def flexibleCounter(lowNum, highNum, mult):
    for x in range(lowNum, highNum + 1):
        if x % mult == 0:
            print(x)


basics()
multiplesOfFive()
countingDojoWay()
suckersHuge()
countdownByFour()
flexibleCounter(2, 9, 3)
