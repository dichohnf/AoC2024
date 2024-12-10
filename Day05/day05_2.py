class Update:
    def __init__(self, sorting_list, update):
        self.update = update
        self.sorting_list = [rule for rule in sorting_list if any(rule[0] == page and rule[1] in update for page in update)]

    def is_sorted(self):
        for rule in self.sorting_list:
            if 0 < self.update.index(rule[1]) < self.update.index(rule[0]):
                return False
        return True

    def sort(self):
        from collections import defaultdict
        from graphlib import TopologicalSorter
        graph = defaultdict(list)
        for u, v in self.sorting_list:
            graph[u].append(v)
        sorting_method = TopologicalSorter(graph)
        self.update = list(sorting_method.static_order())
        return self

    def mid_value(self):
        return self.update[len(self.update)//2]

import regex as re
input_string = open("../inputs/5.in").read()
rules = re.findall(r"\d{2}\|\d{2}", input_string)
rules = [(int(item[0]), int(item[1])) for item in (re.findall(r"\d{2}", rule) for rule in rules)]
updates = re.findall(r".*\d{2},.*\n?", input_string)[::-1]
updates = list(re.findall(r"\d{2}", update) for update in updates)
updates[:] = [[int(page) for page in update] for i, update in enumerate(updates)]

print(sum(up.sort().mid_value() for up in [Update(rules, update) for update in updates] if not up.is_sorted()))
