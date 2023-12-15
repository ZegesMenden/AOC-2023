f = open("input.txt", "r")

game_power_sum = 0
for line_raw in f.readlines():
    games = line_raw.split(";")
    game_id = int(games[0].split(" ")[1][0:-1])
    game_is_valid = True
    max_r = 0
    max_g = 0
    max_b = 0
    for game in games:
        tokens = game.split(" ")
        red = 0
        green = 0
        blue = 0
        for idx, token in enumerate(tokens):
            if token.isnumeric():
                if ( "red" in tokens[idx+1] ):
                    red = int(token)
                if ( "green" in tokens[idx+1] ):
                    green = int(token)
                if ( "blue" in tokens[idx+1] ):
                    blue = int(token)
        max_r = max(red, max_r)
        max_g = max(green, max_g)
        max_b = max(blue, max_b)
    game_power = max_r*max_g*max_b
    game_power_sum += game_power
print(game_power_sum)