def main() -> None:
    counter = 0
    max = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        
        for line in lines:
            if line != '\n':
                counter += int(line)
            else:
                if counter > max:
                    max = counter
                counter = 0
            
    print(max)


if __name__ == '__main__':
    main()