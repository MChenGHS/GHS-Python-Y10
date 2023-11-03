import statistics

income = []
newInput = input("Enter a new household income. Enter 'STOP' to leave program. ")
while newInput!= "STOP":
    income.append(int(newInput))
    newInput = input("Enter a new household income. Enter 'STOP' to leave program. ")
print("The total is ", sum(income))
print("The average is ", statistics.mean(income))
print("The median is ", statistics.median(income))
print("The min is ", min(income))
print("The max is ", max(income))