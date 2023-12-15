f = open("input.txt", "r")

valid_game_id_sum = 0
for line_raw in f.readlines():
    games = line_raw.split(";")
    game_id = int(games[0].split(" ")[1][0:-1])
    game_is_valid = True
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
        if not (red <= 12 and green <= 13 and blue <= 14):
            game_is_valid = False
            break
    if game_is_valid:
        valid_game_id_sum += game_id

print(valid_game_id_sum)