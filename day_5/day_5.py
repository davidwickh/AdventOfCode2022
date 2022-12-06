import re


def read_input_file(file_name: str):
    """Function reads the input file and returns the list of lines"""
    with open(file_name, 'r') as file:
        return file.readlines()


class StackGenerator:
    """Class generates the stacks for the crane"""

    def __init__(self, raw_input_file):
        self.stack_configuration = []
        self.read_in_stack_configuration(raw_input_file)
        self.clean_stack_configuration(self.stack_configuration)
        self.stacks = []

    def read_in_stack_configuration(self, file):
        """Function reads in the stack configuration from the input file"""
        for line in file:
            if line == "\n":
                break
            self.stack_configuration.append(line.strip())
        return self.stack_configuration

    def clean_stack_configuration(self, stack_configuration: list[str]):
        """Function cleans the stack configuration by turning the 2D list into a dictionary with the stack number as the key"""
        # for each row split the row into a list of the individual characters and include empty spaces
        cleaned_stack_configuration = []
        for row_index, row in enumerate(stack_configuration):
            if row_index == len(stack_configuration) - 1:
                continue
            row_to_append = []
            for character_index, character in enumerate(row):
                if character_index % 4 == 1:
                    row_to_append.append(str(character))
            cleaned_stack_configuration.append(row_to_append)

        # rotate the list so that the stacks are in the correct order
        cleaned_stack_configuration = list(zip(*cleaned_stack_configuration[::-1]))

        # create a dictionary with the stack number as the key and the list of crates as the value
        self.stack_configuration = {}
        for stack_number, stack in enumerate(cleaned_stack_configuration):
            stack = [crate for crate in stack if crate != " "]
            self.stack_configuration[stack_number + 1] = stack


class Crane:
    def __init__(self, stack_configuration: dict, part: int = 1):
        """Function parses the moves from the input file"""
        self.stack_configuration = stack_configuration
        self.moves = []
        self.read_in_moves(read_input_file("input.txt"))
        self.parse_moves(part)

    def read_in_moves(self, file):
        """Function reads in the moves from the input file"""
        # get all the lines after the new line in the input file
        passed_stack_configuration = False
        for line in file:
            if line == "\n":
                passed_stack_configuration = True
                continue
            if passed_stack_configuration:
                self.moves.append(line.strip())
        return self.moves

    def parse_moves(self, part: int = 1):
        """Function parses the moves from the input file"""
        for move in self.moves:
            no_of_boxes, start_position, end_position = re.findall(r"\d+", move)

            if part == 1:
                self.move_crane_part_1(int(no_of_boxes), start_position, end_position)
            elif part == 2:
                self.move_crane_part_2(int(no_of_boxes), start_position, end_position)

    def move_crane_part_1(self, no_of_boxes: int, start_position: str, end_position: str):
        """Moves the box(es) from the starting position to the end position"""
        start_stack = self.stack_configuration[int(start_position)]
        end_stack = self.stack_configuration[int(end_position)]

        for _ in range(no_of_boxes):
            end_stack.append(start_stack.pop())

        self.stack_configuration[int(start_position)] = start_stack
        self.stack_configuration[int(end_position)] = end_stack

    def move_crane_part_2(self, no_of_boxes: int, start_position: str, end_position: str):
        """Moves the box(es) from the starting position to the end position. Making sure they keep the same order"""
        crates = self.stack_configuration[int(start_position)]
        crates_to_move = crates[-no_of_boxes:]

        self.stack_configuration[int(start_position)] = crates[:-no_of_boxes]
        self.stack_configuration[int(end_position)] += crates_to_move


def part_1():
    file = read_input_file("input.txt")
    stack_generator = StackGenerator(file)
    crane = Crane(stack_generator.stack_configuration)
    # print the last box in each stack
    print_message = ""
    for stack in crane.stack_configuration.values():
        print_message += stack[-1]

    print(print_message)

def part_2():
    file = read_input_file("input.txt")
    stack_generator = StackGenerator(file)
    crane = Crane(stack_generator.stack_configuration, part=2)
    # print the last box in each stack
    print_message = ""
    for stack in crane.stack_configuration.values():
        print_message += stack[-1]

    print(print_message)


if __name__ == "__main__":
    part_1()
    part_2()
