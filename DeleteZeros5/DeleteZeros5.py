a = [45, 0, 28, 34, 100, 0, 900, 18, 0, 0]
i = 0
maxNumber = a[i]

for i in range(len(a)):
    if a[i] > maxNumber:
        maxIndex = i
        maxNumber = a[i]

print("Index of max number is: ")
print(maxIndex)
print("-------------------------")
print("Max number is: ")
print(maxNumber)
print("-------------------------")

firstPart = a[0 : maxIndex]
secondPart = a[maxIndex : len(a)]
newSecondPart = [j for j in secondPart if j != 0]

print("New a(n) without zeros after max number is: ")
print(firstPart + newSecondPart)
