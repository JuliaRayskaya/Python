a = [45, 0, -17, 28, -5, 0, -34, 100, 25, 0, 18]
result = 0

for i in range(len(a)):
    if a[i] == 0:
        firstZeroIndex = i
        firstZero = a[i]
        break

for j in range(firstZeroIndex + 1, len(a)):
    if a[j] == 0:
        secondZeroIndex = j
        secondZero = a[j]
        break

for k in range(firstZeroIndex+1, secondZeroIndex):
    if a[k] < 0:
        result += a[k]

print("First and second zero indexes are: ")
print(firstZeroIndex, secondZeroIndex)
print("-------------------------")
print("Sum of negative elements is: ")
print(result)