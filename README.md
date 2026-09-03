# Matrix Calculator
#### Description:
A command-line matrix calculator built with NumPy.

## Usage

This program allows you to input and calculate a matrix with a specified amount of rows.

Run the program with `python calculator.py`.

Once you enter the amount of rows, you will be asked to input each row. Separate each number in a single row with a space. Press enter once you've typed all the numbers in a row.

You are allowed to input integers or decimals as values.

    Rows: 3
    Enter rows, separate numbers with spaces:
    7 3 0
    7 2 6
    9 2 5

After creating the matrix, you may choose an operation.

    Choose operation.
    add: Add two matrices together.
    sub: Subtract two matrices together.
    mpy: Multiply two matrices together.
    mpy X: Multiply each element of a matrix by a constant.
    pow X: Raise the matrix to an integer power.
    trs: Filp the rows and columns of a matrix.
    inv: Find the inverse of a matrix.
    det: Find the determinant of a matrix.

Operations `add`, `sub`, `mpy` prompt the user for a second matrix to calculate.

Example 1:

    add

    Rows: 3
    Enter rows, separate numbers with spaces:
    5 6 1
    0 1 8
    8 8 5

    12  9  1
     7  3 14
    17 10 10

Example 2:

    mpy 3

    21 9  0
    21 6 18
    27 6 15

Example 3:

    trs

    7 7 9
    3 2 2
    0 6 5

Example 4:

    det

    43.0

If the program is unable to calculate, you will be given an error message. For instance, if the matrix is missing a number or the number count is not the same in all rows, you will see:

    Please provide valid data.

After calculation, you may choose to either end the program or continue with the resulting matrix. If you choose to continue, you will be asked to choose the operation again.

    Continue with the new matrix (Y/n)? yes

    Choose operation.
    ...

### Requirements

Check `requirements.txt`
