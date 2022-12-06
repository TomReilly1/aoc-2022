def main() -> None:
    opp_choices = {
        'A': {
            'name': 'rock',
            'wins_against': 'scissors'
        },
        'B': {
            'name': 'paper',
            'wins_against': 'rock'
        },
        'C': {
            'name': 'scissors',
            'wins_against': 'paper'
        },
    }
    plyr_choices = {
        'X': {
            'name': 'rock',
            'wins_against': 'scissors',
            'points': 1
        },
        'Y': {
            'name': 'paper',
            'wins_against': 'rock',
            'points': 2
        },
        'Z': {
            'name': 'scissors',
            'wins_against': 'paper',
            'points': 3
        },
    }

    points_total = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            opp_choice = line[0]
            plyr_choice = line[2]

            points_total += plyr_choices[plyr_choice]['points']

            if plyr_choices[plyr_choice]['wins_against'] == opp_choices[opp_choice]['name']:
                points_total += 6
            elif plyr_choices[plyr_choice]['name'] == opp_choices[opp_choice]['name']:
                points_total += 3

    print(points_total)

if __name__ == '__main__':
    main()