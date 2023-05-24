from functools import reduce


def main():
    with open("d6/d6.txt", "r") as f:
        lines = f.read()

    all_answer = []
    for group in lines.split("\n\n"):
        group_answers = [set(answers) for answers in group.strip().split("\n")]
        valid_answers = reduce(lambda x, y: x & y, group_answers)
        all_answer.append(valid_answers)

    print(sum(len(g) for g in all_answer))


if __name__ == "__main__":
    main()
