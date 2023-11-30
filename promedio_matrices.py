from functools import reduce

def neighbors_average(matrix,indexx,indexy):
 
  elements=matrix[indexx][max(indexy-1,0):
  min(indexy+2, len(matrix[indexx]))] + [matrix[i][indexy] 
  for i in range(max(indexx - 1, 0), min(indexx + 2, len(matrix)))
  if matrix[i][indexy] != matrix[indexx][indexy]]
  return round(reduce(lambda accum, n : accum + n, elements )/len(elements),2)
  

def new_row(indexx, matrix):
  return list(map(lambda  indexy: neighbors_average(matrix,indexx,indexy),
                                  range (len(matrix[indexx]))))
  
def matrix_average( matrix):  
  return list(map(lambda indexx:  new_row(indexx, matrix),
                                  range(len(matrix))))
  

print(matrix_average([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))