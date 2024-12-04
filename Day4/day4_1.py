class WordSearch:
    def __init__(self, input_matrix):
        self._matrix = input_matrix
        self._col_num = len(self._matrix[0])
        self._row_num = len(self._matrix)
        self._x_placeholders = []
        for row in range(self._row_num):
            for col in range(self._col_num):
                if self._matrix[row][col] == 'X':
                    self._x_placeholders += [XPlaceholder(self, row, col)]

    @property
    def matrix(self):
        return self._matrix

    @property
    def row_num(self):
        return self._row_num

    @property
    def col_num(self):
        return self._col_num

    def count_xmas(self):
        xmas_count = 0
        for x_placeholder in self._x_placeholders:
            xmas_count += x_placeholder.search_xmas()
        return xmas_count

class XPlaceholder:
    def __init__(self, input_obj, row, col):
        self.input_obj = input_obj
        self.row = row
        self.col = col

    def search_xmas(self):
        return (self.right() + self.right_up() + self.up() +
                self.left_up() + self.left() + self.left_down()
                + self.down() + self.right_down())
    def search(self, row_step, col_step):
        return (self.input_obj.matrix[self.row + row_step][self.col + col_step] == 'M' and
            self.input_obj.matrix[self.row + row_step * 2][self.col + col_step * 2] == 'A' and
            self.input_obj.matrix[self.row + row_step * 3][self.col + col_step * 3] == 'S')

    def check_right(self):
        return self.col < self.input_obj.col_num - 3
    def check_up(self):
        return self.row >= 3
    def check_left(self):
        return self.col >= 3
    def check_down(self):
        return self.row < self.input_obj.row_num - 3

    def right(self):
        return self.search(0, 1) if self.check_right() else 0
    def right_up(self):
        return self.search( -1, 1) if self.check_right() and self.check_up() else 0
    def up(self):
        return self.search(-1, 0) if self.check_up() else 0
    def left_up(self):
        return self.search(-1, -1) if self.check_left() and self.check_up() else 0
    def left(self):
        return self.search(0, -1) if self.check_left() else 0
    def left_down(self):
        return self.search(1, -1) if self.check_left() and self.check_down() else 0
    def down(self):
        return self.search(1, 0) if self.check_down() else 0
    def right_down(self):
        return self.search(1, 1) if self.check_right() and self.check_down() else 0

lines = open("../inputs/4.in").read().splitlines()
matrix = []
for i, line in enumerate(lines):
    matrix.insert(i, list(line))
print(WordSearch(matrix).count_xmas())
