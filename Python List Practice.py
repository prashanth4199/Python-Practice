
# ============================================================
# EASY LEVEL
# ============================================================

# Q1 Find the Sum of List Elements
# Given a list of integers, find and print the sum of all elements in the list.

lst = [1, 2, 3, 4, 5]
total = 0
for i in range(len(lst)):
    total = total + lst[i]
print(total)

lst = [10, 20, 30]
total = 0
for i in range(len(lst)):
    total = total + lst[i]
print(total)

lst = [7, 3, 8, 2]
total = 0
for i in range(len(lst)):
    total = total + lst[i]
print(total)


# Q2 Find the Largest Element
# Given a list of integers, find and print the largest element.

lst = [10, 25, 7, 42, 18]
largest = lst[0]
for i in range(len(lst)):
    if lst[i] > largest:
        largest = lst[i]
print(largest)

lst = [5, 2, 9, 1]
largest = lst[0]
for i in range(len(lst)):
    if lst[i] > largest:
        largest = lst[i]
print(largest)

lst = [100, 50, 75, 25]
largest = lst[0]
for i in range(len(lst)):
    if lst[i] > largest:
        largest = lst[i]
print(largest)


# Q3 Count Even Numbers
# Given a list of integers, count the number of even elements.

lst = [1, 2, 3, 4, 5, 6]
count = 0
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        count = count + 1
print(count)

lst = [10, 15, 20, 25, 30]
count = 0
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        count = count + 1
print(count)

lst = [1, 3, 5, 7]
count = 0
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        count = count + 1
print(count)


# Q4 Count Positive Numbers
# Given a list of integers, count how many elements are greater than zero.

lst = [-2, 5, 7, -1, 3]
count = 0
for i in range(len(lst)):
    if lst[i] > 0:
        count = count + 1
print(count)

lst = [10, -5, 0, 8, -2]
count = 0
for i in range(len(lst)):
    if lst[i] > 0:
        count = count + 1
print(count)

lst = [-1, -2, -3]
count = 0
for i in range(len(lst)):
    if lst[i] > 0:
        count = count + 1
print(count)


# Q5 Reverse a List
# Given a list of integers, print the elements in reverse order.

lst = [1, 2, 3, 4, 5]
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
print(reversed_lst)

lst = [10, 20, 30]
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
print(reversed_lst)

lst = [7, 8]
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
print(reversed_lst)


# Q6 Find the Smallest Element
# Given a list of integers, find and print the smallest element.

lst = [8, 3, 12, 5, 1]
smallest = lst[0]
for i in range(len(lst)):
    if lst[i] < smallest:
        smallest = lst[i]
print(smallest)

lst = [20, 15, 30, 10]
smallest = lst[0]
for i in range(len(lst)):
    if lst[i] < smallest:
        smallest = lst[i]
print(smallest)

lst = [-5, -2, -10, -1]
smallest = lst[0]
for i in range(len(lst)):
    if lst[i] < smallest:
        smallest = lst[i]
print(smallest)


# Q7 Count Occurrences of an Element
# Given a list of integers and a target value, count how many times
# the target occurs in the list.

lst = [1, 2, 2, 3, 2, 4]
target = 2
count = 0
for i in range(len(lst)):
    if lst[i] == target:
        count = count + 1
print(count)

lst = [5, 5, 1, 2, 5]
target = 5
count = 0
for i in range(len(lst)):
    if lst[i] == target:
        count = count + 1
print(count)

lst = [10, 20, 30]
target = 5
count = 0
for i in range(len(lst)):
    if lst[i] == target:
        count = count + 1
print(count)


# Q8 Print Odd Elements
# Given a list of integers, print the odd elements.

lst = [1, 2, 3, 4, 5]
odd_elements = []
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        odd_elements.append(lst[i])
print(odd_elements)

lst = [10, 15, 20, 25, 30]
odd_elements = []
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        odd_elements.append(lst[i])
print(odd_elements)

lst = [2, 4, 6, 8]
odd_elements = []
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        odd_elements.append(lst[i])
print(odd_elements)


# Q9 Calculate the Average
# Given a list of integers, calculate and print the average.

lst = [10, 20, 30, 40]
total = 0
for i in range(len(lst)):
    total = total + lst[i]
average = total / len(lst)
print(average)

lst = [5, 10, 15]
total = 0
for i in range(len(lst)):
    total = total + lst[i]
average = total / len(lst)
print(average)

lst = [2, 4]
total = 0
for i in range(len(lst)):
    total = total + lst[i]
average = total / len(lst)
print(average)


# Q10 Check Whether an Element Exists
# Given a list and a target value, check whether the target exists.

lst = [10, 20, 30, 40]
target = 30
found = False
for i in range(len(lst)):
    if lst[i] == target:
        found = True
print(found)

lst = [1, 3, 5, 7]
target = 4
found = False
for i in range(len(lst)):
    if lst[i] == target:
        found = True
print(found)

lst = [100, 200, 300]
target = 100
found = False
for i in range(len(lst)):
    if lst[i] == target:
        found = True
print(found)


# ============================================================
# MEDIUM LEVEL
# ============================================================

# Q11 Find the Second Largest Element
# Given a list of integers, find and print the second largest element.

lst = [10, 20, 5, 30, 25]
largest = lst[0]
second_largest = lst[0]
for i in range(len(lst)):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] > second_largest and lst[i] != largest:
        second_largest = lst[i]
print(second_largest)

lst = [4, 8, 2, 10, 6]
largest = lst[0]
second_largest = lst[0]
for i in range(len(lst)):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] > second_largest and lst[i] != largest:
        second_largest = lst[i]
print(second_largest)

lst = [15, 15, 10, 20, 5]
largest = lst[0]
second_largest = lst[0]
for i in range(len(lst)):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] > second_largest and lst[i] != largest:
        second_largest = lst[i]
print(second_largest)


# Q12 Remove Duplicate Elements
# Given a list of integers, remove duplicate elements while preserving order.

lst = [1, 2, 2, 3, 1, 4]
unique_elements = []
for i in range(len(lst)):
    if lst[i] not in unique_elements:
        unique_elements.append(lst[i])
print(unique_elements)

lst = [5, 5, 5, 2, 2, 1]
unique_elements = []
for i in range(len(lst)):
    if lst[i] not in unique_elements:
        unique_elements.append(lst[i])
print(unique_elements)

lst = [10, 20, 10, 30, 20]
unique_elements = []
for i in range(len(lst)):
    if lst[i] not in unique_elements:
        unique_elements.append(lst[i])
print(unique_elements)


# Q13 Move All Zeros to the End
# Given a list, move all zeros to the end while preserving other elements.

lst = [0, 1, 0, 3, 12]
result = []
zero_count = 0
for i in range(len(lst)):
    if lst[i] != 0:
        result.append(lst[i])
    else:
        zero_count = zero_count + 1
for i in range(zero_count):
    result.append(0)
print(result)

lst = [1, 0, 2, 0, 4, 5]
result = []
zero_count = 0
for i in range(len(lst)):
    if lst[i] != 0:
        result.append(lst[i])
    else:
        zero_count = zero_count + 1
for i in range(zero_count):
    result.append(0)
print(result)

lst = [0, 0, 1, 2]
result = []
zero_count = 0
for i in range(len(lst)):
    if lst[i] != 0:
        result.append(lst[i])
    else:
        zero_count = zero_count + 1
for i in range(zero_count):
    result.append(0)
print(result)


# Q14 Find the Missing Number
# Given numbers from 0 to n with one number missing, find the missing number.

lst = [3, 0, 1]
n = len(lst)
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing_number = expected_sum - actual_sum
print(missing_number)

lst = [0, 1]
n = len(lst)
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing_number = expected_sum - actual_sum
print(missing_number)

lst = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(lst)
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing_number = expected_sum - actual_sum
print(missing_number)


# Q15 Find Common Elements
# Given two lists, find and print their common elements.

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
common_elements = []
for i in range(len(lst1)):
    if lst1[i] in lst2:
        common_elements.append(lst1[i])
print(common_elements)

lst1 = [10, 20, 30]
lst2 = [20, 30, 40]
common_elements = []
for i in range(len(lst1)):
    if lst1[i] in lst2:
        common_elements.append(lst1[i])
print(common_elements)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
common_elements = []
for i in range(len(lst1)):
    if lst1[i] in lst2:
        common_elements.append(lst1[i])
print(common_elements)


# ============================================================
# HARD LEVEL
# ============================================================

# Q16 Find the Majority Element
# Given a list, find the element that appears more than n/2 times.

lst = [3, 2, 3]
n = len(lst)
majority = None
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[j] == lst[i]:
            count = count + 1
    if count > n / 2:
        majority = lst[i]
print(majority)

lst = [2, 2, 1, 1, 1, 2, 2]
n = len(lst)
majority = None
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[j] == lst[i]:
            count = count + 1
    if count > n / 2:
        majority = lst[i]
print(majority)

lst = [5, 5, 5, 2, 3, 5, 4]
n = len(lst)
majority = None
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[j] == lst[i]:
            count = count + 1
    if count > n / 2:
        majority = lst[i]
print(majority)


# Q17 Find the Pair With a Given Sum
# Given a list and target sum, find a pair whose sum equals the target.

lst = [2, 7, 11, 15]
target = 9
result = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            result = [lst[i], lst[j]]
print(result)

lst = [3, 2, 4]
target = 6
result = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            result = [lst[i], lst[j]]
print(result)

lst = [1, 5, 8, 10]
target = 13
result = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            result = [lst[i], lst[j]]
print(result)


# Q18 Separate Positive and Negative Numbers
# Given a list, separate positive and negative numbers into two lists.

lst = [-2, 5, -7, 8, 0, 3]
positive = []
negative = []
for i in range(len(lst)):
    if lst[i] > 0:
        positive.append(lst[i])
    elif lst[i] < 0:
        negative.append(lst[i])
print("Positive:", positive)
print("Negative:", negative)

lst = [10, -5, -2, 7, 4]
positive = []
negative = []
for i in range(len(lst)):
    if lst[i] > 0:
        positive.append(lst[i])
    elif lst[i] < 0:
        negative.append(lst[i])
print("Positive:", positive)
print("Negative:", negative)

lst = [-1, -2, -3, 0]
positive = []
negative = []
for i in range(len(lst)):
    if lst[i] > 0:
        positive.append(lst[i])
    elif lst[i] < 0:
        negative.append(lst[i])
print("Positive:", positive)
print("Negative:", negative)


# Q19 Find the First Repeated Element
# Given a list, find the first element that repeats.

lst = [10, 5, 3, 4, 3, 5]
repeated = None
for i in range(len(lst)):
    for j in range(i):
        if lst[j] == lst[i]:
            repeated = lst[i]
            break
    if repeated is not None:
        break
print(repeated)

lst = [1, 2, 3, 4, 2, 5]
repeated = None
for i in range(len(lst)):
    for j in range(i):
        if lst[j] == lst[i]:
            repeated = lst[i]
            break
    if repeated is not None:
        break
print(repeated)

lst = [7, 8, 9, 7, 8]
repeated = None
for i in range(len(lst)):
    for j in range(i):
        if lst[j] == lst[i]:
            repeated = lst[i]
            break
    if repeated is not None:
        break
print(repeated)


# Q20 Rotate a List to the Right
# Given a list and k, rotate the list to the right by k positions.

lst = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(lst)
result = []
for i in range(n - k, n):
    result.append(lst[i])
for i in range(0, n - k):
    result.append(lst[i])
print(result)

lst = [1, 2, 3, 4]
k = 2
n = len(lst)
result = []
for i in range(n - k, n):
    result.append(lst[i])
for i in range(0, n - k):
    result.append(lst[i])
print(result)

lst = [10, 20, 30, 40, 50]
k = 1
n = len(lst)
result = []
for i in range(n - k, n):
    result.append(lst[i])
for i in range(0, n - k):
    result.append(lst[i])
print(result)
