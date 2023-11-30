
def neighbors_average(matrix,indexx,indexy):  
  sum, amount = 0 , 0
  last = len(matrix)-1
  
  def isnt_first(index): return index > 0
  def isnt_last(index):  return index < last
  
  if isnt_first(indexx):
    sum = sum + matrix[indexx][indexy-1]
    amount += 1
  if isnt_last(indexy):
    sum = sum + matrix[indexx][indexy+1]
    amount += 1
  if isnt_first(indexx):
    sum = sum + matrix[indexx-1][indexy]
    amount += 1
  if isnt_last(indexx):
    sum = sum + matrix[indexx+1][indexy]
    amount += 1
  
  return round((matrix[indexx][indexy] + sum )/(amount + 1),2)


def new_row(indexx, matrix):
  return list(map(lambda  indexy: neighbors_average(matrix, indexx, indexy),
                                  range (len(matrix[indexx]))))
  
def matrix_average( matrix):  
  return list(map(lambda indexx:  new_row(indexx, matrix),
                                  range(len(matrix))))
  

print(matrix_average([[0,1,1,1],[1,2,2,1],[1,2,2,1]]))
