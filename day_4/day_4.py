from dataclasses import dataclass


def input_data(file_name: str):
    with open(file_name, "r") as f:
        return f.read().splitlines()


@dataclass
class CleaningID:
    start: int
    end: int

    def read_id(self, line: str):
        """Reads the ID from the line and returns the ID"""
        split_line = line.split("-")
        self.start = int(split_line[0])
        self.end = int(split_line[1])

    def create_full_list(self):
        """Creates a list of all possible IDs"""
        return list(range(self.start, self.end + 1))


@dataclass
class CleaningPair:
    cleaning_pair: dict[str, list[int]]

    def read_pair(self, line: str):
        """Reads the pair from the line and returns the pair"""
        split_line = line.split(",")
        cleaning_id1 = CleaningID(0, 0)
        cleaning_id2 = CleaningID(0, 0)
        cleaning_id1.read_id(split_line[0])
        cleaning_id2.read_id(split_line[1])
        self.cleaning_pair['ID_1'] = cleaning_id1
        self.cleaning_pair['ID_2'] = cleaning_id2

    def check_complete_overlap(self):
        """Function checks if one of the CleaningID is contained completely within the other one"""
        for key, value in self.cleaning_pair.items():
            if key == 'ID_1':
                if value.start >= self.cleaning_pair['ID_2'].start and value.end <= self.cleaning_pair['ID_2'].end:
                    return True
            if key == 'ID_2':
                if value.start >= self.cleaning_pair['ID_1'].start and value.end <= self.cleaning_pair['ID_1'].end:
                    return True

    def check_partial_overlap(self):
        """Function checks if one fo the CleaningID overlaps at all with the other one"""
        for key, value in self.cleaning_pair.items():
            if key == 'ID_1':
                if value.start <= self.cleaning_pair['ID_2'].start <= value.end:
                    return True
                if value.start <= self.cleaning_pair['ID_2'].end <= value.end:
                    return True
            if key == 'ID_2':
                if value.start <= self.cleaning_pair['ID_1'].start <= value.end:
                    return True
                if value.start <= self.cleaning_pair['ID_1'].end <= value.end:
                    return True


def part_1():
    """Function reads the input file and returns the number of valid pairs"""
    complete_overlap = 0
    for line in input_data("input.txt"):
        cleaning_pair = CleaningPair({})
        cleaning_pair.read_pair(line)
        if cleaning_pair.check_complete_overlap():
            complete_overlap += 1
    print(f"Number of complete overlaps: {complete_overlap}")


def part_2():
    overlap = 0
    for line in input_data("input.txt"):
        cleaning_pair = CleaningPair({})
        cleaning_pair.read_pair(line)
        if cleaning_pair.check_partial_overlap():
            overlap += 1
    print(f"Number of overlaps: {overlap}")


if __name__ == "__main__":
    part_1()
    part_2()
