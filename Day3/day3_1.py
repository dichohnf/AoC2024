import regex as re

memory = open("../inputs/3.in").read()
matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
result = 0
for match in matches:
    iter_reg = re.findall(r'\d{1,3}', match)
    result += int(iter_reg.pop()) * int(iter_reg.pop())
print(result)


