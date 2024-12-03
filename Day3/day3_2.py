import regex as re

memory = open("../inputs/3.in").read()
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", memory)

result = 0
active = 1
for match in matches:
    if re.findall(r"don", match):
        active = 0
    elif re.findall(r"do", match):
        active = 1
    elif active:
        iter_reg = re.findall(r'\d{1,3}', match)
        result += int(iter_reg.pop()) * int(iter_reg.pop()) * active
print(result)