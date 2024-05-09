import argparse
from create_team import *
from scoreboard import *


def main():
    parser = argparse.ArgumentParser(description='commands of parser information')
    parser.add_argument('-create', '-c' , nargs=2, metavar=("name", "team"), type=str, help='create a team')
    parser.add_argument('-scoreboard', '-s', metavar='scoreboard', type=str, help='create scoreboard by time')
    parser.add_argument('-env', metavar='environment', type=str, help='num of list: us | fav | all')
    # parser.add_argument('-info', action='store_true', help='Show information about the competition')
    # parser.add_argument('-testcase', '-t', metavar='testcase', type=str, help='about out test cases')
    # parser.add_argument('-problem', '-p', metavar='problem', type=str, help='choose a problem')
    # parser.add_argument('-test', metavar='test', type=str, help='choose a testcase')
    # parser.add_argument('-sign', metavar='sign', type=str, help='sign of the problem')
    # parser.add_argument('-language', '-lang', metavar='language', type=str, help='sign of the problem')
    # parser.add_argument('-judge', '-j', metavar='judge', type=str, help='judge the problem')
    # parser.add_argument('-just', metavar='just', type=str, help='just something [compile | run]')
    # parser.add_argument('-timing', '-time', action='store_true', help='by time or not')
    # parser.add_argument('-memory', action='store_true', help='by memory used or not')
    # parser.add_argument('-change', action='store_true', help='change something')
    # parser.add_argument('-contest', action='store_true', help='about contest [description]')
    # parser.add_argument('-status', metavar='status', type=str, help='you should choose: [out | raw | stock | running | accept | done]')
    # parser.add_argument('-ending', '-end', metavar='ending', type=str, help='for end of contest')
    # parser.add_argument('-assets', '-as', nargs=2, metavar=("des", "src") , type=str, help='assets codes')
    # parser.add_argument('-byetc', action='store_true', help='by etc or not')
    # parser.add_argument('-search', metavar='search', type=str, help='for end of contest')
    # parser.add_argument('-addproblem', '-addp', metavar='addproblem', type=str, help='to add a problem')
    # parser.add_argument('-rmproblem', '-rmp', metavar='addproblem', type=str, help='to remove a problem')
    args = parser.parse_args()

    if args.create:
        name, university = args.create
        create_team(name, university)
    elif args.scoreboard:
        scoredboard = create_scoreboard(int(args.scoreboard))
        printscoreboard(scoredboard, args.env)
    else:
        print("\033[1;31mError\033[0m: Invalid arguman!")


if __name__ == "__main__":
    main()