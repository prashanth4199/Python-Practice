# 1. Solid Square Pattern
n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# 2. Solid Rectangle Pattern
m = 3
n = 5
for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()


# 3. Right-Angled Triangle (Left-Aligned)
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 4. Right-Angled Triangle (Right-Aligned)
n = 5
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# 5. Inverted Triangle (Left-Aligned)
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 6. Inverted Triangle (Right-Aligned)
n = 5
for i in range(n, 0, -1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# 7. Centered Pyramid Pattern
n = 4
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


# 8. Diamond Pattern
n = 3
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


# 9. Butterfly Pattern
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# 10. Left-Aligned Half Diamond
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 11. Right-Aligned Half Diamond
n = 4
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# 12. Sandglass Pattern
n = 4
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(2, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 13. Increasing Width Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 14. Decreasing Width Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 15. Right-Aligned Hill Pattern
n = 4
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# 16. Hollow Square Pattern
n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 17. Hollow Rectangle Pattern
m = 4
n = 5
for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 18. Hollow Right-Angled Triangle (Left-Aligned)
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 19. Hollow Right-Angled Triangle (Right-Aligned)
n = 5
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 20. Hollow Inverted Triangle (Left-Aligned)
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 21. Hollow Inverted Triangle (Right-Aligned)
n = 5
for i in range(n, 0, -1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 22. Hollow Pyramid Pattern
n = 4
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 23. Hollow Diamond Pattern
n = 3
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 24. Hollow Butterfly Pattern
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 25. Hollow Hourglass Pattern
n = 5
for i in range(n, 0, -1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(2, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 26. Increasing Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 27. Repeating Row Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


# 28. Continuous Number Triangle
n = 4
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# 29. Reverse Row Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# 30. Inverted Number Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# 31. Right-Aligned Number Triangle
n = 5
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 32. Pyramid Number Pattern
n = 4
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


# 33. Even Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()


# 34. Odd Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()


# 35. Pascal's Triangle
n = 5
for i in range(n):
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
