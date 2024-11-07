import numpy as np

def rref(matrix):
    matrix = matrix.astype(float)  # Ensure the matrix is in float to handle division

    rows, cols = matrix.shape
    row = 0  # Start with the first row

    for col in range(cols):
        if row >= rows:
            break
        
        # Find the pivot row (the row with the largest value in the current column)
        max_row = np.argmax(np.abs(matrix[row:rows, col])) + row
        if matrix[max_row, col] == 0:
            continue  # Skip this column if no pivot is found
        
        # Swap the current row with the pivot row
        matrix[[row, max_row]] = matrix[[max_row, row]]

        # Scale the pivot row to make the pivot element 1
        matrix[row] = matrix[row] / matrix[row, col]

        # Eliminate all other entries in the current column
        for i in range(rows):
            if i != row:
                matrix[i] = matrix[i] - matrix[i, col] * matrix[row]

        # Move to the next row
        row += 1

    return matrix

# Example matrix
matrix = np.array([
    [1, 5, 1],
[2, 11, 5]
], dtype=float)

print("Original Matrix:")
print(matrix)


# Get the Reduced Row Echelon Form (RREF)
rref_matrix = rref(matrix)
print("\nReduced Row Echelon Form (RREF):")
print(rref_matrix)
