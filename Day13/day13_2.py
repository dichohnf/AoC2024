class Machine:
    def __init__(self,A, B, prize):
        self.A = {"X":A[0], "Y":A[1]}
        self.B = {"X":B[0], "Y":B[1]}
        self.prize = {"X":prize[0], "Y":prize[1]}
        sol = self.__calculate_solution__()
        self.solution = {"A":sol[0], "B":sol[1]} if sol else None

    def __calculate_solution__(self):
        denom = self.B["Y"] * self.A["X"] - self.A["Y"] * self.B["X"]
        pa_num = self.prize["X"] * self.B["Y"] - self.prize["Y"] * self.B["X"]
        pb_num = self.prize["Y"] * self.A["X"] - self.prize["X"] * self.A["Y"]
        passes = (pa_num // denom, pb_num // denom) if pa_num % denom == 0 and pb_num % denom == 0 else (-1,-1)
        return passes if (
            passes[0] >= 0 and
            passes[1] >= 0
        ) else None

    def is_solvable(self):
        return self.solution is not None

import regex as re
lines = open("../inputs/13.in").read().splitlines()
costs = {"A":3,"B":1}
machines = []

for claw_lines in [lines[i:i+3] for i in range(0, len(lines), 4)]:
    A       = [int(val) for val in (re.findall(r"\d+", claw_lines[0]))]
    B       = [int(val) for val in (re.findall(r"\d+", claw_lines[1]))]
    prize   = [int(val)+10000000000000 for val in (re.findall(r"\d+", claw_lines[2]))]
    machines.append(Machine(A, B, prize))

print(sum(
    machine.solution["A"] * costs["A"] + machine.solution["B"] * costs["B"]
    for machine in machines
    if machine.is_solvable()
))