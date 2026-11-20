C=8
while C>=8:
    height = float(input("Enter your height in centimetres"))

    if height<140 and height>=120:
        answer = input("Are you riding with an adult")
        if answer == "yes":
            print("You are allowed to ride")
            C = C+1
        else:
            print("Cannot ride")
    elif h >=140:
        print("You can ride")
        C = C+1
    else:
        print("You can't ride")
  



