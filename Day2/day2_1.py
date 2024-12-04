class Report:
  def __init__(self, levels):
    self.levels = [int(level) for level in levels]

  def is_safe(self):
    if self.levels[0] < self.levels[1]:
        return all(self.levels[i+1] - self.levels[i] in range(1,4)
                for i in range(len(self.levels)-1))
    elif self.levels[0] > self.levels[1]:
        return all(self.levels[i] - self.levels[i+1] in range(1,4)
                for i in range(len(self.levels)-1))
    else:
        return self.levels[0] != self.levels[1]


reports = open("../inputs/2.in").read().splitlines()
print(sum(Report(report.split()).is_safe()
          for report in reports))