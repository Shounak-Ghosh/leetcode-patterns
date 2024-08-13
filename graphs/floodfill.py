def flood_fill(matrix, x, y, new_color):
    # Dimensions of the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # The color of the starting pixel
    original_color = matrix[x][y]
    
    # If the starting pixel is already of the new color, return immediately
    if original_color == new_color:
        return
    
    # Helper function to perform DFS
    def dfs(x, y):
        # Base case: if the pixel is out of bounds or not the original color, return
        if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] != original_color:
            return
        
        # Fill the pixel with the new color
        matrix[x][y] = new_color
        
        # Recursive calls for the four adjacent directions
        dfs(x + 1, y)  # Down
        dfs(x - 1, y)  # Up
        dfs(x, y + 1)  # Right
        dfs(x, y - 1)  # Left

    # Start the flood fill from the initial pixel
    dfs(x, y)

# Example usage
matrix = [
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1]
]

flood_fill(matrix, 1, 1, 2)

for row in matrix:
    print(row)
