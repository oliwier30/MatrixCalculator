import numpy as np
import pandas as pd
import sys


def main():
    matrix = create_matrix()
    operation = choose_operation()
    result = calculate(matrix, operation)
    print_result(result)

    yes = ["yes", "y", "ye"]
    while True:
        if isinstance(result, np.ndarray) and input("Continue with the new matrix (Y/n)? ").strip().lower() in yes:
            operation = choose_operation()
            result = calculate(result, operation)
            print_result(result)
        else:
            sys.exit()


def create_matrix():
    try:
        rows = int(input("Rows: "))
        if rows <= 0:
            rows = 1
        print("Enter rows, separate numbers with spaces:")
        array = []

        # creating a 2-dimensional array
        for _ in range(rows):
            array_inner = input().strip().split()
            for i in range(len(array_inner)):
                array_inner[i] = float(array_inner[i])
            array.append(array_inner)

        array = np.array(array)
        return array
    except ValueError:
        sys.exit("\nPlease provide valid data.\n")


def print_result(m):
    try:
        frame = pd.DataFrame(m)
        def fmt(value):
            return str(int(value)) if value.is_integer() else str(round(value, 10))

        print(f"\n{frame.to_string(header=False, index=False, float_format=fmt)}\n")
    except ValueError:
        print(f"\n{m}\n") # prints determinant


def choose_operation():
    print("""
    Choose operation.
    add: Add
    sub: Subtract
    mpy: Multiply two matrices
    mpy X: Multiply by X (number)
    pow X: Power of X (integer)
    trs: Transpose
    inv: Inverse
    det: Determinant
    """)
    operation = input().strip().lower()
    return operation


def calculate(matrix, operation):
    try:
        match operation:
            case "add":
                matrix2 = create_matrix()
                return np.add(matrix, matrix2)
            case "sub":
                matrix2 = create_matrix()
                return np.subtract(matrix, matrix2)
            case "mpy":
                matrix2 = create_matrix()
                return np.matmul(matrix, matrix2)
            case "trs":
                return np.matrix.transpose(matrix)
            case "inv":
                try:
                    return np.linalg.inv(matrix)
                except np.linalg.LinAlgError:
                    sys.exit("\nDeterminant is 0. Inverse does not exist.\n")
            case "det":
                try:
                    return round(np.linalg.det(matrix), 10)
                except np.linalg.LinAlgError:
                    sys.exit("\nThe row and column size need to be the same.\n")
            case _:
                match operation.split():
                    case ["mpy", x]:
                        return np.multiply(matrix, float(x))
                    case ["pow", x]:
                        return powfix(matrix, int(x))
                    case _:
                        sys.exit("\nInvalid operation.\n")
    except ValueError:
        sys.exit("\nPlease provide valid data.\n")


def powfix(matrix, x):
    try:
        if matrix.shape[0] != matrix.shape[1]:
            sys.exit("\nThe row and column size need to be the same.\n")
        return np.linalg.matrix_power(matrix, x)
    except np.linalg.LinAlgError:
        sys.exit("\nMatrix is singular. Cannot invert for negative powers.\n")


if __name__ == "__main__":
    main()
