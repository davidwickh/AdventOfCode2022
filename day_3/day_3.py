from dataclasses import dataclass


@dataclass
class PriorityMapping:
    """
    Maps the letter to a priority number. a through to z have a priority of 1 through to 26. and A through to Z have a
    priority of 27 through to 52
    """

    @staticmethod
    def get_priority(letter: str):
        if letter.islower():
            return ord(letter) - 96
        elif letter.isupper():
            return ord(letter) - 38
        else:
            raise ValueError(f"Invalid letter {letter}")


@dataclass
class Rucksack:
    full_content: list[str]
    compartment_1: list[str] = None
    compartment_2: list[str] = None

    def split_rucksack_into_compartments(self):
        # find the middle index of
        middle_index = len(self.full_content) // 2
        self.compartment_1 = self.full_content[:middle_index]
        self.compartment_2 = self.full_content[middle_index:]

    def find_repeated_items(self):
        repeated_items = []
        for item in self.compartment_1:
            if item in self.compartment_2:
                repeated_items.append(item)
        return repeated_items


def part_1():
    priority = 0
    with open('input.txt') as f:
        for line in f.read().splitlines():
            letters = list(line)
            rucksack = Rucksack(full_content=letters)
            priority_mapping = PriorityMapping()
            rucksack.split_rucksack_into_compartments()
            repeated_items = rucksack.find_repeated_items()
            priority += priority_mapping.get_priority(repeated_items[0])

    print(f"Part 1: {priority}")


if __name__ == "__main__":
    part_1()
