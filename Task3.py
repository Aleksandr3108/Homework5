n = int(input("Введіть кількість рядків: \n"))
m = int(input("Введіть кількість стовпчиків: \n"))
my_list = []
for i in range(n):
    row = [int(j) for j in input("Введіть рядок чисел:  \n").split()]
    while len(row) != m:
        row = [int(j) for j in input("Введіть корректно рядок! \n").split()]
    my_list.append(row)
print(my_list)

counter = 0
s_sum = 0
for i in my_list:
    for j in i:
        if j >= 0:
            s_sum = s_sum + j
            counter = counter + 1
print("Середнє арифметичне:", s_sum / counter)