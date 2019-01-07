def main():
    frequency_number = 0
    input_file = open('input', 'r')
    for line in input_file:
        number = int(line)
        frequency_number += number
    print(frequency_number)


if __name__ == "__main__":
    main()
