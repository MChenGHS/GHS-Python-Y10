# Ask a loop to repeat for a cycle chosen by user
count = int(input("How many times?"))
for i in range(count):
    print("You're counting once")

# Check if a number is in a particular range
if i > 80 and i < 100:
    print("Something")

# Get the total from several inputs
sum = 0
count = int(input("How many inputs?"))
for i in range(count):
    tmp = int(input("Enter a new number"))
    sum = sum + tmp
print("Total is ", sum)