values = open("../inputs/11.in").read().splitlines()[0].split()
for _ in range(25):
    flag = False
    for i, value in enumerate(values):
        if flag:
            flag = False
            continue
        elif value == '0':
            values[i] = '1'
        elif len(value) % 2 == 0:
            tmp = value
            values[i] = value[:len(value)//2]
            values.insert(i+1, str(int(value[len(value)//2:])))
            flag = True
        else:
            values[i] = str(int(value) * 2024)
print(len(values))