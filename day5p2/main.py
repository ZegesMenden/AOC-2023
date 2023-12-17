f = open("input.txt", "r")
lines = f.readlines()
f.close()

maps = {}

current_map_key = ""
all_map_keys = []

for line in lines[1:]:

    if line[0].isalpha():
        current_map_key = line.split(" ")[0]
        all_map_keys.append(current_map_key)
        maps[current_map_key] = []
    elif line[0].isnumeric():
        lsplit = line.split(" ")
        src_start = int(lsplit[1])
        src_end = src_start+int(lsplit[2])
        src_mod = int(lsplit[0]) - src_start
        maps[current_map_key].append([src_start, src_end, src_mod])

for key in all_map_keys:

    maps[key] = sorted(maps[key])
    # print(maps[key])

    new_maps = []
    if maps[key][0][0] != 0:
        new_maps.append([0,maps[key][0][0],0])
    for submap_idx, submap in enumerate(maps[key]):
        new_maps.append(submap)
        if ( submap_idx + 1 ) < len(maps[key]):
            if submap[1]+1 <= maps[key][submap_idx+1][0]:
                new_maps.append([submap[1], maps[key][submap_idx+1][0]-1, 0])

    maps[key] = new_maps

seed_ranges = []
line0 = lines[0].split(" ")
for widx, w in enumerate(line0):
    w = w.strip("\n")
    if (widx%2)==1:
        ws = int(w)
        wr = int(line0[widx+1].strip("\n"))
        seed_ranges.append([ws, ws+wr])

new_seed_ranges = []

for key in all_map_keys:

    for seed_range in seed_ranges:
        max_modified_idx = 0
        for submap in maps[key]:
            if seed_range[0] >= submap[0] and seed_range[0] <= submap[1]:
                r_end = min(seed_range[1], submap[1])
                max_modified_idx = r_end
                new_seed_ranges.append([seed_range[0]+submap[2], r_end+submap[2]])
            if seed_range[1] >= submap[0] and seed_range[1] <= submap[1]:
                r_start = max(seed_range[0], submap[0])
                max_modified_idx = max(seed_range[1], max_modified_idx)
                new_seed_ranges.append([r_start+submap[2], seed_range[1]+submap[2]])
            if seed_range[1] >= submap[1] and seed_range[0] <= submap[0]:
                max_modified_idx = max(submap[1], max_modified_idx)
                new_seed_ranges.append([submap[0]+submap[2], submap[1]+submap[2]])
        if max_modified_idx == 0:
            new_seed_ranges.append(seed_range)
        else:
            if max_modified_idx < seed_range[1]:
                new_seed_ranges.append([max_modified_idx, seed_range[1]])

    # condense to minimum required sets
    seed_ranges = []
    new_seed_ranges = sorted(new_seed_ranges)

    for new_seed_idx, new_seed in enumerate(new_seed_ranges):
        for i in range(new_seed_idx+1, len(new_seed_ranges)):
            if new_seed_ranges[i][1] <= new_seed[1]:
                new_seed_ranges[i].append(0)
    for new_seed in new_seed_ranges:
        if len(new_seed) < 3:
            seed_ranges.append(new_seed)

    new_seed_ranges = []

print(min(seed_ranges)[0])