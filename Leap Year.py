year = int(input("Which year do you want to check? "))


a = year % 4
b = year % 100
c = year % 400
d = 0

if (a == d):
    if (b == d):
        if (c == d):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


