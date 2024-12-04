class ReportRemovedLevel:
    def __init__(self, levels, idx_to_remove):
        self.levels = [int(level) for level in levels]
        self.levels = self.levels[:idx_to_remove] + self.levels[idx_to_remove+1:]

    def is_safe(self):
        if self.levels[0] < self.levels[1]:
            return all(self.levels[i+1] - self.levels[i] in range(1,4)
                    for i in range(len(self.levels)-1))
        elif self.levels[0] > self.levels[1]:
            return all(self.levels[i] - self.levels[i+1] in range(1,4)
                   for i in range(len(self.levels)-1))
        else:
            return self.levels[0] != self.levels[1]

class Report:
    def __init__(self, levels):
        self.levels = [int(level) for level in levels]

    def is_safe(self):
        return any(ReportRemovedLevel(self.levels,i).is_safe() for i in range(len(self.levels)))

reports = open("../inputs/2.in").read().splitlines()
print(sum(Report(report.split()).is_safe() for report in reports))