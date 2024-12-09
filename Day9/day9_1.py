class Block:
    def __init__(self, position, file_id):
        self.position = position
        self.file_id = file_id

    def to_string(self):
        return str(self.file_id) if self.file_id >= 0 else "."

class Sorter:
    def __init__(self, blocks):
        self.blocks = blocks

    def sort(self):
        left, right = 0, len(self.blocks) - 1
        while left < right:
            left = self.next_index(left, right, lambda x: x == -1, 1)
            right = self.next_index(right, left, lambda x: x != -1, -1)
            self.blocks[left].file_id, self.blocks[right].file_id = self.blocks[right].file_id, self.blocks[left].file_id

    def next_index(self, start, end, condition, step):
        for idx in range(start, end, step):
            if condition(self.blocks[idx].file_id):
                return idx
        return end

string = open("../inputs/9.in").read().splitlines()[0]
blocks = [Block(i, i // 2 if i % 2 == 0 else -1) for i, block in enumerate(string) for _ in range(int(block))]
Sorter(blocks).sort()
print(sum(block.file_id * i for i, block in enumerate(blocks) if block.file_id >= 0))
