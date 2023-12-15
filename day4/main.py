f = open("input.txt", "r")

points_sum = 0
lines = f.readlines()
for line_idx, line in enumerate(lines):
    winning_nums = line.split("|")[0].split(" ")
    card_nums = line.split("|")[1].split(" ")
    card_points = 0
    for wnum in winning_nums:
        wnum = wnum.strip(" ")
        wnum = wnum.strip("\n")
        if wnum.isnumeric():
            for cnum in card_nums:
                cnum = cnum.strip(" ")
                cnum = cnum.strip("\n")
                if cnum == wnum:
                    card_points += 1
    if card_points > 0:
        points_sum += pow(2,card_points-1)
print(points_sum)