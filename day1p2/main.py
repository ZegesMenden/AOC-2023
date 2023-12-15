f = open("input.txt", "r")

nums = ["one","two","three","four","five","six","seven","eight","nine"]

def getnum(line: str):
    
    nline = ""
    for idx, char in enumerate(line):
        if char.isnumeric():
            nline = nline + char
            continue
        for nidx, n in enumerate(nums):
            if n in line[idx:idx+len(n)]:
                nline = nline + str(nidx+1)
                continue
    num_l = ''
    idx = 0
    while not ((nline[idx]).isnumeric()):
        idx += 1
    num_l = nline[idx]
    
    idx = -1
    while not ((nline[idx]).isnumeric()):
        idx -= 1

    return int(num_l+nline[idx])


sum_of_nums = 0
for line in f.readlines():
    num = getnum(line)
    # print(num)
    sum_of_nums += num
print(sum_of_nums)