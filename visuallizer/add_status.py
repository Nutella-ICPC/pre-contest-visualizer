import json

def check_inputs(time, problem, status, problemnum):
    try:
        time = int(time)
    except ValueError:
        print("\033[1;31mError\033[0m: Invalid time!")
        exit(1)
    if status.lower() not in ['a', 'w', 'accept', 'wrong']:
        print("\033[1;31mError\033[0m: Invalid status!")
        exit(1)
    if 0 <= (ord(problem.lower()[0]) - ord('a')) < problemnum:
        problem = ord(problem.lower()[0]) - ord('a') + 1
    status = 'a' if status.lower() in ['a', 'accept'] else 'w'
    return time, problem, status

def add_status(time, problem, status):
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)
    with open(f"./{config['jsonfile']}", 'r') as jsonfile:
        scoreboard = json.load(jsonfile)
    time, problem, status = check_inputs(time, problem, status, len(scoreboard['question_names']))

    config['status'].append((time, chr(problem + ord('A') - 1), status))
    for team in scoreboard['teams']:
        if team[2] == config['team_curser']:
            if status == 'a':
                team[6][problem - 1] = 1
                team[8][problem - 1] = time
            team[7][problem - 1] += 1

    with open(f"./{config['jsonfile']}", 'w') as jsonfile:
        json.dump(scoreboard, jsonfile)
    with open(f"./config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)

