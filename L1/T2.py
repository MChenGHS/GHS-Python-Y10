eggNum = int(input("How many eggs do you want? "))
while eggNum < 6:
    print("The minimum order quantity is 6.")
    eggNum = int(input("Enter again? "))
total = eggNum * 0.6
print("Your total is £", total)