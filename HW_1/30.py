a1 = int(input('vvedite chislo a: '))
b = int(input('vvedite chislo b:'))
n = int(input('vvedite chislo N:'))
result = [a1 + (i - 1) * b
          for i in range(1, n + 1)]
print(result)