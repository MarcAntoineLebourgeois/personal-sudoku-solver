def find_missing_numbers(input_list):
    all_numbers = set(range(1, 10))
    input_set = set(input_list)
    missing_numbers = sorted(all_numbers - input_set)
    return missing_numbers