def main() -> None:
    total_overlaps = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            assignments = line[:-1].split(',')
            assign_one = list(map(int, assignments[0].split('-')))
            assign_two = list(map(int, assignments[1].split('-')))

            if (assign_one[1] >= assign_two[0] and assign_one[1] <= assign_two[1] or # asn-1's min is between asn-2's min and max
                assign_one[0] >= assign_two[0] and assign_one[0] <= assign_two[1] or # asn-1's max is between asn-2's min and max
                assign_two[1] >= assign_one[0] and assign_two[1] <= assign_one[1] or # asn-2's min is between asn-1's min and max
                assign_two[0] >= assign_one[0] and assign_two[0] <= assign_one[1]):  # asn-2's max is between asn-1's min and max
                total_overlaps += 1

    print('\nFinal Total overlaps:', total_overlaps)


if __name__ == '__main__':
    main()
