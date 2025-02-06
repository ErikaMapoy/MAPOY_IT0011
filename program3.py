print("-" * 45)
print("|    Pattern (a) - Using Nested For Loops   |")
print("-" * 45 + "\n")

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()

print("\n" + "-" * 45)
print("|   Pattern (b) - Using Nested While Loops  |")
print("-" * 45 + "\n")

rows = [1, 3, 5, 6, 7]
i = 0
while i < len(rows):
    num = rows[i]
    j = 0
    while j < num:
        print(num, end="")
        j += 1
    print()
    i += 1

print("\n" + "-" * 45)