# домашн€€ работа по phiton задача 26
from unittest import result


a = int(input(" vvedite chislo a: - "))
b = int(input(" vvedite chislo b: - "))
def power(a,b):
    if b == 0:
        return 1
    else:
        return a* power(a, b-1)
result=power(a,b)
print(result)