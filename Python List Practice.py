# Q1 Find the Sum of List Elements 
list = [1,2,3,4,5]
total = 0
for i in range(len(list)):
    total = total + list[i]
print(total)

list = [10,20,30]
total = 0
for i in range(len(list)):
    total = total + list[i]
print(total)

list = [7, 3, 8, 2] 
total = 0
for i in range(len(list)):
    total = total + list[i]
print(total)


# Q2 — Find the Largest Element
list = [10, 25, 7, 42, 18] 
largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        largest = list[i]
print(largest)

list = [5, 2, 9, 1] 
largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        largest = list[i]
print(largest)

list = [100, 50, 75, 25]
largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        largest = list[i]
print(largest)


# Q3 Count Even Numbers
list = [1, 2, 3, 4, 5, 6]
count = 0
for i in range(len(list)):
    if list[i] % 2 == 0:
        count = count + 1
print(count)

list = [10, 15, 20, 25, 30]
count = 0
for i in range(len(list)):
    if list[i] % 2 == 0:
        count = count + 1
print(count)

list = [1, 3, 5, 7]
count = 0
for i in range(len(list)):
    if list[i] % 2 == 0:
        count = count + 1
print(count)


# Q4 — Count Positive Numbers
list = [-2, 5, 7, -1, 3] 
count = 0
for i in range(len(list)):
    if list[i] > 0:
        count = count + 1
print(count)

list = [10, -5, 0, 8, -2]
count = 0
for i in range(len(list)):
    if list[i] > 0:
        count = count + 1
print(count)

list = [-1, -2, -3]
count = 0
for i in range(len(list)):
    if list[i] > 0:
        count = count + 1
print(count)


# Q5 Reverse a List 
list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(list) -1, -1, -1):
    reversed_list.append(list[i])
print(reversed_list)

list = [10, 20, 30]
reversed_list = []
for i in range(len(list) - 1, -1, -1):
    reversed_list.append(list[i])
print(reversed_list)

list = [7, 8]
reversed_list = []
for i in range(len(list) - 1, -1, -1):
    reversed_list.append(list[i])
print(reversed_list)


# Q6 Find the Smallest Element
list = [8, 3, 12, 5, 1] 
smallest = list[0]
for i in range(len(list)):
    if list[i] < smallest:
        smallest = list[i]
print(smallest)

list = [20, 15, 30, 10]
smallest = list[0]
for i in range(len(list)):
    if list[i] < smallest:
        smallest = list[i]
print(smallest)

list = [-5, -2, -10, -1]
smallest = list[0]
for i in range(len(list)):
    if list[i] < smallest:
        smallest = list[i]
print(smallest)


# Q7 — Count Occurrences of an Element
list = [1, 2, 2, 3, 2, 4]
target = 2
count = 0
for i in range(len(list)):
    if list[i] == target:
        count = count + 1
print(count)

list = [5, 5, 1, 2, 5]
target = 5
count = 0
for i in range(len(list)):
    if list[i] == target:
        count = count + 1
print(count)

list = [10, 20, 30]
target = 5
count = 0
for i in range(len(list)):
    if list[i] == target:
        count = count + 1
print(count)


# Q8 Print Odd Elements 
list = [1, 2, 3, 4, 5]
odd_elements = []
for i in range(len(list)):
    if list[i] % 2 != 0:
        odd_elements.append(list[i])
print(odd_elements)

list = [10, 15, 20, 25, 30]
odd_elements = []
for i in range(len(list)):
    if list[i] % 2 != 0:
        odd_elements.append(list[i])
print(odd_elements)

list = [2, 4, 6, 8]
odd_elements = []
for i in range(len(list)):
    if list[i] % 2 != 0:
        odd_elements.append(list[i])
print(odd_elements)


# Q9 Calculate the Average 
list = [10, 20, 30, 40] 
total = 0
for i in range(len(list)):
    total = total + list[i]
    average = total / len(list)
print(average)

list = [5, 10, 15]
total = 0
for i in range(len(list)):
    total = total + list[i]
    average = total / len(list)
print(average)

list = [2, 4]
total = 0
for i in range(len(list)):
    total = total + list[i]
    average = total / len(list)
print(average)


# Q10 Check Whether an Element Exists 
list = [10, 20, 30, 40] 
target = 30
found = False
for i in range(len(list)):
    if list[i] == target:
        found = True
print(found)

list = [1, 3, 5, 7] 
target = 4
found = False
for i in range(len(list)):
    if list[i] == target:
        found = True
print(found)

list = [100, 200, 300]
target = 100
found = False
for i in range(len(list)):
    if list[i] == target:
        found = True
print(found)


# Q11 Find the Second Largest Element 
list = [10, 20, 5, 30, 25] 
largest = list[0]
second_largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        second_largest = largest
        largest = list[i]
    elif list[i] > second_largest and list[i] != largest:
        second_largest = list[i]
print(second_largest)

list = [4, 8, 2, 10, 6] 
largest = list[0]
second_largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        second_largest = largest
        largest = list[i]
    elif list[i] > second_largest and list[i] != largest:
        second_largest = list[i]
print(second_largest)

list = [15, 15, 10, 20, 5] 
largest = list[0]
second_largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        second_largest = largest
        largest = list[i]
    elif list[i] > second_largest and list[i] != largest:
        second_largest = list[i]
print(second_largest)


# Q12 Remove Duplicate Elements 
list = [1, 2, 2, 3, 1, 4]
unique_elements = []
for i in range(len(list)):
    if list[i] not in unique_elements:
        unique_elements.append(list[i])
print(unique_elements)

list = [5, 5, 5, 2, 2, 1] 
unique_elements = []
for i in range(len(list)):
    if list[i] not in unique_elements:
        unique_elements.append(list[i])
print(unique_elements)

list = [10, 20, 10, 30, 20] 
unique_elements = []
for i in range(len(list)):
    if list[i] not in unique_elements:
        unique_elements.append(list[i])
print(unique_elements)


# Q13 Move All Zeros to the End
list = [0, 1, 0, 3, 12]
result = []
zero_count = 0
for i in range(len(list)):
    if list[i] != 0:
        result.append(list[i])
    else:
        zero_count = zero_count + 1
for i in range(zero_count):
    result.append(0)
print(result)

list = [1, 0, 2, 0, 4, 5]
result = []
zero_count = 0
for i in range(len(list)):
    if list[i] != 0:
        result.append(list[i])
    else:
        zero_count = zero_count + 1
for i in range(zero_count):
    result.append(0)
print(result)

list = [0, 0, 1, 2]
result = []
zero_count = 0
for i in range(len(list)):
    if list[i] != 0:
        result.append(list[i])
    else:
        zero_count = zero_count + 1
for i in range(zero_count):
    result.append(0)
print(result)


# Q14 Find the Missing Number
list = [3, 0, 1]
n = len(list)
expected_sum = n * (n + 1) // 2
actual_sum = sum(list)
missing_number = expected_sum - actual_sum
print(missing_number)

list = [0, 1] 
n = len(list)
expected_sum = n * (n + 1) // 2 
actual_sum = sum(list)
missing_number = expected_sum - actual_sum
print(missing_number)

list = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(list)
expected_sum = n * (n + 1) // 2
actual_sum = sum(list)
missing_number = expected_sum - actual_sum
print(missing_number)


# Q15 Find Common Elements
list1 = [1, 2, 3, 4] 
list2 = [3, 4, 5, 6] 
common_elements = []
for i in range(len(list1)):
    if list1[i] in list2:
        common_elements.append(list1[i])
print(common_elements)

list1 = [10, 20, 30] 
list2 = [20, 30, 40]
common_elements = []
for i in range(len(list1)):
    if list1[i] in list2:
        common_elements.append(list1[i])
print(common_elements)

list1 = [1, 2, 3] 
list2 = [4, 5, 6] 
common_elements = []
for i in range(len(list1)):
    if list1[i] in list2:
        common_elements.append(list1[i])
print(common_elements)


# Q16 Find the Majority Element
list = [3, 2, 3]
n = len(list)
majority = None
for i in range(len(list)):
    count = 0
    for j in range(len(list)):
        if list[j] == list[i]:
            count = count + 1
    if count > n / 2:
        majority = list[i]
print(majority)

list = [2, 2, 1, 1, 1, 2, 2]
n = len(list)
majority = None
for i in range(len(list)):
    count = 0
    for j in range(len(list)):
        if list[j] == list[i]:
            count = count + 1
    if count > n / 2:
        majority = list[i]
print(majority)

list = [5, 5, 5, 2, 3, 5, 4]
n = len(list)
majority = None
for i in range(len(list)):
    count = 0
    for j in range(len(list)):
        if list[j] == list[i]:
            count = count + 1
    if count > n / 2:
        majority = list[i]
print(majority)


# Q17 Find the Pair With a Given Sum
list = [2, 7, 11, 15]
target = 9
result = []
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] + list[j] == target:
            result = [list[i], list[j]]
print(result)

list = [3, 2, 4]
target = 6
result = []
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] + list[j] == target:
            result = [list[i], list[j]]
print(result)

list = [1, 5, 8, 10]
target = 13
result = []
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] + list[j] == target:
            result = [list[i], list[j]]
print(result)


# Q18 Separate Positive and Negative Numbers
list = [-2, 5, -7, 8, 0, 3]
positive = []
negative = []
for i in range(len(list)):
    if list[i] > 0:
        positive.append(list[i])
    elif list[i] < 0:
        negative.append(list[i])
print("Positive:", positive)
print("Negative:", negative)

list = [10, -5, -2, 7, 4]
positive = []
negative = []
for i in range(len(list)):
    if list[i] > 0:
        positive.append(list[i])
    elif list[i] < 0:
        negative.append(list[i])
print("Positive:", positive)
print("Negative:", negative)

list = [-1, -2, -3, 0]
positive = []
negative = []
for i in range(len(list)):
    if list[i] > 0:
        positive.append(list[i])
    elif list[i] < 0:
        negative.append(list[i])
print("Positive:", positive)
print("Negative:", negative)


# Q19 Find the First Repeated Element 
list = [10, 5, 3, 4, 3, 5]
repeated = None
for i in range(len(list)):
    for j in range(i):
        if list[j] == list[i]:
            repeated = list[i]
            break
    if repeated is not None:
        break
print(repeated)

list = [1, 2, 3, 4, 2, 5]
repeated = None
for i in range(len(list)):
    for j in range(i):
        if list[j] == list[i]:
            repeated = list[i]
            break
    if repeated is not None:
        break
print(repeated)

list = [7, 8, 9, 7, 8]
repeated = None
for i in range(len(list)):
    for j in range(i):
        if list[j] == list[i]:
            repeated = list[i]
            break
    if repeated is not None:
        break
print(repeated)


# Q20 Rotate a List to the Right 
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
