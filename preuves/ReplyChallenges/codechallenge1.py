class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Grid:
    def __init__(self, width, height, golden_points, silver_points, tiles):
        self.width = width
        self.height = height
        self.golden_points = golden_points
        self.silver_points = silver_points
        self.tiles = tiles
        self.map = [['.' for _ in range(width)] for _ in range(height)]

    def add_tile(self, tile, pos):
        # add tile to the grid
        # ...

    def get_neighbors(grid, pos):
        """
        Returns the valid neighbors of a given position in the grid.
        """
        x, y = pos
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_neighbors = []

        for nx, ny in neighbors:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] != '#':
                    valid_neighbors.append((nx, ny))

    return valid_neighbors.

    def cost_path(self, path):
        """
        Calculates the cost of a given path.
        """
        cost = 0
        for i in range(1, len(path)):
            prev, curr = path[i-1], path[i]
            if grid[curr[0]][curr[1]] == 'T':
                cost += 15
            else:
                cost += 1
        return cost

    def score_path(self, path):
        """
        Calculates the score of a given path.
        """
        score = 0
        for pos in path:
            if grid[pos[0]][pos[1]] == 'S':
                score += 100
            elif grid[pos[0]][pos[1]] == 'T':
                score += 15
            else:
                score += 1
        return score


  def find_path(self, start, end):
    """
    Finds the shortest path between two points in the grid.
    """
    queue = [(0, start, [start])]
    visited = set([start])

    while queue:
        cost, pos, path = heapq.heappop(queue)

        if pos == end:
            return path

        for nx, ny in get_neighbors(grid, pos):
            if (nx, ny) not in visited:

class Tile:
    # tile class
    # ...

def solve_problem(grid):
    min_cost = float('inf')
    best_paths = None

    for gp1 in grid.golden_points:

