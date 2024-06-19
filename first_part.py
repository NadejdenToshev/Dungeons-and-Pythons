import random

class Item:
    def __init__(self, item_type, description):
        self.item_type = item_type
        self.description = description

    def __repr__(self):
        return f"{self.item_type}: {self.description}"

class TreasureChest:
    def __init__(self, max_items):
        self.items = []
        num_items = random.randint(0, max_items)
        possible_items = [
            Item("Sword", "+10 attack power"),
            Item("Shield", "-10 incoming attack damage"),
            Item("Small Health Potion", "+10 health"),
            Item("Large Health Potion", "+50 health"),
            Item("Boots", "Allows movement of 2 steps instead of 1")
        ]
        for _ in range(num_items):
            self.items.append(random.choice(possible_items))

    def __repr__(self):
        return f"TreasureChest({self.items})"

class Cave:
    def __init__(self):
        self.edges = []
        self.treasure = None

    def add_edge(self, corridor):
        self.edges.append(corridor)

    def add_treasure(self, treasure):
        self.treasure = treasure

    def __repr__(self):
        if self.treasure:
            return 'о'
        else:
            return ' '

class Corridor:
    def __init__(self, cave1, cave2, passable):
        self.cave1 = cave1
        self.cave2 = cave2
        self.passable = passable

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.caves = [[Cave() for _ in range(cols)] for _ in range(rows)]
        self.corridors = []
        self.generate()
        self.place_treasures()

    def generate(self):
        directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
        for x in range(self.rows):
            for y in range(self.cols):
                current_cave = self.caves[x][y]
                for dx, dy in directions.values():
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
        return any((corridor.cave1 == cave1 and corridor.cave2 == cave2) or 
                   (corridor.cave1 == cave2 and corridor.cave2 == cave1) 
                   for corridor in self.corridors)

    def _is_passable(self, cave1, cave2):
        for corridor in cave1.edges:
            if (corridor.cave1 == cave1 and corridor.cave2 == cave2) or \
               (corridor.cave1 == cave2 and corridor.cave2 == cave1):
                return corridor.passable
        return False

    def place_treasures(self):
        num_treasures = random.randint(min(self.rows, self.cols), max(self.rows, self.cols))
        max_items = min(self.rows, self.cols)
        placed_treasures = 0
        while placed_treasures < num_treasures:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if self.caves[x][y].treasure is None:
                self.caves[x][y].add_treasure(TreasureChest(max_items))
                placed_treasures += 1

    def __repr__(self):
        maze_repr = ""
        for x in range(self.rows):
            for y in range(self.cols):
                maze_repr += f"|{self.caves[x][y]}"
            maze_repr += "|\n"
            if x < self.rows - 1:
                for y in range(self.cols):
                    if self._is_passable(self.caves[x][y], self.caves[x+1][y]):
                        maze_repr += " "
                    else:
                        maze_repr += "x"
                    maze_repr += " "
                maze_repr += "\n"
        return maze_repr

# Example usage
if __name__ == "__main__":
    N = random.randint(5, 5)
    M = random.randint(5, 5)
    maze = Maze(N, M)
    print(maze)









 








