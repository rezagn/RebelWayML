import random

def generate_maze(width, height, seed=None):
    if seed is not None:
        random.seed(seed)

    # Direction of movements: up, down, left, right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the maze full of walls (1)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # List of path cells to define start and end
    path = []

    def dfs(x, y):
        # Mark the current cell as part of the path (0)
        maze[x][y] = 0
        path.append((x, y))
        
        # Shuffle the movements for randomness
        random.shuffle(movements)
        
        for dx, dy in movements:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == 1:
                maze[x + dx][y + dy] = 0
                dfs(nx, ny)

    # Start the generation of the maze from the top left corner
    dfs(0, 0)

    # Mark the start point (2) and the end point (3)
    if path:
        start = path[0]
        end = path[-1]
        maze[start[0]][start[1]] = 2
        maze[end[0]][end[1]] = 3

    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(str(cell) for cell in row))

# Maze configuration
width = 5
height = 5
seed = 42  # You can change the seed to get a different maze

# Generate and display the maze
maze = generate_maze(width, height, seed)
print_maze(maze)
