def get_neighbors(matrix: list[list[int]], rowNumber: int, colNumber: int) -> list[(int, (int, int))]:
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix) - 1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix[0]) - 1:
                    if newCol != colNumber or newRow != rowNumber:
                        result.append((matrix[newRow][newCol], (newRow, newCol)))

    return result
