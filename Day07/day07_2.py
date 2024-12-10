class Equation:
    def __init__(self, result, numbers):
        self.result = result
        self.numbers = numbers
        self.comb = 0

    def is_solvable(self):
        while self.comb <= (3**(len(self.numbers)-1)):
            if int(self.__comb_calc__()) == self.result:
                return True
            self.comb += 1
        return False

    def __comb_calc__(self):
        res = ""
        for j, number in enumerate(self.numbers):
            mod = (self.comb//(3 ** (j-1))) % 3
            if j == 0:
                res = number
            elif mod == 0:
                res = str(int(res) + int(number))
            elif mod == 1:
                res = str(int(res) * int(number))
            else:
                res = res + number
        return res

import regex as re
lines = open("../inputs/7.in").read().splitlines()
results = [int(re.findall(r"^\d+", line)[0]) for line in lines]
equations_numbers = [line[line.index(":")+1:].split() for line in lines]
print(sum([results[i] for i in range(len(results)) if Equation(results[i], equations_numbers[i]).is_solvable()]))