from settings import DATA_DIR


def day_1():
    elves = []

    with open(DATA_DIR / "day_1.txt") as f:
        lines = f.read().splitlines()

    curr_sum = 0
    for line in lines:
        if line:
            curr_sum += int(line)
        else:
            elves.append(curr_sum)
            curr_sum = 0

    print(f"Part 1: {max(elves)}")
    print(f"Part 2: {sum(sorted(elves, reverse=True)[:3])}")


if __name__ == "__main__":
    day_1()
