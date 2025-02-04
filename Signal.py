

def buy(value):
    if value>60:
        print("Bullish moment")
    elif value==60:
        print(" Waiting moment")
    else:
        print(" Bearish moment")
    return

n = int(input(" Can you enter the index "))
buy(n)

