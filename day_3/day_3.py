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


@dataclass
class ElfGroup:
    rucksacks: dict[Rucksack]

    def add_rucksack(self, rucksack: Rucksack):
        number_of_keys = len(self.rucksacks)
        self.rucksacks[f'rucksack_{number_of_keys}'] = rucksack

    def find_repeated_items(self):
        # separate out values of dictionary into separate lists
        rucksack_0 = self.rucksacks['rucksack_0']
        rucksack_1 = self.rucksacks['rucksack_1']
        rucksack_2 = self.rucksacks['rucksack_2']

        repeated_items = []
        for item in rucksack_0.full_content:
            if item in rucksack_1.full_content and item in rucksack_2.full_content:
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


def part_2():
    priority = 0
    with open('input.txt') as f:
        for index, line in enumerate(f.read().splitlines()):
            letters = list(line)
            if index % 3 == 0:
                rucksack_group = ElfGroup(rucksacks={})
            rucksack = Rucksack(full_content=letters)
            rucksack_group.add_rucksack(rucksack)
            if index % 3 == 2:
                priority_mapping = PriorityMapping()
                badge = rucksack_group.find_repeated_items()
                priority += priority_mapping.get_priority(badge[0])

    print(f"Part 2: {priority}")


if __name__ == "__main__":
    part_2()
