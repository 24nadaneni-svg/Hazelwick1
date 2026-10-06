temperature = int(input("Enter your temperature in celsius"))

if temperature<0:
    print("Freezing")
elif temperature<=20:
    print("cold")
elif temperature<=30:
    print("Warm")
elif temperature>30:
    print("Hot")