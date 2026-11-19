# 1. Ввод и создание матрицы
R = int(input("Строк: "))
C = int(input("Столбцов: "))

matrix = []
num = 1
for i in range(R):
    row = []
    for j in range(C):
        row.append(num)
        num += 1
    matrix.append(row)

print("\nМатрица:")
for row in matrix:
    print(row)

# 2. Сумма и произведение строк/столбцов
print("\nСуммы и произведения:")
for i in range(R):
    s, p = 0, 1
    for j in range(C):
        s += matrix[i][j]
        p *= matrix[i][j]
    print("Строка", i+1, "Сумма:", s, "Произв:", p)

for j in range(C):
    s, p = 0, 1
    for i in range(R):
        s += matrix[i][j]
        p *= matrix[i][j]
    print("Столбец", j+1, "Сумма:", s, "Произв:", p)

# 3. Максимальная сумма
max_sum, max_i = 0, 0
for i in range(R):
    s = sum(matrix[i]) # Встроенная функция sum() - это просто
    if s > max_sum:
        max_sum, max_i = s, i

max_c_sum, max_c_i = 0, 0
for j in range(C):
    s = 0
    for i in range(R):
        s += matrix[i][j]
    if s > max_c_sum:
        max_c_sum, max_c_i = s, j

print("\nМакс. сумма в строке:", max_i+1, "| в столбце:", max_c_i+1)

# 4. Меняем местами строки и столбцы
matrix[0], matrix[R-1] = matrix[R-1], matrix[0] # Строки

for i in range(R): # Столбцы
    matrix[i][0], matrix[i][C-1] = matrix[i][C-1], matrix[i][0]

print("\nПосле замены краев:")
for row in matrix:
    print(row)

# 5. Транспонирование
transposed = []
for j in range(C):
    new_row = []
    for i in range(R):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print("\nТранспонированная:")
for row in transposed:
    print(row)

if R == C:
    print("Симметрична?", matrix == transposed) # Сравнение списков в Python работает само!

# 6. Седловые точки
print("\nСедловые точки:")
for i in range(R):
    for j in range(C):
        if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([matrix[k][j] for k in range(R)]):
            print(matrix[i][j])

# 7. Уникальные элементы
unique = []
for row in matrix:
    for x in row:
        if x not in unique:
            unique.append(x)
unique.sort()
print("\nУникальные:", unique)

# 8. След матрицы
if R == C:
    trace = 0
    for i in range(R):
        trace += matrix[i][i]
    print("След:", trace)