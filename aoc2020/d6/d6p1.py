def main():
    with open("d6/d6.txt", "r") as f:
        lines = f.read()

    groups = [set(group.replace("\n", "")) for group in lines.split("\n\n")]
    print(sum(len(g) for g in groups))


if __name__ == "__main__":
    main()
