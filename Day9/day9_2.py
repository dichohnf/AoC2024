class File:
    def __init__(self, position, file_id, dimension):
        self.position = position
        self.file_id = file_id
        self.dimension = dimension

class ContiguousBlankSpace:
    def __init__(self, position, dimension):
        self.position = position
        self.dimension = dimension

class Sorter:
    def __init__(self, files, blank_spaces):
        self.files = files
        self.blank_spaces = blank_spaces
    def sort(self):
        for file_id in range(len(self.files)-1, 0, -1):
            self.search_and_move(file_id)
    def search_and_move(self, file_id):
        file = self.files[file_id]
        for idx, space in enumerate(self.blank_spaces):
            if file.position < space.position:
                return
            if file.dimension <= space.dimension:
                file.position, space.position = space.position, file.position
                new_space_dim, space.dimension = space.dimension - file.dimension, file.dimension
                if new_space_dim > 0:
                    self.blank_spaces.insert(
                        idx,
                        ContiguousBlankSpace(
                            file.position + file.dimension,
                            new_space_dim))
                    idx += 1
                self.merge_blank_spaces(idx, space)
    def merge_blank_spaces(self, idx, space):
        while idx+1 < len(self.blank_spaces) and space.position > self.blank_spaces[idx+1].position:
            self.blank_spaces[idx], self.blank_spaces[idx+1] = self.blank_spaces[idx+1], self.blank_spaces[idx]
            idx += 1
        if self.blank_spaces[idx-1].position + self.blank_spaces[idx-1].dimension >= space.position -1:
            idx -= 1
            self.blank_spaces[idx].dimension += space.dimension
            self.blank_spaces.remove(space)
            space = self.blank_spaces[idx]
        if idx+1 < len(self.blank_spaces) and space.position + space.dimension >= self.blank_spaces[idx+1].position -1:
            space.dimension += self.blank_spaces[idx+1].dimension
            self.blank_spaces.remove(self.blank_spaces[idx+1])

string = open("../inputs/9.in").read().splitlines()[0]
files = []
blank_spaces = []
pos = 0
for i, value in enumerate(string):
    if i % 2 == 0:
        files.append(File(pos, i//2, int(value)))
        pos += int(value)
    else:
        blank_spaces.append(ContiguousBlankSpace(pos, int(value)))
        pos += int(value)
Sorter(files, blank_spaces).sort()
print(sum(file.file_id * sum(range(file.position, file.position+file.dimension)) for file in files))