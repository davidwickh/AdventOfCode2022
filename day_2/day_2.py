from dataclasses import dataclass


@dataclass
class ShapeCodeMappingOpponent:
    rock: str = "A"
    paper: str = "B"
    scissor: str = "C"

    def get_shape_played(self, code: str):
        if code == self.rock:
            return "rock"
        elif code == self.paper:
            return "paper"
        elif code == self.scissor:
            return "scissor"
        else:
            raise ValueError(f"Invalid code {code}")


@dataclass
class ShapeCodeMappingPlayer:
    rock: str = "X"
    paper: str = "Y"
    scissor: str = "Z"

    def get_shape_played(self, code: str):
        if code == self.rock:
            return "rock"
        elif code == self.paper:
            return "paper"
        elif code == self.scissor:
            return "scissor"
        else:
            raise ValueError(f"Invalid code {code}")


def get_play(opponent_play, outcome):
    """
    Handles calculating what the player should play based on what the opponent plays and the desired outcome
    :param opponent_play:
    :param outcome:
    :return:
    """
    if outcome == "win":
        if opponent_play == "rock":
            return "paper"
        elif opponent_play == "paper":
            return "scissor"
        elif opponent_play == "scissor":
            return "rock"
    elif outcome == "lose":
        if opponent_play == "rock":
            return "scissor"
        elif opponent_play == "paper":
            return "rock"
        elif opponent_play == "scissor":
            return "paper"
    elif outcome == "draw":
        return opponent_play
    else:
        raise ValueError(f"Invalid outcome {outcome}")


@dataclass
class OutcomeMapping:
    lose: str = "X"
    draw: str = "Y"
    win: str = "Z"

    def get_outcome(self, code: str):
        if code == self.lose:
            return "lose"
        elif code == self.draw:
            return "draw"
        elif code == self.win:
            return "win"
        else:
            raise ValueError(f"Invalid code {code}")


@dataclass
class ScoreCalculator:
    player_score: int = 0
    rock: int = 1
    paper: int = 2
    scissor: int = 3

    def win(self, selected_shape):
        self.player_score += self.__getattribute__(selected_shape)
        self.player_score += 6

    def draw(self, selected_shape):
        self.player_score += self.__getattribute__(selected_shape)
        self.player_score += 3

    def lose(self, selected_shape):
        self.player_score += self.__getattribute__(selected_shape)
        self.player_score += 0

    def process_game(self, player_shape, opponent_shape):
        if player_shape == opponent_shape:
            self.draw(player_shape)
        elif player_shape == "rock" and opponent_shape == "scissor":
            self.win(player_shape)
        elif player_shape == "rock" and opponent_shape == "paper":
            self.lose(player_shape)
        elif player_shape == "paper" and opponent_shape == "rock":
            self.win(player_shape)
        elif player_shape == "paper" and opponent_shape == "scissor":
            self.lose(player_shape)
        elif player_shape == "scissor" and opponent_shape == "paper":
            self.win(player_shape)
        elif player_shape == "scissor" and opponent_shape == "rock":
            self.lose(player_shape)
        else:
            raise ValueError(f"Invalid shapes {player_shape} {opponent_shape}")


def read_input_part_1(opponent_mapping, player_mapping) -> dict[str, list[str]]:
    """
    Handles the reading in and parsing of the input file
    :return: (dict)
        dictionary of turns
    """
    turns = {"player": [], 'opponent': []}
    with open("input.txt") as f:
        for line in f.read().splitlines():
            opponent, player = line.split()
            turns['opponent'].append(opponent_mapping.get_shape_played(opponent))
            turns['player'].append(player_mapping.get_shape_played(player))

    return turns


def read_input_part_2(opponent_mapping, outcome_mapping) -> dict[str, list[str]]:
    """
    Handles the reading in and parsing of the input file
    :return: (dict)
        dictionary of turns
    """
    turns = {"player": [], 'opponent': []}
    with open("input.txt") as f:
        for line in f.read().splitlines():
            opponent, outcome = line.split()
            opponent_shape = opponent_mapping.get_shape_played(opponent)
            outcome = outcome_mapping.get_outcome(outcome)
            player_shape = get_play(opponent_shape, outcome)

            turns['opponent'].append(opponent_shape)
            turns['player'].append(player_shape)

    return turns


def part_1():
    shape_code_mapping_opponent = ShapeCodeMappingOpponent()
    shape_code_mapping_player = ShapeCodeMappingPlayer()
    score_calculator = ScoreCalculator()
    turns = read_input_part_1(shape_code_mapping_opponent, shape_code_mapping_player)
    for player_shape, opponent_shape in zip(turns['player'], turns['opponent']):
        score_calculator.process_game(player_shape, opponent_shape)

    print(f'Part 1 ans: {score_calculator.player_score}')


def part_2():
    shape_code_mapping_opponent = ShapeCodeMappingOpponent()
    outcome_mapping = OutcomeMapping()
    score_calculator = ScoreCalculator()
    turns = read_input_part_2(shape_code_mapping_opponent, outcome_mapping)
    for player_shape, opponent_shape in zip(turns['player'], turns['opponent']):
        score_calculator.process_game(player_shape, opponent_shape)

    print(f'Part 2 ans: {score_calculator.player_score}')


if __name__ == "__main__":
    part_1()
    part_2()
