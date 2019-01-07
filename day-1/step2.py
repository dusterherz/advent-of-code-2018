def main(list_numbers, start_frequency_number=0, old_frequencies={0: True}):
    frequency_number = start_frequency_number
    for number in list_numbers:
        frequency_number += number
        if frequency_number in old_frequencies:
            print(frequency_number)
            exit(0)
        old_frequencies[frequency_number] = True
    main(list_numbers, frequency_number, old_frequencies)


if __name__ == "__main__":
    input_file = open('input', 'r')
    list_numbers = []
    for line in input_file:
        list_numbers.append(int(line))
    main(list_numbers)
