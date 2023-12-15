f = open("input.txt", "r")

part_id_sum = 0
lines = f.readlines()
for line_idx, line in enumerate(lines):
    char_idx = 0
    while char_idx < len(line):
        if line[char_idx].isnumeric():
            
            idx_end = char_idx
            while line[idx_end].isnumeric():
                idx_end += 1
            
            is_engine_part = False

            for c in lines[max(line_idx-1,0)][max(char_idx-1,0):min(idx_end+1,len(line)-1)]:
                if (not c.isalnum()) and c != '.':
                    is_engine_part = True
            
            for c in lines[line_idx][max(char_idx-1,0):min(idx_end+1,len(line)-1)]:
                if (not c.isalnum()) and c != '.':
                    is_engine_part = True
            
            for c in lines[min(line_idx+1, len(lines)-1)][max(char_idx-1,0):min(idx_end+1,len(line)-1)]:
                if (not c.isalnum()) and c != '.':
                    is_engine_part = True

            if is_engine_part:
                part_id_sum += int(line[char_idx:idx_end])
            else:
                print(int(line[char_idx:idx_end]))
            char_idx = idx_end+1
        else:
            char_idx += 1
print(part_id_sum)