import random

class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[1] * (2 * cols + 1) for _ in range(2 * rows + 1)]
        self.visited = [[False] * cols for _ in range(rows)]

    def generate_maze(self, start_row=0, start_col=0):
        self._generate_path(start_row, start_col)

    def _generate_path(self, row, col):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # right, down, left, up
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and not self.visited[new_row][new_col]:
                self.visited[new_row][new_col] = True
                self.maze[row * 2 + 1 + dr][col * 2 + 1 + dc] = 0
                self.maze[row * 2 + 1 + 2 * dr][col * 2 + 1 + 2 * dc] = 0
                self._generate_path(new_row, new_col)

# Example Usage for Maze Generation
if __name__ == "__main__":
    maze_rows = 5
    maze_cols = 5

    generator = MazeGenerator(maze_rows, maze_cols)
    generator.generate_maze()

    for row in generator.maze:
        print(' '.join(['#' if cell == 1 else ' ' for cell in row]))
