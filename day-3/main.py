from math import floor


def generate_priority_dict() -> dict:
    l_dict = dict()

    # 97-122 is ASCII decimal values for a-z 
    # 65-90 is ASCII decimal values for A-Z 
    for i in range(1, 53):
        if i <= 26:
            l_dict[chr(i + 96)] = i
        else:
            l_dict[chr(i + 64 - 26)] = i

    return l_dict

def main() -> None:
    priority_dict = generate_priority_dict()
    total_points = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        curr_group = []

        for index, line in enumerate(lines):
            curr_group.append(line[:-1])

            if (index + 1) % 3 == 0:
                group_badge = None

                for char in curr_group[0]:
                    if char in curr_group[1] and char in curr_group[2]:
                        group_badge = char

                total_points += priority_dict[group_badge]

                curr_group.clear()                
                                
    print('\nFinal Total Points:', total_points)


if __name__ == '__main__':
    main()
