def main():
    input_file = open('input', 'r')
    for line in input_file:
        test_file = open('input', 'r')
        for test_line in test_file:
            matching_char = ''
            for i, char in enumerate(line):
                if (char == test_line[i]):
                    matching_char += char
            if len(matching_char) == len(line) - 1:
                print(matching_char)
                exit(0)


if __name__ == "__main__":
    main()
