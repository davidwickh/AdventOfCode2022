from dataclasses import dataclass


def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


@dataclass
class File:
    directory: str
    file_name: str
    size: int


@dataclass
class Directory:
    name: str
    parent_directory: str
    children_directories: list[str]
    files: list[File]
    file_sizes_in_directory: int = 0
    sub_directory_sizes: int = 0
    total_size: int = 0


class DirectorTree:
    """Class to represent a tree of directors and their children"""

    def __init__(self, root_directory: Directory):
        self.current_directory = root_directory
        self.directory_tree = {root_directory.name: root_directory}

    def add_child_directory(self, child: Directory):
        if child.name in self.directory_tree:
            self.navigate_to_directory(child)
            return
        else:
            self.directory_tree[child.name] = child
            self.current_directory = child

    def add_file_to_current_directory(self, file: File):
        self.current_directory.files.append(file)

    def navigate_to_directory(self, directory: Directory):
        if self.current_directory == directory:
            return
        self.current_directory = self.directory_tree[directory.name]


def user_command(input_command: str, directory_tree: DirectorTree):
    command = input_command[2:]
    if input_command.__contains__("ls"):
        return

    if input_command.__contains__("cd"):
        command = command.split(" ")
        if command[1] == "..":
            directory_tree.navigate_to_directory(directory_tree.current_directory.parent_directory)
        else:
            new_directory = Directory(command[1], directory_tree.current_directory, [], [])
            directory_tree.add_child_directory(new_directory)


def computer_response(output: str, directory_tree: DirectorTree):
    # if output starts with dir then it is a directory
    if output.startswith("dir"):
        output = output.split(" ")
        directory = Directory(output[1], directory_tree.current_directory, [], [])
        directory_tree.add_child_directory(directory)

    else:
        output = output.split(" ")
        file = File(directory_tree.current_directory, output[1], int(output[0]))
        directory_tree.add_file_to_current_directory(file)


def add_file_sizes_to_directories(directory_tree):
    """Function finds the file sizes within each directory and adds them to the directory size attribute"""
    for directory_name, directory in directory_tree.directory_tree.items():
        total_file_size = 0
        for file in directory.files:
            total_file_size += file.size
            directory.file_sizes_in_directory = total_file_size


def calculate_total_size(directory_tree):
    """Function handles calculating the size of subdirectories and total size of each directory, making sure to not double count"""
    for directory_name, directory in directory_tree.directory_tree.items():
        if directory.parent_directory is not None:
            directory.parent_directory.sub_directory_sizes += directory.total_size
        directory.total_size = directory.file_sizes_in_directory + directory.sub_directory_sizes


def find_all_directories_with_size(directory_tree, operator, size):
    """Function finds all directories that have a size that is less than or equal to the size given"""
    largest_directories = {}
    for directory_name, directory in directory_tree.directory_tree.items():
        if operator == "le":
            if directory.total_size <= size:
                largest_directories[directory_name] = directory.total_size
        elif operator == "ge":
            if directory.total_size >= size:
                largest_directories[directory_name] = directory.total_size
    return largest_directories


def part_1():
    command_list = read_input()
    root_directory = Directory("root", None, [], [])
    directory_tree = DirectorTree(root_directory)

    for command in command_list:
        if command.startswith("$"):
            user_command(command, directory_tree=directory_tree)
        else:
            computer_response(command, directory_tree)

    add_file_sizes_to_directories(directory_tree)

    calculate_total_size(directory_tree)

    largest_directories = find_all_directories_with_size(directory_tree, "le", 1000000)

    total_size = 0
    for directory_name, directory_size in largest_directories.items():
        print(f"{directory_name} has a size of {directory_size}")
        total_size += directory_size
    print(f"The total size of all directories is {total_size}")
def part_2():
    pass


if __name__ == "__main__":
    part_1()
    part_2()
