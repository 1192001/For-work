import random
valid = []
for i  in range(10):
    number = random.randint(1,99)
    character = chr(number)
    print(character)
    answer = input("Is this a valid character?(Y/N) ")
    if answer == "Y":
        valid.append(character)
print(valid)
FILENAME = 'character.txt'
with open (FILENAME, 'a') as myfile:
    for item in valid:
        myfile.write(item)