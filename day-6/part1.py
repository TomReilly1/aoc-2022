def main() -> None:
    datastream = ''
    with open('input.txt', 'r') as f:
        datastream = f.readline()

    proc_chars = 0
    curr_string = ''
    for index, char in enumerate(datastream[:-1]):
        if len(curr_string) < 4:
            curr_string += char
        else:
            curr_string = curr_string[1:] + char
           
            start_packet = True
            for i in curr_string:
                if curr_string.count(i) > 1:
                    start_packet = False

            if start_packet:
                proc_chars = index + 1
                break
    
    print('Processed Characters:', proc_chars)


if __name__ == '__main__':
    main()
