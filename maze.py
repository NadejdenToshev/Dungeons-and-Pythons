import random
from cave import Cave
from corridor import Corridor


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.caves = [[Cave() for y in range(cols)] for x in range(rows)]
        self.corridors = []  

    def generate(self):
        directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
        for x in range(self.rows):
            for y in range(self.cols):
                current_cave = self.caves[x][y]
                for direction, (dx, dy) in directions.items():
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rows and 0 <= ny < self.cols:
                        neighbor_cave = self.caves[nx][ny]
                        if not self._corridor_exists(current_cave, neighbor_cave):
                            passable = random.choice([True, False])
                            corridor = Corridor(current_cave, neighbor_cave, passable)
                            self.corridors.append(corridor)
                            if passable:
                                current_cave.add_edge(corridor)
                                neighbor_cave.add_edge(corridor)

    def _corridor_exists(self, cave1, cave2):
        for corridor in self.corridors:
            if (corridor.cave1 == cave1 and corridor.cave2 == cave2) or (corridor.cave1 == cave2 and corridor.cave2 == cave1):
                return True
        return False

    def is_passable(self, cave1, cave2):
        for corridor in cave1.edges:
            if (corridor.cave1 == cave1 and corridor.cave2 == cave2) or (corridor.cave1 == cave2 and corridor.cave2 == cave1):
                return corridor.passable
        return False

    def __repr__(self):
        maze_repr = ""
        for x in range(self.rows):
            for y in range(self.cols):
                maze_repr += f"{self.caves[x][y]} "
            maze_repr += "\n"
        return maze_repr



    