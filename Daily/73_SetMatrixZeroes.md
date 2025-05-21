# 73. Set Matrix Zeroes

## LeetCode Link
[73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)

## Problem Description
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

![Example](/Daily/screenshots/73/examples.png)

## Initial Thought Process & Brute Force
Make a copy of the original Array. We then iterate the Matrix using the copy of the array. We do this to keep track of digits. Lets say i encounter a 0 at matrix[m][n] and i set the entire row and column as 0. After traversing the matrix further we encounter a 0 when it should have been say a 1. We are supposed to change the matrix only at the end. By iterating through the copy and making changes to only the original we not only avoid the mistake highlighted earlier but also edit the matrix in place as per question. However this solution requires a 0(1) space complexity. The current solution is o(n).

## Optimized Approach
Looking at the hints i was quickly able to figure out that we can use the first row and column as flags. When we encounter a 0 we can set the first value of that row and column to 0. This way after iterating through the entire array we can edit the array in place in the end. However i ran into two problems:
* My solution was not accounting for the fact that row and column flag will overlap on matrix[0][0].

Inorder to get a trully correct solution i turn to [neetcode](https://www.youtube.com/watch?v=T41rL0L3Pnw).

### Neetcode Solution

Below is a diagram to visualize the structure of flags in a matrix.  
![Diagram of matrix](/Daily/screenshots/73/diagram.png)  

### Step-by-Step Breakdown

1. **Store Dimensions**  
   Save the number of rows and columns in `rows` and `cols`.

2. **Flag Setup**  
   Use the **first row and first column** of the matrix to act as **flags** to mark which rows and columns should be zeroed later.  
   Since `matrix[0][0]` overlaps both first row and column, use an extra boolean `rowZero` to track whether the **first row** needs to be zeroed.

3. **First Pass – Mark Rows and Columns**  
   Iterate over the matrix:  
   - If `matrix[r][c] == 0`:
     - Set `matrix[0][c] = 0` → mark column `c` for zeroing.
     - If `r > 0`, set `matrix[r][0] = 0` → mark row `r` for zeroing.
     - If `r == 0`, set `rowZero = True`.

4. **Second Pass – Apply Flags (excluding first row and column)**  
   Iterate from row 1 and column 1:
   - If either `matrix[0][c] == 0` or `matrix[r][0] == 0`, set `matrix[r][c] = 0`.

5. **Handle First Column**  
   - If `matrix[0][0] == 0`, set the **entire first column** to `0`.

6. **Handle First Row**  
   - If `rowZero` is `True`, set the **entire first row** to `0`.

***Thanks to chat gpt for helping me summarize the solution below***

### Time Complexity
$O(N * M)$ 

### Space Complexity
$O(1)$ 

## Code
```python
# Python solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Saving number of rows and columns in two variables.
        rows, cols = len(matrix), len(matrix[0])
        # We are making use of first row and column as flags. matrix[0][0] will overlap for rows and columns so taking an extra variable. 
        rowZero = False
        # Iterating through matrix
        for r in range(rows):
            for c in range(cols):
                # If the cell is 0 we move to if condition.
                if matrix[r][c] == 0:
                    # We set the 1st element in that column to zero.
                    matrix[0][c] = 0
                    # If r>0 (since we have extra rowZero variable) we set first element in that particular row to zero.
                    if r > 0:
                        matrix[r][0] = 0
                    # If r = 0 setting the variable to true instead.
                    else:
                        rowZero = True
        # Again iterating through matrix except row, col = 0, 0.
        for r in range(1, rows):
            for c in range(1, cols):
                # If first row and column have 0 anywhere we set the whole row/column to zero.
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # Checking if first row ( in this case for column flag) = 0. If true it will update the whole column to zero.
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        # Checking if variable (row flag) is true. When true it will set whole row 0 to the value 0.
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0                  
