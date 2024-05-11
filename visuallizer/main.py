import argparse
from create_team import create_team
from scoreboard import create_scoreboard, printscoreboard
from add_status import add_status
from read_status import read_status
from add_to_fav import add_to_fav
from remove_from_fav import remove_from_fav
from pop_last_submit import pop_last_submit

def main():
    parser = argparse.ArgumentParser(description='commands of parser information')
    parser.add_argument('-create', '-c' , nargs=2, metavar=("name", "team"), type=str, help='create a team')
    parser.add_argument('-scoreboard', '-s', metavar='scoreboard', type=str, help='create scoreboard by time')
    parser.add_argument('-env', '-e', metavar='environment', type=str, help='num of list: us | fav | all')
    parser.add_argument('-hide', metavar='hide', type=str, help='hide some information')
    parser.add_argument('-add', '-a' , nargs=3, metavar=("time", 'problem', "status"), type=str, help='add a status')
    parser.add_argument('-read', action='store_true', help='reading status')
    parser.add_argument('-pop', action='store_true', help='pop last submit')
    parser.add_argument('-favorite', '-f', nargs=2, metavar=("status", "team"), type=str, help='add a team to favorite list')
    args = parser.parse_args()

    if args.create:
        name, university = args.create
        create_team(name, university)
    elif args.scoreboard and args.env:
        scoredboard = create_scoreboard(int(args.scoreboard))
        if args.hide:
            printscoreboard(scoredboard, args.env, args.hide)
        else:
            printscoreboard(scoredboard, args.env)
    elif args.add:
        time, problem, status = args.add
        add_status(time, problem, status)
    elif args.read:
        read_status()
    elif args.favorite:
        status, team = args.favorite
        if status.lower() in ['add', 'a']:
            add_to_fav(team)
        elif status.lower() in ['remove', 'r']:
            remove_from_fav(team)
        else:
            print("\033[1;31mError\033[0m: Invalid arguman for favorite!")
    elif args.pop:
        pop_last_submit()
    else:
        print("\033[1;31mError\033[0m: Invalid arguman!")


if __name__ == "__main__":
    main()