f = open("input.txt", "r")

part_id_sum = 0
lines = f.readlines()
for line_idx, line in enumerate(lines):
    char_idx = 0
    while char_idx < len(line):
        if line[char_idx] == "*":
            adjacent_nums = []
            char_ncheck = char_idx-1
            lidx = line_idx-1
            while lidx <= line_idx+1:
                char_ncheck = char_idx-1
                while char_ncheck <= char_idx+1:
                    if lines[lidx][char_ncheck].isnumeric():
                        while lines[lidx][char_ncheck-1].isnumeric():
                            char_ncheck -= 1
                        idx_num_start = char_ncheck
                        while lines[lidx][char_ncheck+1].isnumeric():
                            char_ncheck += 1  
                        adjacent_nums.append(int(lines[lidx][idx_num_start:char_ncheck+1]))
                    char_ncheck += 1
                lidx += 1
            if len(adjacent_nums) == 2:
                part_id_sum += adjacent_nums[0]*adjacent_nums[1]
        char_idx += 1
print(part_id_sum)