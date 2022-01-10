def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum_tlbr = 0
    for i in range(len(matrix)):
        sum_tlbr += matrix[i][i]

    sum_brtl = 0
    for i in range(len(matrix)):
        print(matrix[-(i + 1)][-(i + 1)])
        sum_brtl += matrix[i][-(i + 1)]

    total_diagonal_sum = sum_brtl + sum_tlbr
    print(total_diagonal_sum)



m1 = [[1, 2], [30, 40], ]
sum_up_diagonals(m1)
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_up_diagonals(m2)
