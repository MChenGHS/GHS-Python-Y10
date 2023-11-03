counter = 0
total = 0
newInput = input("Enter a new household income. Enter 'STOP' to leave program. ")
while newInput!= "STOP":
    total = total + int(newInput)
    counter = counter + 1
    newInput = input("Enter a new household income. Enter 'STOP' to leave program. ")
print("The total is ", total)
print("The average is ", total/counter)