import json

def pop_last_submit():
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)
    with open(f"./{config['jsonfile']}", 'r') as jsonfile:
        scoreboard = json.load(jsonfile)
    
    try:
        time, problem, status = config['status'].pop()
    except IndexError:
        print("\033[1;31mError\033[0m: submit stack is empty!")
        exit(1)

    problem_index = ord(problem) - ord('A')
    for team in scoreboard['teams']:
        if team[2] == config['team_curser']:
            team[6][problem_index] = 0
            team[7][problem_index] -= 1
            team[8][problem_index] = 0
            break

    with open(f"./{config['jsonfile']}", 'w') as jsonfile:
        json.dump(scoreboard, jsonfile)
    with open(f"./config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)