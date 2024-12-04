class WordSearch:
    def __init__(self, input_matrix):
        self._matrix = input_matrix
        self._col_num = len(self._matrix[0])
        self._row_num = len(self._matrix)
        self._a_placeholders = []
        for row in range(self._row_num):
            for col in range(self._col_num):
                if self._matrix[row][col] == 'A':
                    self._a_placeholders += [APlaceholder(self, row, col)]

    @property
    def matrix(self):
        return self._matrix

    @property
    def row_num(self):
        return self._row_num

    @property
    def col_num(self):
        return self._col_num

    def count_mas(self):
        mas_count = 0
        for a_placeholder in self._a_placeholders:
            mas_count += a_placeholder.search_mas()
        return mas_count

class APlaceholder:
    def __init__(self, input_obj, row, col):
        self.input_obj = input_obj
        self.row = row
        self.col = col

    def search_mas(self):
        return self.increasing() and self.decreasing()

    def check(self):
        return (self.row in range(1, self.input_obj.row_num -1) and
                self.col in range(1, self.input_obj.col_num -1))

    def increasing(self):
        return ({self.input_obj.matrix[self.row + 1][self.col - 1],
                 self.input_obj.matrix[self.row - 1][self.col + 1]}
                == {'M', 'S'}) if self.check() else 0

    def decreasing(self):
        return ({self.input_obj.matrix[self.row -1][self.col -1],
                 self.input_obj.matrix[self.row +1][self.col +1]}
                == {'M', 'S'}) if self.check() else 0

lines = open("../inputs/4.in").read().splitlines()
matrix = []
for i, line in enumerate(lines):
    matrix.insert(i, list(line))
print(WordSearch(matrix).count_mas())