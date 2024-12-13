from collections import deque
import multiprocessing as mp

def process_rock(rock, iterations):
    queue = deque([(rock, 0)])
    count = 0

    while queue:
        current_rock, current_iteration = queue.popleft()
        if current_iteration == iterations:
            count += 1
        else:
            if current_rock == '0':
                queue.append(('1', current_iteration + 1))
            elif len(current_rock) % 2 == 0:
                mid = len(current_rock) // 2
                left_half = current_rock[:mid]
                right_half = str(int(current_rock[mid:]))
                queue.append((left_half, current_iteration + 1))
                queue.append((right_half, current_iteration + 1))
            else:
                new_rock = str(int(current_rock) * 2024)
                queue.append((new_rock, current_iteration + 1))

    return count


def main():
    rocks = open("../inputs/11.in").read().splitlines()[0].split()
    iterations = 75
    max_processes = 16

    with mp.Pool(processes=min(max_processes, len(rocks))) as pool:
        results = pool.starmap(process_rock, [(rock, iterations) for rock in rocks])
    print(sum(results))

if __name__ == "__main__":
    main()
