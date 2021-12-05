list = []
with open('password.txt') as f:
    for line in f:
        list.append(line.replace('\n', ''))

valid_password = 0
a = set()

for i in list:
    key, value = i.split(': ')
    k1, k2 = key.split(' ')
    min = k1.split('-')[0]
    max = k1.split('-')[-1]

    if int(min) <= value.count(k2) <= int(max):
        valid_password += 1

print(valid_password)
