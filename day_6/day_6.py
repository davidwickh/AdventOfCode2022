def read_input(file_name: str) -> list[str]:
    """Function reads the input file and returns the data in a 1D list"""
    with open(file_name, "r") as file:
        return list(file.read().strip())


def check_for_marker(characters: list[str], no_of_unique_characters: int) -> bool:
    """Function checks if the characters contain a marker where all no_of_unique_characters characters are all unique,
    if so it returns True, else it returns False"""
    assert len(characters) == no_of_unique_characters, "The list of characters must be 4 characters long"
    if len(set(characters)) == no_of_unique_characters:
        return True
    return False


def part_1():
    raw_data = read_input("input.txt")
    marker_number_of_characters = 4
    for index, character in enumerate(raw_data):
        if check_for_marker(raw_data[index:index + marker_number_of_characters],
                            no_of_unique_characters=marker_number_of_characters):
            print(
                f"Part 2: The start of message marker is {character} with index {index + marker_number_of_characters}")
            break


def part_2():
    raw_data = read_input("input.txt")
    marker_number_of_characters = 14
    for index, character in enumerate(raw_data):
        if check_for_marker(raw_data[index:index + marker_number_of_characters],
                            no_of_unique_characters=marker_number_of_characters):
            print(f"Part 2: The start of message marker is {character} with index {index + marker_number_of_characters}")
            break


if __name__ == "__main__":
    part_1()
    part_2()
