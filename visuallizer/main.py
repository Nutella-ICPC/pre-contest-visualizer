import argparse
from create_team import *
from scoreboard import *
from add_status import *

def main():
    parser = argparse.ArgumentParser(description='commands of parser information')
    parser.add_argument('-create', '-c' , nargs=2, metavar=("name", "team"), type=str, help='create a team')
    parser.add_argument('-scoreboard', '-s', metavar='scoreboard', type=str, help='create scoreboard by time')
    parser.add_argument('-env', '-e', metavar='environment', type=str, help='num of list: us | fav | all')
    parser.add_argument('-hide', metavar='hide', type=str, help='hide some information')
    parser.add_argument('-add', '-a' , nargs=3, metavar=("time", 'problem', "status"), type=str, help='add a status')
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
    else:
        print("\033[1;31mError\033[0m: Invalid arguman!")


if __name__ == "__main__":
    main()