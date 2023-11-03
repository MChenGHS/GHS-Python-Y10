eggNum = int(input("How many eggs do you want? "))
while eggNum % 6 != 0:
    print("The quantity must be multiple of 6.")
    eggNum = int(input("Enter again? "))

size = input("What size are they? Choose from large, medium and small. ")
size = size.lower()

unitPrice = 1
if size == "large":
    unitPrice = 0.8
elif size == "medium":
    unitPrice = 0.6
elif size == "small":
    unitPrice = 0.45
else:
    print("Not sure what you mean. We'll assume that you're buying medium eggs.")
    unitPrice = 0.6

total = eggNum * unitPrice
if eggNum > 54:
    total = total * 0.8
    print("You got 20% off today!")
print("Your total is £", total)