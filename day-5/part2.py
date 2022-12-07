def generate_stacks() -> dict:
    stacks_dict = dict()
    num_of_stacks = 0

    with open('input.txt', 'r') as f:
        line = f.readline()
        num_of_stacks = int(len(line) / 4)

    for i in range(1, num_of_stacks + 1):
        stacks_dict[i] = []

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line[1] == '1':
                break
            
            line_norm = line[:-1]
            line_arr = list(line_norm)

            for index, char in enumerate(line_arr):
                if (index - 1) % 4 == 0 and char != ' ':
                    stacks_dict[((index - 1) / 4) + 1].insert(0, char)
            
    return stacks_dict


def sort_stacks(stacks: dict) -> dict:
    sorted_stacks = stacks.copy()

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line[0:4] == 'move':
                line_arr = line[:-1].split(' ')
                num_crates_to_move = int(line_arr[1])
                stack_from = int(line_arr[3])
                stack_to = int(line_arr[5])

                list_crates_to_move = sorted_stacks[stack_from][-num_crates_to_move:]
                del sorted_stacks[stack_from][-num_crates_to_move:]
                sorted_stacks[stack_to] += (list_crates_to_move)

    return sorted_stacks


def main() -> None:
    sorted_stacks = sort_stacks(generate_stacks())
    final_msg = ''

    for stack in sorted_stacks:
        top_crate = sorted_stacks[stack].pop()
        final_msg += top_crate

    print('Final Message:', final_msg)


if __name__ == '__main__':
    main()
