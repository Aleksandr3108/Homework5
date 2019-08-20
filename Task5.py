n = int(input("Введіть кількість рядків: \n"))
m = int(input("Введіть кількість стовпчиків: \n"))
my_list = []
for i in range(n):
    row = [int(j) for j in input("Введіть рядок чисел:  \n").split()]
    while len(row) != m:
        row = [int(j) for j in input("Введіть корректно рядок \n").split()]
    my_list.append(row)
for i in my_list:
    i.sort()
print(my_list)


