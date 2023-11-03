eggNum = int(input("How many eggs do you want? "))
while eggNum % 6 != 0:
    print("The quantity must be multiple of 6.")
    eggNum = int(input("Enter again? "))
total = eggNum * 0.6
if eggNum > 54:
    total = total * 0.8
    print("You got 20% off today!")
print("Your total is £", total)