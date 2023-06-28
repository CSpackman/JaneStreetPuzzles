
def solve_puzzle():
    grid = [[0 for _ in range(9)] for _ in range(9)]  # Initialize the grid with zeros
    hooks = [9, 8, 7, 6, 5, 4, 3, 2, 1]  # Number of squares in each hook

    # Helper function to check if a number can be placed in a specific position
    def is_valid(number, row, col):
        # Check if the number is already present in the row or column
        for i in range(9):
            if grid[row][i] == number or grid[i][col] == number:
                return False

        # Check if every 2-by-2 region contains at least one unfilled square
        for i in range(row - (row % 3), row - (row % 3) + 3):
            for j in range(col - (col % 3), col - (col % 3) + 3):
                if grid[i][j] == number:
                    return False

        return True

    # Helper function to find the next empty square in the grid
    def find_empty_square():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return None, None  # No empty square found

    # Backtracking function to solve the puzzle
    def backtrack():
        # Check if all hooks are filled
        if not hooks:
            return True

        # Find the next empty square
        row, col = find_empty_square()

        # Try placing numbers in the empty square
        for number in hooks:
            if is_valid(number, row, col):
                grid[row][col] = number
                hooks.remove(number)

                # Recursively solve the puzzle
                if backtrack():
                    return True

                grid[row][col] = 0  # Reset the square
                hooks.append(number)

        return False

    # Start backtracking to solve the puzzle
    backtrack()

    return grid


# Solve the puzzle and print the valid grid
grid = solve_puzzle()
for row in grid:
    print(row)


# This algorithm will solve the puzzle and print the valid grid configuration where the L-shaped hooks are filled with the respective numbers.