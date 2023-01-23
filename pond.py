print("FIsh Pond Model")
print("===============")
width = float(input("Enter pond width (meters):  "))
length = float(input("Enter pond length (meters):  "))
depth = float(input("Enter pond depth (meters):  "))
print("\n")
print("Results")
print("-------")
area = width * length
print(area, "square meters")

volume = area * depth
print(volume, "cubic meters of water")

fish = int(volume * 2)
print('Number of fish: ', fish)
