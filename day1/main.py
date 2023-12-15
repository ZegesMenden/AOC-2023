f = open("input.txt", "r")
sum_of_codes = 0
for line in f.readlines():
    num_l = ''
    idx = 0
    while not ((line[idx]).isnumeric()):
        idx += 1
    num_l = line[idx]
    
    idx = -1
    while not ((line[idx]).isnumeric()):
        idx -= 1

    num = num_l+line[idx]
    sum_of_codes += int(num)

print(sum_of_codes)