def main() -> None:
    counter = 0
    max_values = [0, 0, 0]

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line != '\n':
                counter += int(line)
            else:
                min_value = min(max_values)
                min_index = max_values.index(min_value)

                if counter > min_value:
                    max_values[min_index] = counter

                counter = 0
            
    print(sum(max_values))


if __name__ == '__main__':
    main()