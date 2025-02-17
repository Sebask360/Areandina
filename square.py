from itertools import product
import numpy as np

def is_magic_square(grid, target_sum=0):
    """Verifica si la cuadrícula es un cuadrado mágico con la suma dada."""
    size = len(grid)
    grid = np.array(grid)
    
    # Sumar filas y columnas
    for i in range(size):
        if sum(grid[i, :]) != target_sum or sum(grid[:, i]) != target_sum:
            return False
    
    # Sumar diagonales
    if sum(grid.diagonal()) != target_sum or sum(np.fliplr(grid).diagonal()) != target_sum:
        return False
    
    return True

def solve_magic_square(grid, target_sum=0):
    """Intenta encontrar una solución para el cuadrado mágico dado."""
    size = len(grid)
    empty_positions = [(i, j) for i in range(size) for j in range(size) if grid[i][j] is None]
    
    # Rango de números permitidos (ajustable según reglas)
    possible_numbers = list(range(-10, 11))  # Números de prueba entre -10 y 10, puedes cambiar el rango
    
    for values in product(possible_numbers, repeat=len(empty_positions)):
        for (i, j), val in zip(empty_positions, values):
            grid[i][j] = val
        
        if is_magic_square(grid, target_sum):
            return grid  # Retorna la primera solución encontrada
    
    return None  # No se encontró solución

# Ejemplo de uso
initial_grid = [
    [None, None, 3],
    [None, 4, None],
    [-7, None, None]
]

solution = solve_magic_square(initial_grid, target_sum=0)
if solution:
    print("Cuadrado mágico encontrado:")
    for row in solution:
        print(row)
else:
    print("No se encontró solución.")
