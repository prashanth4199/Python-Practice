# Q1: Print Numbers from 1 to n
n = 5
for i in range(1, n + 1):
    print(i)


# Q2: Print Numbers from m to n
m = 3
n = 7
for i in range(m, n + 1):
    print(i)


# Q3: Print Numbers from n to 1
n = 5
for i in range(n, 0, -1):
    print(i)


# Q4: Print Numbers from n to m in Reverse
n = 10
m = 6
for i in range(n, m - 1, -1):
    print(i)


# Q5: Sum of n Natural Numbers
n = 5
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)


# Q6: Factorial of a Number
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)


# Q7: Sum of m to n Numbers
m = 3
n = 6
sum = 0
for i in range(m, n + 1):
    sum += i
print(sum)


# Q8: Product of m to n Numbers
m = 2
n = 4
product = 1
for i in range(m, n + 1):
    product *= i
print(product)


# Q9: Print Factors of a Number
n = 6
for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# Q10: Count of Factors
n = 6
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)


# Q11: Prime Number Check
n = 7
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")


# Q12: Even Numbers from m to n
m = 3
n = 10
for i in range(m, n + 1):
    if i % 2 == 0:
        print(i)


# Q13: Odd Numbers from m to n
m = 3
n = 10
for i in range(m, n + 1):
    if i % 2 != 0:
        print(i)


# Q14: Count Even and Odd Numbers
m = 3
n = 7
even = 0
odd = 0
for i in range(m, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", even)
print("Odd =", odd)


# Q15: Reverse a String
s = "hello"
reverse = ""
for ch in s:
    reverse = ch + reverse
print(reverse)


# Q16: Check Palindrome String
s = "madam"
reverse = ""
for ch in s:
    reverse = ch + reverse
if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q17: Sum of Digits
n = 123
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
print(sum)


# Q18: Product of Digits
n = 123
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10
print(product)


# Q19: Armstrong Number
n = 153
original = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit * digit * digit
    n = n // 10
if sum == original:
    print("Armstrong number")
else:
    print("Not Armstrong")


# Q20: Reverse a Number
n = 123
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)


# Q21: Palindrome Number
n = 121
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q22: Count Vowels
s = "apple"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)


# Q23: Count Consonants
s = "apple"
count = 0
for ch in s:
    if ch not in "aeiou":
        count += 1
print(count)


# Q24: Count Vowels and Consonants
s = "apple"
vowels = 0
consonants = 0
for ch in s:
    if ch in "aeiou":
        vowels += 1
for ch in s:
    if ch not in "aeiou":
        consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)


# Q25: Perfect Number
n = 28
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Perfect number")
else:
    print("Not Perfect")


# Q26: Neon Number
n = 9
square = n * n
sum = 0
while square > 0:
    digit = square % 10
    sum += digit
    square = square // 10
if sum == n:
    print("Neon number")
else:
    print("Not Neon")


# Q27: Strong Number
n = 145
original = n
sum = 0
while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    n = n // 10
if sum == original:
    print("Strong number")
else:
    print("Not Strong")


# Q28: Harshad Number
n = 18
original = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
if original % sum == 0:
    print("Harshad number")
else:
    print("Not Harshad")


# Q29: Fibonacci Series
n = 5
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


# Q30: Neon Number (repeated)
n = 9
square = n * n
sum = 0
while square > 0:
    digit = square % 10
    sum += digit
    square = square // 10
if sum == n:
    print("Neon number")
else:
    print("Not Neon")
