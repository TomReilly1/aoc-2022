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

        for line in lines:
            line_length = len(line) - 1  # subtract newline character '\n' from each line 
            mid = floor(line_length / 2)
            
            comp_one = line[:mid]
            comp_two = line[mid:]

            for char in comp_one:
                if char in comp_two:
                    total_points += priority_dict[char]
                    break

    print('\nFinal Total Points:', total_points)

if __name__ == '__main__':
    main()
