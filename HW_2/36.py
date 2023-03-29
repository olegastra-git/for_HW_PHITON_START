a = int(input(" vvedite num_rows: - "))
b = int(input(" vvedite num_columns: - "))

def print_operation_table(operation, num_rows=a, num_columns=b):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(*list(map(operation, [i], [j])), end="\t")
print_operation_table(lambda x, y: x * y)