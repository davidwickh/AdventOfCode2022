def read_input(file_name: str) -> list[str]:
    """Function reads the input file and returns the data in a 1D list"""
    with open(file_name, "r") as file:
        return list(file.read().strip())


def check_for_marker(characters: list[str]) -> bool:
    """Function checks if the characters contain a marker where all 4 characters are all unique, if so it returns True,
    else it returns False"""
    assert len(characters) == 4, "The list of characters must be 4 characters long"
    if len(set(characters)) == 4:
        return True
    return False


def part_1():
    raw_data = read_input("input.txt")
    for index, character in enumerate(raw_data):
        if check_for_marker(raw_data[index:index + 4]):
            print(f"The marker is {character} with index {index + 4}")
            break


def part_2():
    pass


if __name__ == "__main__":
    part_1()
    part_2()
