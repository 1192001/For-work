print("THE DIAMOND EXPERT SYSTEM")
question1 = input("floats in water? (Y/N)")
if question1 == "Y":
    print("Fake")
else: 
    question2 = input("Can scratch glass? (Y/N)")
    if question2 == "N":
        print("Fake")
    else:
        question3 = input("Does it conduct electric? (Y/N)")
        if question3 == "Y":
            print("Fake")
        else: "N"
        print("Could be real")
