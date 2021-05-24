import sys

if __name__ == "__main__":
    predicate_table = {
        '#': "wall",
        '0': "black",
        'F': "food",
        'T': "treasure",
        'S': "start",
        'E': "exit"
    }

    fact_table = {}
    for predicate in predicate_table.values():
        fact_table[predicate] = []

    dim = int(input())
    for y, line in enumerate(sys.stdin):
        for x in range(dim):
            if x < dim and y < dim:
                char = line[x]
                predicate = predicate_table[char]
                fact_table[predicate].append((x, y))

    for predicate, position_list in fact_table.items():
        for x, y in position_list:
            print(f"{predicate}([{x}, {y}]).")
