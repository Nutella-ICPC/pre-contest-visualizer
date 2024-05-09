import json

def create_team(name, university):
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)
    with open(f"./{config['jsonfile']}", 'r') as jsonfile:
        scoreboard = json.load(jsonfile)

    if name.lower() in [team[2].lower() for team in scoreboard['teams']]:
        print(f"Error: {name} was exist!")
        exit(1)

    new_rank = scoreboard['teams'][-1][0] + 1
    qnum = len(scoreboard['question_names'])
    new_team = [new_rank, university, name, 0, 0, 0, [0] * qnum, [0] * qnum, [0] * qnum]
    scoreboard['teams'].append(new_team)
    
    config['team_curser'] = name

    with open('./config.json', 'w') as configfile:
        json.dump(config, configfile, indent=4)
    with open(f"./{config['jsonfile']}", 'w') as jsonfile:
        json.dump(scoreboard, jsonfile)