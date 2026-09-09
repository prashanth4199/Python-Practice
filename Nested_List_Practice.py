# Nested List — Easy Problem Solving Practice Questions

# 1. Print Every Element One by One
numbers = [[1, 2], [3, 4], [5, 6]]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j])


# 2. Print Each Inner List
numbers = [[10, 20], [30, 40], [50, 60]]
for i in range(len(numbers)):
    print(numbers[i])


# 3. Find Total Number of Elements
numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
count = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        count = count + 1
print(count)


# 4. Calculate Sum of All Elements
numbers = [[1, 2], [3, 4], [5, 6]]
total = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        total = total + numbers[i][j]
print(total)


# 5. Find the Largest Element
numbers = [[10, 5], [25, 15], [8, 30]]
largest = numbers[0][0]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] > largest:
            largest = numbers[i][j]
print(largest)


# 6. Find the Smallest Element
numbers = [[10, 5], [25, 15], [8, 30]]
smallest = numbers[0][0]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] < smallest:
            smallest = numbers[i][j]
print(smallest)


# 7. Count Even Numbers
numbers = [[1, 2, 3], [4, 5, 6], [7, 8]]
count = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] % 2 == 0:
            count = count + 1
print(count)


# 8. Count Odd Numbers
numbers = [[1, 2, 3], [4, 5, 6], [7, 8]]
count = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] % 2 != 0:
            count = count + 1
print(count)


# 9. Search for an Element
numbers = [[10, 20], [30, 40], [50, 60]]
search = 40
found = False
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] == search:
            found = True
if found:
    print("Found")
else:
    print("Not Found")


# 10. Count Occurrences
numbers = [[1, 2, 2], [3, 2, 4], [2, 5]]
search = 2
count = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] == search:
            count = count + 1
print(count)


# 11. Print First Element of Every List
numbers = [[10, 20], [30, 40], [50, 60]]
for i in range(len(numbers)):
    print(numbers[i][0])


# 12. Print Last Element of Every List
numbers = [[10, 20], [30, 40], [50, 60]]
for i in range(len(numbers)):
    print(numbers[i][-1])


# 13. Find Sum of Each Inner List
numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
for i in range(len(numbers)):
    total = 0
    for j in range(len(numbers[i])):
        total = total + numbers[i][j]
    print(total)


# 14. Find Maximum of Each Inner List
numbers = [[10, 20, 5], [30, 15], [8, 25, 12]]
for i in range(len(numbers)):
    largest = numbers[i][0]
    for j in range(len(numbers[i])):
        if numbers[i][j] > largest:
            largest = numbers[i][j]
    print(largest)


# 15. Find Minimum of Each Inner List
numbers = [[10, 20, 5], [30, 15], [8, 25, 12]]
for i in range(len(numbers)):
    smallest = numbers[i][0]
    for j in range(len(numbers[i])):
        if numbers[i][j] < smallest:
            smallest = numbers[i][j]
    print(smallest)


# 16. Print Only Positive Numbers
numbers = [[-2, 5, -8], [10, -3, 7], [-1, 4]]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] > 0:
            print(numbers[i][j])


# 17. Print Only Numbers Greater Than 10
numbers = [[5, 15, 20], [8, 25], [30, 3]]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] > 10:
            print(numbers[i][j])


# 18. Calculate Average of All Elements
numbers = [[10, 20], [30, 40]]
total = 0
count = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        total = total + numbers[i][j]
        count = count + 1
average = total / count
print(average)
