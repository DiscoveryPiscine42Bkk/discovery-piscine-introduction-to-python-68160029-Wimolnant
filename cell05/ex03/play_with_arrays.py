try:
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    processed_list_with_duplicates = []
    for number in original_array:
        if number > 5:
            new_value = number + 2
            processed_list_with_duplicates.append(new_value)
    unique_values_set = set(processed_list_with_duplicates)
    new_array_unique = list(unique_values_set)
    print(original_array)
    output_string = " " + ", ".join(map(str, new_array_unique))
    print(output_string)

except Exception:
    pass