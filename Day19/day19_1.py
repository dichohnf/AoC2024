def recursive_pass(design, patterns):
    available_patterns = [pat for pat in patterns if design.startswith(pat)]
    available_patterns.sort(key=len, reverse=True)

    if not available_patterns:
        return False

    for pattern in available_patterns:
        next_design = design[len(pattern):]
        if not next_design or recursive_pass(next_design, patterns):
            return True
    return False


def remove_redundant_patterns(patterns):
    non_redundant_patterns = []

    for pattern in patterns:
        temp_patterns = [p for p in patterns if p != pattern]
        if not recursive_pass(pattern, temp_patterns):
            non_redundant_patterns.append(pattern)

    return non_redundant_patterns


def main():
    with open("../inputs/19.in") as file:
        lines = file.read().splitlines()

    patterns = lines[0].split(", ")
    designs = lines[2:]

    patterns = remove_redundant_patterns(patterns)
    result = sum(recursive_pass(design, patterns) for design in designs)

    print(result)


if __name__ == '__main__':
    main()
