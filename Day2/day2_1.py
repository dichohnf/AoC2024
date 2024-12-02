class Report:
  def __init__(self, levels):
    self.levels = [int(level) for level in levels]

  def is_safe(self):
    if self.levels[0] < self.levels[1]:
        for i in range(len(self.levels)-1):
            if self.levels[i+1] - self.levels[i] not in range(1,4):
                return False
    elif self.levels[0] > self.levels[1]:
        for i in range(len(self.levels)-1):
            if self.levels[i] - self.levels[i+1] not in range(1,4):
                return False
    elif self.levels[0] == self.levels[1]:
        return False
    return True

reports = open("../inputs/2.in").read().splitlines()

safe_reports = 0
for report in reports:
    rep = Report(report.split())
    safe_reports += rep.is_safe()
print(safe_reports)