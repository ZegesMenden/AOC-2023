f = open("input.txt", "r")
lines = f.readlines()

cards_sum = 0
card_points = []
card_instances = []

for line_idx, line in enumerate(lines):
    winning_nums = line.split("|")[0].split(" ")
    card_nums = line.split("|")[1].split(" ")
    cpoints = 0
    for wnum in winning_nums:
        wnum = wnum.strip(" ")
        wnum = wnum.strip("\n")
        if wnum.isnumeric():
            for cnum in card_nums:
                cnum = cnum.strip(" ")
                cnum = cnum.strip("\n")
                if cnum == wnum:
                    cpoints += 1
    card_points.append(cpoints)
    card_instances.append(1)


for card_idx, card_point in enumerate(card_points):
    
    for i in range(card_instances[card_idx]):
        tmpidx = card_idx
        while tmpidx < (card_idx + card_points[card_idx]):
            tmpidx += 1
            card_instances[tmpidx] += 1
cards_sum = sum(card_instances)
print(cards_sum)