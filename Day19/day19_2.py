suffixes_seen = {}


def recursive_pass(design, patterns):
    if design in suffixes_seen:
        return suffixes_seen[design]

    available_patterns = [pat for pat in patterns if design.startswith(pat)]

    if not available_patterns:
        suffixes_seen[design] = 0
        return 0

    total_suffix_val = 0
    for pattern in available_patterns:
        next_design = design[len(pattern):]
        if not next_design:
            total_suffix_val += 1
        else:
            total_suffix_val += recursive_pass(next_design, patterns)

    suffixes_seen[design] = total_suffix_val
    return total_suffix_val


def main():
    with open("../inputs/19.in") as file:
        lines = file.read().splitlines()

    patterns = lines[0].split(", ")
    designs = lines[2:]

    result = sum(recursive_pass(design, patterns) for design in designs)
    print(result)


if __name__ == '__main__':
    main()
