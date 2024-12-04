import regex as re

memory = open("../inputs/3.in").read()
matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
print(sum(int(iter_reg.pop()) * int(iter_reg.pop()) for iter_reg in (re.findall(r'\d{1,3}', match) for match in matches)))