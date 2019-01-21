from parse import parse


def parse_line(line):
    parsed_line = parse("#{line:d} @{x:d},{y:d}: {width:d}x{length:d}", line)
    return parsed_line


def main():
    tissue = [[]]
    input_file = open('input', 'r')
    nb_overlap = 0
    for line in input_file:
        overlapped = False
        wanted_tissue = parse_line(line)
        for x in range(wanted_tissue['x'], wanted_tissue['width']):
            for y in range(wanted_tissue['y'], wanted_tissue['length']):
                if not overlapped and tissue[x][y] == 'x':
                    overlapped = True
                tissue[x][y] = 'x'
        nb_overlap += 1
    print(nb_overlap)


if __name__ == '__main__':
    main()
