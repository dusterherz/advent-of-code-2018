def main():
    base_number = 0
    input_file = open('input', 'r')
    for line in input_file:
        number = int(line)
        base_number += number
    print(base_number)


if __name__ == "__main__":
    main()
