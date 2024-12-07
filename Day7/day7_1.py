class Equation:
    def __init__(self, result, numbers):
        self.result = int(result)
        self.numbers = [int(number) for number in numbers]
        self.comb = 0

    def is_solvable(self):
        while self.comb <= (2**(len(self.numbers)-1)):
            if self.__comb_calc__() == self.result:
                return True
            self.comb += 1
        return False

    def __comb_calc__(self):
        res = 0
        for j, number in enumerate(self.numbers):
            if j == 0:
                res = number
            elif (self.comb//(2 ** (j-1))) % 2 == 0:
                res += number
            else:
                res *= number
        return res

import regex as re
lines = open("../inputs/7.in").read().splitlines()
results = [re.findall(r"^\d+", line) for line in lines]
equations_numbers = [line[line.index(":")+1:].split() for line in lines]
print(sum([int(results[i][0]) for i in range(len(results)) if Equation(results[i][0], equations_numbers[i]).is_solvable()]))

