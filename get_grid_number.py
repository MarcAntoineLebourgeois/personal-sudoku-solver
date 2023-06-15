
def get_grid_number(row, column):
    grid_row = row // 3  # Calcul de la rangée de la grille
    grid_column = column // 3  # Calcul de la colonne de la grille
    grid_number = grid_row * 3 + grid_column + 1  # Calcul du numéro de la grille
    if grid_row == 1:
        grid_number += 2
    elif grid_row == 2:
        grid_number -= 2
    return grid_number