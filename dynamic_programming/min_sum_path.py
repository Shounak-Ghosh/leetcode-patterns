def min_sum_path(A, B):
    N = len(A)
    
    # Create a DP table
    dp = [[0] * N for _ in range(2)]
    
    # Initialize the DP table
    dp[0][0] = A[0]
    dp[1][0] = A[0] + B[0]
    
    # Fill the DP table
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + A[j]  # Moving right in the upper row
        dp[1][j] = min(dp[0][j-1] + B[j], dp[1][j-1] + B[j])  # Moving down or right in the lower row
    
    # Trace back to find the path
    path = []
    row, col = 1, N - 1  # Start from the bottom-right corner
    while col > 0:
        path.append((row, col))
        if row == 1 and dp[1][col] == dp[0][col-1] + B[col]:
            row = 0  # Move up
        col -= 1
    path.append((0, 0))  # Add the starting point
    path.reverse()  # Reverse the path to start from (0, 0)
    
    # Return the minimum sum and the path
    return dp[1][N-1], path

# Example usage
A = [1, 3, 1, 4]
B = [2, 1, 3, 1]
min_sum, path = min_sum_path(A, B)
print(f"Minimum sum: {min_sum}")
print(f"Path: {path}")
