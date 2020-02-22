class Map2D:
    def __init__(self):
        self.map = [[]]
        self.maxHeight = 0
        self.maxWidth = 0

    def growMapToY(self, y):
        if len(self.map) <= y:
            if self.maxHeight < y + 1:
                self.maxHeight = y + 1
            self.map.extend([[] for i in range(y - len(self.map) + 1)])

    def growMapToX(self, x, y):
        if len(self.map[y]) <= x:
            if self.maxWidth < x + 1:
                self.maxWidth = x + 1
            self.map[y].extend([None for i in range(x - len(self.map[y]) + 1)])

    def add(self, x, y, item):
        self.growMapToY(y)
        self.growMapToX(x, y)

        self.map[y][x] = item

    def check(self, x, y):
        if len(self.map) <= y:
            return None
        if len(self.map[y]) <= x:
            return None
        return self.map[y][x]

    def print(self):
        for y in range(self.maxHeight):
            row = []
            for x in range(self.maxWidth):
                item = self.check(x, y)
                row.append(item if item else '.')
            print(row)

    def count(self, predicate):
        count = 0
        for y in range(self.maxHeight):
            for x in range(self.maxWidth):
                item = self.check(x, y)
                if predicate(item):
                    count += 1
        return count

    def find(self, predicate):
        for y in range(self.maxHeight):
            for x in range(self.maxWidth):
                item = self.check(x, y)
                if predicate(item):
                    return item
        return None
