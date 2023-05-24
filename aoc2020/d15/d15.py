def play(starting_numbers, target_turn):
    last_turns = {v: i + 1 for i, v in enumerate(starting_numbers[:-1])}  # num: turn

    last_num = starting_numbers[-1]
    turn = len(starting_numbers)

    while turn < target_turn:
        if last_num not in last_turns:
            cur_num = 0
        else:
            cur_num = turn - last_turns[last_num]
        last_turns[last_num] = turn
        last_num = cur_num
        turn += 1

    return f"{starting_numbers} - {target_turn}: {last_num}"


if __name__ == "__main__":
    target_turn = 30_000_000
    starting_numbers = [9, 19, 1, 6, 0, 5, 4]
    print(play(starting_numbers, target_turn))
