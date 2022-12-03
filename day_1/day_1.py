def find_max_calories(elves):
    """
    Finds the maximum number of calories in the dictionary of elves
    :param elves: (dict)
        Dictionary of elves and their calorie count
    :return: (int)
        Maximum number of calories
    """
    return max(elves.values())


def process_data(data):
    """
    Handles processing of data from file by reading into a dictionary, where the key is the elf and the value is the
    number of calories they are carrying.
    :param data: (str)
        String of data from file

    :return: (dict)
        Dictionary of elves and their calorie count
    """
    processed_data = {}
    elf_number = 1
    for line in data.splitlines():
        if line:
            if f'elf_{elf_number}' not in processed_data:
                processed_data[f'elf_{elf_number}'] = int(line)
            else:
                processed_data[f'elf_{elf_number}'] += int(line)
        else:
            elf_number += 1
            processed_data[f'elf_{elf_number}'] = 0

    return processed_data


def read_in_data(input_file):
    """
    Reads in data from file and returns it as
    :param input_file:
    :return: (dict)
        Dictionary of elves and their calorie count
    """
    with open(input_file, 'r') as f:
        processed_data = process_data(f.read())

    return processed_data


def part_1():
    elf_calories = read_in_data('input.txt')
    max_calories = find_max_calories(elf_calories)
    print(f'The maximum number of calories is {max_calories}')


def part_2():
    top_three_calories = []
    elf_calories = read_in_data('input.txt')
    for _ in range(3):
        max_calories = find_max_calories(elf_calories)
        top_three_calories.append(max_calories)
        del elf_calories[f'{list(elf_calories.keys())[list(elf_calories.values()).index(max_calories)]}']

    print(f'The top three elves have a combined calorie count of {sum(top_three_calories)}')


if __name__ == '__main__':
    part_1()
    part_2()
