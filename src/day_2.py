from settings import DATA_DIR

MAPPTING = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

MAPPTING_2 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": 0,
    "Y": 3,
    "Z": 6,
}

POINTS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

OUTCOMES = {
    ("rock", "rock"): 3,
    ("rock", "paper"): 0,
    ("rock", "scissors"): 6,
    ("paper", "rock"): 6,
    ("paper", "paper"): 3,
    ("paper", "scissors"): 0,
    ("scissors", "rock"): 0,
    ("scissors", "paper"): 6,
    ("scissors", "scissors"): 3,
}


def day_2():
    with open(DATA_DIR / "day_2.txt") as f:
        lines = f.read().splitlines()

    score = 0
    for line in lines:
        opponent, me = map(MAPPTING.get, line.split(" "))
        score += OUTCOMES[(me, opponent)] + POINTS[me]

    print(f"Part 1: {score}")

    score_2 = 0
    for line in lines:
        opponent, expected_result = map(MAPPTING_2.get, line.split(" "))
        me = [
            m
            for ((m, o), r) in OUTCOMES.items()
            if o == opponent and r == expected_result
        ][0]

        score_2 += OUTCOMES[(me, opponent)] + POINTS[me]

    print(f"Part 2: {score_2}")


if __name__ == "__main__":
    day_2()
