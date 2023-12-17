f = open("t.txt", "r")
lines = f.readlines()
f.close()

maps = {}

seeds = []
line0 = lines[0].split(" ")
for w in line0:
    w = w.strip("\n")
    if w.isnumeric():
        seeds.append(int(w))

current_map_key = ""
all_map_keys = []

for line in lines[1:]:

    if line[0].isalpha():
        # if current_map_key in maps.keys():
        #     print(f"{current_map_key}:")
        #     print(maps[current_map_key])
        #     print("\n")

        current_map_key = line.split(" ")[0]
        all_map_keys.append(current_map_key)
        maps[current_map_key] = []
    elif line[0].isnumeric():
        lsplit = line.split(" ")
        dest_start = int(lsplit[0])
        src_start = int(lsplit[1])
        map_range = int(lsplit[2])
        maps[current_map_key].append([dest_start, src_start, map_range])

for key in all_map_keys:
    for seed_idx, seed in enumerate(seeds):
        for submap in maps[key]:
            if seed >= submap[1] and seed <= submap[1] + submap[2]:
                seeds[seed_idx] = submap[0] + (seed-submap[1])
                break
    r_max = max(seeds)
    for i in range(r_max):
        if i in seeds:
            print("*",end="")
        else:
            print("_",end="")
    print()
print()
print()
r_max = max(seeds)
for i in range(r_max):
    if i in seeds:
        print("*",end="")
    else:
        print("_",end="")
print()

print(min(seeds))