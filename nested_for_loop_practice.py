
# Q1: Print 1 2 3 in 3 rows
for i in range(3):
    for j in range(1, 4):
        print(j, end=" ")
    print()
print()


# Q2: Print * * * in 3 rows
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
print()


# Q3: Print numbers 1 to 5 in 3 rows
for i in range(3):
    for j in range(1, 6):
        print(j, end=" ")
    print()
print()


# Q4: Print row number repeated 3 times
for i in range(1, 4):
    for j in range(3):
        print(i, end=" ")
    print()
print()


# Q5: Print 1 2 in 4 rows
for i in range(4):
    for j in range(1, 3):
        print(j, end=" ")
    print()
print()


# Q6: Print 4x4 square of *
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
print()


# Q7: Multiplication tables 1 to 3, each up to 5
for i in range(1, 4):
    print(f"Table of {i}:")
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()


# Q8: Print 1 to 9 in 3x3 grid
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
print()


# Q9: Print letter repeated 3 times, row by row (A, B, C)
for letter in ["A", "B", "C"]:
    for j in range(3):
        print(letter, end=" ")
    print()
print()


# Q10: Print A B C in 3 rows
for i in range(3):
    for letter in ["A", "B", "C"]:
        print(letter, end=" ")
    print()
print()


# Q11: Print numbers 1 to 4, each number filling its own row 4 times
for i in range(1, 5):
    for j in range(4):
        print(i, end=" ")
    print()
print()


# Q12: Print * * in 5 rows
for i in range(5):
    for j in range(2):
        print("*", end=" ")
    print()
print()


# Q13: Print 5x5 grid, each row = numbers 1 to 5
for i in range(5):
    for j in range(1, 6):
        print(j, end=" ")
    print()
print()


# Q14: Print increasing count pattern (1 / 2 2 / 3 3 3)
for i in range(1, 4):
    for j in range(i):
        print(i, end=" ")
    print()
print()


# Q15: Print increasing * pattern
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
print()


# Q16: Print increasing 1..i pattern
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# Q17: Print increasing A..letter pattern
for i in range(1, 4):
    for j in range(i):
        print(chr(ord('A') + j), end=" ")
    print()
print()


# Q18: Print decreasing 1..4 pattern
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# Q19: Print decreasing * pattern
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()


# Q20: Print continuing count pattern (1 / 2 3 / 4 5 6)
num = 1
for i in range(1, 4):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
print()


# Q21: Print 3x3 multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
print()


# Q22: Print shifting number ranges (1234 / 2345 / 3456)
for i in range(1, 4):
    for j in range(i, i + 4):
        print(j, end=" ")
    print()
print()


# Q23: Print 5 to 1 repeated 4 times each row
for i in range(5, 0, -1):
    for j in range(4):
        print(i, end=" ")
    print()
print()


# Q24: Print letter pairs A B / C D / E F
letters = ["A", "B", "C", "D", "E", "F"]
index = 0
for i in range(3):
    for j in range(2):
        print(letters[index], end=" ")
        index += 1
    print()
print()


# Q25: Print rectangle of * with 3 rows and 5 columns
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()
print()
