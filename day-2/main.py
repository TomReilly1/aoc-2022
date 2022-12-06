def main() -> None:
    opp_choices = {
        'A': {
            'name': 'rock',
            'wins_over': 'scissors',
            'loses_to': 'paper'
        },
        'B': {
            'name': 'paper',
            'wins_over': 'rock',
            'loses_to': 'scissors'
        },
        'C': {
            'name': 'scissors',
            'wins_over': 'paper',
            'loses_to': 'rock'
        }
    }

    points_total = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            opp_choice = line[0]
            outcome = line[2]

            plyr_choice = None
            points_from_round = 0

            match outcome:
                case 'X': # lose
                    plyr_choice = opp_choices[opp_choice]['wins_over']
                    pass
                case 'Y': # draw
                    plyr_choice = opp_choices[opp_choice]['name']
                    points_from_round += 3
                case 'Z': # win
                    plyr_choice = opp_choices[opp_choice]['loses_to']
                    points_from_round += 6
                case _:
                    raise Exception('Did not match outcome character')
            
            match plyr_choice:
                case 'rock':
                    points_from_round += 1
                case 'paper':
                    points_from_round += 2
                case 'scissors':
                    points_from_round += 3
                case _:
                    raise Exception('Did not match player choice string')

            points_total += points_from_round


    print(points_total)

if __name__ == '__main__':
    main()