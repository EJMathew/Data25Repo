list = []
with open('input.txt') as inp:
    for line in inp:
        list.append(int(line))

for num1 in list:
    for num2 in list:
        if num1 + num2 == 2020:
            print(num1)
            print(num2)
            print(num1 * num2)
