def get_first_vertical_adjacent_grid(grid_number):
    if grid_number < 1 or grid_number > 9:
        raise ValueError("Invalid grid number. Grid number should be between 1 and 9.")
    if grid_number == 1:
        return 4
    elif grid_number == 2:
        return 5
    elif grid_number == 3:
        return 6
    elif grid_number == 4:
        return 1
    elif grid_number == 5:
        return 2
    elif grid_number == 6:
        return 3
    elif grid_number == 7:
        return 1
    elif grid_number == 8:
        return 2
    elif grid_number == 9:
        return 3

def get_second_vertical_adjacent_grid(grid_number):
    if grid_number < 1 or grid_number > 9:
        raise ValueError("Invalid grid number. Grid number should be between 1 and 9.")
    if grid_number == 1:
        return 7
    elif grid_number == 2:
        return 8
    elif grid_number == 3:
        return 9
    elif grid_number == 4:
        return 7
    elif grid_number == 5:
        return 8
    elif grid_number == 6:
        return 9
    elif grid_number == 7:
        return 4
    elif grid_number == 8:
        return 5
    elif grid_number == 9:
        return 6

def get_first_horizontal_adjacent_grid(grid_number):
    if grid_number < 1 or grid_number > 9:
        raise ValueError("Invalid grid number. Grid number should be between 1 and 9.")
    if grid_number == 1:
        return 2
    elif grid_number == 2:
        return 1
    elif grid_number == 3:
        return 1
    elif grid_number == 4:
        return 5
    elif grid_number == 5:
        return 4
    elif grid_number == 6:
        return 4
    elif grid_number == 7:
        return 8
    elif grid_number == 8:
        return 7
    elif grid_number == 9:
        return 7

def get_second_horizontal_adjacent_grid(grid_number):
    if grid_number < 1 or grid_number > 9:
        raise ValueError("Invalid grid number. Grid number should be between 1 and 9.")
    if grid_number == 1:
        return 3
    elif grid_number == 2:
        return 3
    elif grid_number == 3:
        return 2
    elif grid_number == 4:
        return 6
    elif grid_number == 5:
        return 6
    elif grid_number == 6:
        return 5
    elif grid_number == 7:
        return 9
    elif grid_number == 8:
        return 9
    elif grid_number == 9:
        return 8