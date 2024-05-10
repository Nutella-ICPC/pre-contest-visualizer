import json

def create_scoreboard(time):
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)
    with open(f"./{config['jsonfile']}", 'r') as jsonfile:
        latest_scoreboard = json.load(jsonfile)

    first_accept = ['na'] * len(latest_scoreboard['question_names'])
    total_accept = [0] * len(latest_scoreboard['question_names'])

    new_scoreboard = []
    for team in latest_scoreboard['teams']:
        new_team = [team[0], *team[2: 0: -1]]
        count = 0
        penalty = 0
        statusbar = []
        counter = 0
        for accept, trying, timing in zip(*team[6: 9]):
            if accept > 0 and time >= timing:
                total_accept[counter] += 1
                first_accept[counter] = timing if first_accept[counter] == 'na' else min(first_accept[counter], timing)
                count += 1
                penalty += (timing + (trying - 1) * 20)
                status = timing
            else:
                status = '--'
            counter += 1

            statusbar.append(f'{trying}/{status}')
        new_team.append(count)
        new_team.append(penalty)
        new_team.append(statusbar)
        new_scoreboard.append(new_team)
    
    new_scoreboard = sorted(new_scoreboard, key=lambda x: (-x[3], x[4]))
    for i in range(1, len(new_scoreboard) + 1):
        new_scoreboard[i - 1][0] = i
    new_scoreboard.append(['+', 'total acccept', '', '', '', total_accept])
    new_scoreboard.append(['*', 'first acccept', '', '', '', first_accept])

    return new_scoreboard


def colored_text(text, color,  *features, reset = True):

    colors = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magneta": "35",
        "cyan": "36",
        "gray": "37",

        "reset": "0",
        "bold": "1",
        "faint": "2",
        "italic": "3",
        "underline": "4",
        "blink": "5",
        "negative": "7",
        "crossed": "9",
    }

    light = None
    if len(color.split()) == 2:
        light, color = color.split()

    result = f'\033[{1 if light else 0};{colors.get(color.lower(), "")}m'
    for feature in features:
        if feature.lower() in colors.keys():
            result += f'\033[{colors[feature.lower()]}m'

    return result + str(text) + ("\033[0m" if reset else '')

def get_rank_by_color(rank):
    if (rank <= 4):
        return 'light yellow'
    if (rank <= 8):
        return 'light blue'
    if (rank <= 12):
        return 'light red'
    return None

def showscoreboard(scoreboard, our_team, hide):
    max_field_width = [0, 0, 0, 0] # rank, name, university, penalty

    def returner_message_fields(team):
        return [*team[0: 3], team[4]]

    for team in scoreboard:
        team_message = returner_message_fields(team)
        for i, field in enumerate(team_message):
            max_field_width[i] = max(max_field_width[i], len(str(field)))

    for row, team in enumerate(scoreboard):
        rank = f"{str(team[0]):>{max_field_width[0]}}"
        if row < len(scoreboard) - 2:
            rank_color = get_rank_by_color(team[0])
            if rank_color:
                rank = colored_text(rank, rank_color)
        else:
            if 'status' in hide:
                break
        name = f"{str(team[1]):>{max_field_width[1]}}"
        university = f"{str(team[2]):>{max_field_width[2]}}" if 'uni' not in hide else ''
        if team[1] == our_team:
            name = colored_text(name, 'light green')
            university = colored_text(university, 'light green')
        accept = f"{str(team[3]):>{2}}"
        penalty = f"{str(team[4]):>{max_field_width[3]}}"
        print(rank, name, university, accept, penalty, end=' ')
        if 'status' not in hide:
            for status, first_accept in zip(team[5], scoreboard[-1][5]):
                if row < len(scoreboard) - 2 or len(scoreboard) == 1:
                    trying, timing = status.split('/')    
                    status_color = None
                    if timing == '--' and int(trying):
                        status_color = 'light red'
                    elif timing != '--':
                        if int(timing) == first_accept:
                            status_color = 'light cyan'
                        else:
                            status_color = 'light green'
                else:
                    status_color = 'green'
                status_message = f"{status:>{6}}"
                if status_color:
                    status_message = colored_text(status_message, status_color)
                print(status_message, end=' ')
        print()


def printscoreboard(scoreboard, env, hide = False):
    with open('./config.json', 'r') as configfile:
        config = json.load(configfile)
    hide_list = list(hide.split()) if hide else []
    show = []
    if env == 'all':
        show += scoreboard
    elif env == 'fav':
        for team in scoreboard:
            if team[1] in config['favorites'] or team[1] == config['team_curser']:
                show.append(team)
    elif env == 'us':
        for team in scoreboard:
            if team[1] == config['team_curser']:
                show.append(team)
                break
    else:
        print("\033[1;31mError\033[0m: Invalid arguman for env!")
        exit(1)
    
    showscoreboard(show, config['team_curser'], hide_list)