f = open("input.txt", "r")
lines = f.readlines()
f.close()

instructions = lines[0]
lines = lines[2:]

nodes = {}

for element in lines:
    element_parts = element.split(" ")
    nodes[element_parts[0]] = [element_parts[2][1:-1], element_parts[3][:-2]]

position = nodes["AAA"]
total_moves = 0

while True:
    for instruction in instructions:
        if "R" in instruction:
            if position[1] == "ZZZ":
                print("reached ZZZ")
                print((total_moves+1))
                quit()
            position = nodes[position[1]]

            total_moves += 1
        elif "L" in instruction:
            if position[0] == "ZZZ":
                print("reached ZZZ")
                print((total_moves+1))
                quit()
            position = nodes[position[0]]
            total_moves += 1
        else:
            if instruction != "\n":
                print(f"error parsing direction: |{instruction}|")
