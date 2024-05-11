import json

def remove_from_fav(name):
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)

    for team in config['favorites']:
        if team.lower() == name.lower():
            config['favorites'].remove(team)
            break
    else:
        print(f"\033[1;31mError\033[0m: {name} is not exist!")
        exit(1)

    with open(f"./config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)

