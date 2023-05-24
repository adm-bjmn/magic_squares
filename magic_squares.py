''' Magic Squares Solver'''

def magic_square_solver(entered_number):
    '''
    The magic_square_solver takes an odd number (n) entered by a user 
    and creates a matix of n * n. The function then completes a magic square
    within the matrix with all numbers ranging 1 to n^2 only appearing 
    once. The algorithm follows a sequence were by numbers are added in order
    starting at one. The next number is added one position up and one 
    position across to the right on the grid, unless this number has already 
    been added in which case the number is added directly below the most recently 
    added number.
    '''
    matrix=[] #define empty matrix
    for i in range(entered_number): # create 'n' number of rows
        row=[] 
        for j in range(entered_number): # for each row created 
            row.append(0) # add 0 value for 'n' number of columns
        matrix.append(row) #add row to the matrix
    
    total_numbers = entered_number * entered_number # eg 3x3 grid = 9 numbers
    middle_index = int(len(range(entered_number))/2) # to define start point
    
    # for this solution the starting point is always the middle of the top row
    matrix_X = 0 # matrix X postion
    matrix_Y = middle_index # matrix Y postion
    
    for number in range(1,total_numbers+1):
        '''
        if the position variables happen to move off the edges of the matrix
        then the following logic will cause it to loop back to the other side.
        For example if the position goes of the edge of the left side (-1) 
        of the matrix it will appear back on the right side by using negative
        indexing ([-1]).
        Imagine the old snake game.
        '''
        if matrix_X == -1:
            matrix_X = range(entered_number)[-1] 
        if matrix_Y == -1:
            matrix_Y = range(entered_number)[-1]
        if matrix_Y == entered_number:
            matrix_Y = 0
        if matrix_X == entered_number:
            matrix_X = 0
        '''
        for each iteration, if the index hasnt been changed (0) then change
        it to the current number and move X postion up 1 on grid and move
        Y position along 1 on grid.
        If the index has already been changed then the position is moved down 
        one from the previously changed index and that index is changed to the
        current number.
        '''
        if matrix[matrix_X][matrix_Y] == 0: # check if number has be changed
            matrix[matrix_X][matrix_Y] = number 
            matrix_X = matrix_X - 1 # move X position for next iteration
            matrix_Y = matrix_Y + 1 # move Y position for next iteration
        else: 
            if matrix_X == entered_number-1: 
                matrix[1][-1] = number
                matrix_X = matrix_X + 1  # move X position for next iteration
            else:
                matrix[matrix_X+2][matrix_Y-1] = number
                matrix_X = matrix_X + 1  # move X position for next iteration
    
    return matrix

def magic_square_validity(matrix, entered_number):
    '''
    The magic_square_valisity function tests the validity of a magic 
    square by testing whether the total of the numbers in each individial 
    horizontal, vertical and corner to corner line is the same. 
    It does so be determaining a control (the top row) and comparing all other
    rows, columns and diaganals to the control.
    If any totals do not match the control the square is invalid.
    '''
    
    test_row = 0 # stores the control total

    # set the test row variable to to the total of the top row
    for i in matrix[0]:
        test_row = test_row + i
    
    # compare horizontal lines
    for i, row in enumerate(matrix):
        # calculate sum of current row and compare to control
        if sum(row) != test_row:
            return 'Invalid' # if any rows dont match the square is invalid

    
    # vertical lines
    # to test the columns start by arranging a new matrix 
    # where the columns of the original are now the rows.
    column_matrix=[[] for i in range(entered_number)] 
    for i in matrix: # 
        for j, number in enumerate(i): 
            column_matrix[j].append(number)
    # test the rows and compare as before
    for i, row in enumerate(column_matrix):
        if sum(row) != test_row:
            return 'Invalid'

        
    # diagonal lines
    diagonal_1 = 0 # sum of diagonal line left to right
    diagonal_2 = 0 # sum of diagonal line right to left
    for i in range(entered_number):
        diagonal_1 = diagonal_1 + matrix[i][i]
        diagonal_2 = diagonal_2 + matrix[i][-(i+1)]
     # if either sum does not match the control the square is invalid
    if diagonal_1 != test_row:
        outcome = 'Invalid'
    if diagonal_2 != test_row:
        return 'Invalid'
    
    return 'Valid' # if all test match the control the square is valid


def main():
    even_number = True #even_number varible is True at launch

    while even_number:
        # request input from user and test for odd/even quality
        entered_number = input('Please enter an odd number: ')
        try:
            entered_number = int(entered_number)
            if entered_number % 2 == 0:
                print(f'{entered_number} is not odd.')
            else:
                even_number = False # if input = odd, accept input and end while loop.
        except ValueError:
            print(f'{entered_number} is not a number.')

    # pass entered_number through the magic_squares_solver and print results.
    print()
    print(f'Here is a {entered_number} x {entered_number} magic square:\n')
    matrix = magic_square_solver(entered_number)
    for lines in matrix:
        print(lines)
    print()
    print(f'This magic square appears to be {magic_square_validity(matrix, entered_number)}.')
    

#===== Program Start ===== 
if __name__=='__main__':
    main()