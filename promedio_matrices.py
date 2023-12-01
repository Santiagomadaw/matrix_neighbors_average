from functools import reduce


def neighbors_average(matrix:list[list[float]], indexx:int, indexy:int):
    '''Calcula el promedio de cada elemento con sus adyacentes.'''
    
    startx, endx = max(indexy - 1, 0), min(indexy+2, len(matrix[indexx]))
    starty, endy = max(indexx - 1, 0), min(indexx+2, len(matrix))
    
    #Lista de elementos adyacentes fila incluido elemento
    elements = matrix[indexx][startx:endx]
    
    #Lista de elementos adyacentes columna incluido elemento
    elements += list(map(lambda i: matrix[i][indexy],range(starty, endy )))
    
    # Al estar el elemento matrix[indexx][indexy] repetido por estar en las 2 listas elimino 1
    elements.remove(matrix[indexx][indexy])
        
    return round(reduce(lambda accum, n: accum + n, elements)/len(elements), 2)


def new_row(indexx:int, matrix:list[list[float]]):
    '''Devuelve una lista con los promedios de cada elemento en una fila.'''
    
    # Monta los elementos que le devuelve 'neighbors_average' en una lista
    return list(map(lambda indexy:
      neighbors_average(matrix, indexx, indexy),
      range(len(matrix[indexx]))))


def matrix_average(matrix:list[list[float]]):
    '''Devuelve una matriz con los promedios de cada elemento y sus adyacentes.'''
    
    # Monta las listas que le devuelve 'new_row' en una matriz
    return list(map(lambda indexx:
      new_row(indexx, matrix),
      range(len(matrix))))


print(matrix_average([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))