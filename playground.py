for i in range(1000):
    #initialValue = int(input("Enter a value"))
    nextValue = i % 13
    anotherValue = nextValue % 7
    if nextValue*anotherValue not in newList:
        newList.append(nextValue*anotherValue)
    print(nextValue*anotherValue)

print(newList)

initialValue = int(input("Enter a value"))
nextValue = i % 13
anotherValue = nextValue % 7
print(nextValue*anotherValue)