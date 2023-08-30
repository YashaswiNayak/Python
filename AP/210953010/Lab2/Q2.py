m, n = map(int, input("Enter the order of the matrix: ").split(" "))
matrix1 = {}
matrix2 = {}
print("Enter the values of the first matrix: ")
for i in range(m):
    for j in range(n):
        value = int(input(f"Enter the value at position ({i},{j}): "))
        if value != 0:
            matrix1[(i, j)] = value
print("Enter the values of the second matrix")
for i in range(m):
    for j in range(n):
        value = int(input(f"Enter the value at position ({i},{j}): "))
        if value != 0:
            matrix2[(i, j)] = value

result = {}
for key in matrix1:
    result[key] = matrix1[key] + matrix2.get(key, 0)
for key in matrix2:
    if key not in matrix1:
        result[key] = matrix2[key]

print("Result: ")
for i in range(m):
    for j in range(n):
        value = result.get((i, j), 0)
        print(value, end=" ")
    print()
