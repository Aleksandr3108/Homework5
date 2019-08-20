my_string = input("Введіть рядок слів:")
my_string = my_string.split(' ')
counter = 0
for x in my_string:
    if my_string.count(x) == 1:
        counter = counter + 1
print(counter)