from typing import List, AnyStr


def check_row(desk: List[List[AnyStr]], row_ind: int, column_ind: int) -> List:
    for i in range(max(0, column_ind - 3), min(len(desk[row_ind]) - 3, column_ind + 1)):
        if all([char == 'R' for char in desk[row_ind][i:i + 4]]):
            return [True, 'R']
        elif all([char == 'Y' for char in desk[row_ind][i:i + 4]]):
            return [True, 'Y']
    return [False, 'E']


def check_column(desk: List[List[AnyStr]], row_ind: int, column_ind: int) -> List:
    for i in range(max(0, row_ind - 3), min(len(desk) - 3, row_ind + 1)):
        subcolumn = [desk[j][column_ind] for j in range(i, i + 4)]
        if all([char == 'R' for char in subcolumn]):
            return [True, 'R']
        elif all([char == 'Y' for char in subcolumn]):
            return [True, 'Y']
    return [False, 'E']


def check_lower_diag(desk: List[List[AnyStr]], row_ind: int, column_ind: int) -> List:
    for i in range(3, -1, -1):
        try:
            subdiag = [desk[row_ind - i + j][column_ind - i + j] for j in range(4) if
                       0 <= row_ind - i + j < len(desk) and 0 <= column_ind - i + j < len(desk[0])]
            if len(subdiag) != 4:
                continue
            if all([char == 'R' for char in subdiag]):
                return [True, 'R']
            elif all([char == 'Y' for char in subdiag]):
                return [True, 'Y']
        except IndexError:
            continue
    return [False, 'E']


def check_upper_diag(desk: List[List[AnyStr]], row_ind: int, column_ind: int) -> List:
    for i in range(3, -1, -1):
        try:
            subdiag = [desk[row_ind + i - j][column_ind - i + j] for j in range(4) if
                       0 <= row_ind + i - j < len(desk) and 0 <= column_ind - i + j < len(desk[0])]
            if len(subdiag) != 4:
                continue
            if all([char == 'R' for char in subdiag]):
                return [True, 'R']
            elif all([char == 'Y' for char in subdiag]):
                return [True, 'Y']
        except IndexError:
            continue
    return [False, 'E']


def check_victory(desk: List[List[AnyStr]], row_ind: int, column_ind: int) -> List:
    ans = check_row(desk, row_ind, column_ind)
    if ans[0]:
        return ans + ['by row']
    ans = check_column(desk, row_ind, column_ind)
    if ans[0]:
        return ans + ['by column']
    ans = check_upper_diag(desk, row_ind, column_ind)
    if ans[0]:
        return ans + ['by upper diag']
    ans = check_lower_diag(desk, row_ind, column_ind)
    if ans[0]:
        return ans + ['by lower diag']
    return [False, 'E', 'continue game']
