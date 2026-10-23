hours = -1
total = 0

while hours>0:
    hours = int(input("Enter your number of hours"))
    choice = input("Is your car electric")
    if choice == "electric":
        total = hours*2
    else:
        total = hours*4
