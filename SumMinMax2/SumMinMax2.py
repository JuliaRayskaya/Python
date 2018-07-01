a = [45, 17, 28, 34, 100, 25, 900, 18]
i = 0
minNumber = a[i]
maxNumber = a[i]

for i in range(len(a)):
    if a[i] < minNumber:
        minIndex = i
        minNumber = a[i]
    if a[i] > maxNumber:
        maxIndex = i
        maxNumber = a[i]
print("Indexes of min and max numbers are: ")
print(minIndex,maxIndex)
print("-------------------------")
print("Min and max numbers are: ")
print(minNumber, maxNumber)
print("-------------------------")
result = sum(a[minIndex+1:maxIndex])
print("Sum between min and max is: ")
print(result)