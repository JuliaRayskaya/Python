a = [45, 17, 28, 0, 0, 4, 900, 18, -500]
sumNumbers = 0
lengthNew = 0

for i in range(len(a)):
    if a[i] == 0:
        zeroIndex = i

print("Index of last zero in row is:")
print(zeroIndex)
print("-------------------------")

for j in range(zeroIndex + 1, len(a)):
    if a[j] > 0:
        sumNumbers += a[j]
        lengthNew += 1

print("Sum of positive elements after last 0 is:")
print(sumNumbers)
print("-------------------------")
print("Number of positive elements after last 0 is:")
print(lengthNew)
print("-------------------------")
print("Result is:")
print(sumNumbers/lengthNew)






