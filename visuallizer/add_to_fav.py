import json

def add_to_fav(name):
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)
    with open(f"./{config['jsonfile']}", 'r') as jsonfile:
        scoreboard = json.load(jsonfile)

    if name.lower() in [team[2].lower() for team in scoreboard['teams']] and name.lower() not in [team.lower() for team in config['favorites']]:
        config['favorites'].append(name)
    else:
        print(f"\033[1;31mError\033[0m: {name} is not exist! (or exist in favorite list)")
        exit(0)

    with open(f"./{config['jsonfile']}", 'w') as jsonfile:
        json.dump(scoreboard, jsonfile)
    with open(f"./config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)

