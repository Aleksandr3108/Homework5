n = int(input("Введіть кількість рядків: \n"))
m = int(input("Введіть кількість стовпчиків: \n"))
my_list = []
for i in range(n):
    row = [int(j) for j in input("Введіть рядок чисел:  \n").split()]
    while len(row) != m:
        row = [int(j) for j in input("Введіть корректно рядок: \n").split()]
    my_list.append(row)
print(my_list)
minimum = my_list[0][0]
min_num = 0
for i in range(len(my_list)):
    if min(my_list[i]) < minimum:
        minimum = min(my_list[i])
        min_num = i
print(minimum, my_list[min_num])

