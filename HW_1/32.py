list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
min = int(input('vveite minimalnoe chslo: '))
max = int(input('vveite maksimalnoechslo: '))
for i in range(len(list)):
    if min <= list[i] <= max:
        print(i)