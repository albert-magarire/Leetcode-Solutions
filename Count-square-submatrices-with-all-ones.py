'''
THE PROBLEM:
    Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
        
        Example 1:
        Input: matrix =
        [
          [0,1,1,1],,
          [1,1,1,1],
          [0,1,1,1]
        ]
        Output: 15
        Explanation: 
        There are 10 squares of side 1.
        There are 4 squares of side 2.
        There is  1 square of side 3.
        Total number of squares = 10 + 4 + 1 = 15.
        
        Example 2:
        Input: matrix = 
        [
          [1,0,1],
          [1,1,0],
          [1,1,0]
        ]
        Output: 7
        Explanation: 
        There are 6 squares of side 1.  
        There is 1 square of side 2. 
        Total number of squares = 6 + 1 = 7.
'''

'''
THOUGHT PROCESS:
(This is basically just a brute force solution)
    We are going to iterate over each element in the matrix, treating it as the top left corner of the sub-matrix
    If matrix[i][j] == 1, then increment submatrix_sum by 1
    Next check if 
        [i+n][j], 
        [i][j+n], 
        [i+n][j+n] 
        are all equal to 1, starting with n = 1,
     Every time we have a square submatrix, then we have to remember it and then n increases by 1 in a recursive function
     It is important to limit the values that n can have to avoid going out of bounds IndexError
     Base Cases:
         What if all values are 1s
         What if none of the values are 1s
         Is the array length fixed
     How are we going to store/remember the submatrices that we come up with --> Do we even need to store them🤷
    
'''

'''
CHOSEN SOLUTION:
    I couldn't think of anything better, however after looking it up on ChatGPT, you can use Dynamic Programming(which I haven't studied yet)
    
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        submatrix_sum = 0

        # Helper function to check if all elements in the square are 1
        def is_square_of_ones(i, j, n):
            # Ensure the square does not extend beyond the matrix bounds
            if i + n > rows or j + n > cols:
                return False
            # Check the boundaries of the n x n square
            for x in range(i, i + n):
                if matrix[x][j + n - 1] != 1:
                    return False
            for y in range(j, j + n):
                if matrix[i + n - 1][y] != 1:
                    return False
            return True

        # Iterate over all possible top-left corners of the submatrices
        for i in range(rows):
            for j in range(cols):
                # If the current cell is 1, start expanding the square size
                if matrix[i][j] == 1:
                    # Count the initial 1x1 square
                    submatrix_sum += 1
                    n = 2
                    # Check for larger squares
                    while is_square_of_ones(i, j, n):
                        submatrix_sum += 1
                        n += 1

        return submatrix_sum
'''
TIME COMPLEXITY:
     ### 1. Outer loops:
     - The two outer loops are running concurrently with a O(m * n) complexity.

     ### 2. While loop:
     - Every element is being checked for larger submatrixes by increasing the value of n
     - This takes O(n)
     
SPACE COMPLEXITY:
    ### 1. Vowel Set:
    -  In this solution, no new data structures are being created except for a few variables.
    - Therefore, the space complexity is O(1)
    
'''
