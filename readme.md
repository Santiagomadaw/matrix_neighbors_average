
## Práctica con Listas en Python

Este proyecto presenta una implementación en Python de una función que realiza el promedio de un elemento y sus vecinos en una matriz bidimensional.

### Funciones Principales

#### `neighbors_average(matrix, index_x, index_y)`

Esta función toma una matriz y las coordenadas de un elemento en la posición `(index_x, index_y)`. Calcula el promedio entre el valor de este elemento y los valores de sus vecinos (arriba, abajo, izquierda, derecha) en la matriz. El resultado se redondea a dos decimales.

#### `new_row(index_x, matrix)`

Genera una nueva fila para la matriz de salida, aplicando la función `neighbors_average` a cada elemento de la fila en la posición `index_x` de la matriz de entrada.

#### `matrix_average(matrix)`

Aplica la función `new_row` a cada fila de la matriz de entrada, generando así la matriz de salida completa con los promedios de cada elemento y sus vecinos.

### Ejemplo de Uso

```python

# Definir una matriz de ejemplo

matriz_entrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
# Calcular la matriz de promedios
matriz_resultado = matrix_average(matriz_entrada)

# Mostrar los resultados
print("Matriz de Entrada:")
print(matriz_entrada)
print("Matriz de Promedios:")
print(matriz_resultado)

### Detalles de Implementación

- La función `neighbors_average` utiliza funciones internas para verificar si un índice no es el primero o el último en su dimensión respectiva.
- Se emplea la función `map` para aplicar las funciones de promedio a cada fila y elemento de la matriz.

### Contribuciones

¡Se agradecen las contribuciones! Si encuentras formas de mejorar el código, corregir errores o agregar nuevas características, no dudes en contribuir al proyecto.

### Requisitos

- Python 3.x
- No se requieren bibliotecas externas

### Licencia

Este proyecto está bajo la licencia [Licencia MIT](LICENSE).

## Practice with Lists in Python

This project introduces a Python implementation of a function that computes the average of an element and its neighbors in a two-dimensional matrix.

### Main Functions

#### `neighbors_average(matrix, index_x, index_y)`

This function takes a matrix and the coordinates of an element at position `(index_x, index_y)`. It calculates the average between the value of this element and the values of its neighbors (above, below, left, right) in the matrix. The result is rounded to two decimals.

#### `new_row(index_x, matrix)`

Generates a new row for the output matrix by applying the `neighbors_average` function to each element in the row at position `index_x` of the input matrix.

#### `matrix_average(matrix)`

Applies the `new_row` function to each row of the input matrix, generating the complete output matrix with averages for each element and its neighbors.

### Usage Example

```python
# Define an example matrix
matrix_input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
# Calculate the matrix of averages
matrix_result = matrix_average(matrix_input)

# Display the results
print("Input Matrix:")
print(matrix_input)
print("Matrix of Averages:")
print(matrix_result)

### Implementation Details

- The `neighbors_average` function utilizes internal functions to check whether an index is not the first or last in its respective dimension.
- The `map` function is utilized to apply the averaging functions to each row and element of the matrix.

### Contributions

Contributions are appreciated! If you find ways to improve the code, fix errors, or add new features, feel free to contribute to the project.

### Requirements

- Python 3.x
- No external libraries are required

### License

This project is under the MIT License.