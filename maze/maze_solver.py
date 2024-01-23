import heapq

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.start = (0, 0)
        self.end = (self.rows - 1, self.cols - 1)

    def solve_maze(self):
        path = self._a_star()
        if path:
            self._print_solution(path)
        else:
            print("No solution found.")

    def _a_star(self):
        heap = [(0, self.start, [])]  # (cost, current position, path)
        heapq.heapify(heap)

        while heap:
            cost, current, path = heapq.heappop(heap)
            if current == self.end:
                return path + [current]

            if not self.visited[current[0]][current[1]]:
                self.visited[current[0]][current[1]] = True

                for neighbor in self._get_neighbors(current):
                    heapq.heappush(heap, (cost + 1 + self._heuristic(neighbor), neighbor, path + [current]))

        return []

    def _get_neighbors(self, position):
        row, col = position
        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        return [(r, c) for r, c in neighbors if 0 <= r < self.rows and 0 <= c < self.cols and not self.maze[r][c]]

    def _heuristic(self, position):
        return abs(position[0] - self.end[0]) + abs(position[1] - self.end[1])

    def _print_solution(self, path):
        solution = [[0] * self.cols for _ in range(self.rows)]
        for row, col in path:
            solution[row][col] = 1

        for row in solution:
            print(' '.join(['*' if cell == 1 else ' ' for cell in row]))

# Example Usage for Maze Solving
if __name__ == "__main__":
    maze_rows = 5
    maze_cols = 5

    generator = MazeGenerator(maze_rows, maze_cols)
    generator.generate_maze()

    for row in generator.maze:
        print(' '.join(['#' if cell == 1 else ' ' for cell in row]))

    print("\nSolving the Maze...\n")

    solver = MazeSolver(generator.maze)
    solver.solve_maze()
