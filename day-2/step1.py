def main():
    double_letters = 0
    triple_letters = 0
    input_file = open('input', 'r')
    for line in input_file:
        double_letters_found = False
        triple_letters_found = False
        characters = set(line.replace('\n', ''))
        for character in characters:
            if not double_letters_found and (line.count(character) == 2):
                double_letters += 1
                double_letters_found = True
            elif not triple_letters_found and (line.count(character) == 3):
                triple_letters += 1
                triple_letters_found = True
            if double_letters_found and triple_letters_found:
                break
    checksum = double_letters * triple_letters
    print(checksum)


if __name__ == "__main__":
    main()
