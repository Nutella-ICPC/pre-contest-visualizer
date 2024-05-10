import requests # type: ignore
from bs4 import BeautifulSoup
import json


name = 'Internet ICPC 2022 Asia Region Tehran Site'
url = 'http://icpc.sharif.edu/2022/iipc/scoreboard/'

# name = input('Enter name of contest: ')
# url = input('Enter scoreboard url of contest: ')

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text  # Get the HTML content
else:
    print("Error fetching webpage:", response.status_code)
    exit()

soup = BeautifulSoup(html_content, "html.parser")

rankings_table = soup.find("table", id='scoreboard')  # Assuming only one table
if not rankings_table:
    raise Exception("Couldn't find rankings table in the HTML")

header_row = rankings_table.find('thead').find('tr')
letters = []
for th in header_row.find_all('th')[4: -1]:
    letter_span = th.find("span", class_="balloon")
    if letter_span:
        letters.append(letter_span.text.strip())

my_data_html = soup.find('script')
row_list = eval(my_data_html.string.split('=')[1].strip()[0: -1])

total_teams = []
for team in row_list:
    try:
        team[0] = int(team[0])
    except ValueError:
        team[0] = 0
    team_list = [team[0], team[1].split(":")[0].strip(), team[1].split(":")[1].strip(), *team[2: 5]]
    accept = [0] * len(letters)
    trying = [0] * len(letters)
    timing = [0] * len(letters)
    for index, q in enumerate(team[5: -1]):
        if q != 0:
            if q[1] == 'yes':
                accept[index] = 1
            elif q[1] == 'yes first':
                accept[index] = 2
            ti, tr = q[0].split('/')
            tr = tr.split()[0]
            trying[index] = int(tr)
            timing[index] = int(ti) if ti != '--' else 0
    team_list.append(accept)
    team_list.append(trying)
    team_list.append(timing)
    total_teams.append(team_list)

main_dict = {
    'name': name,
    'url': url,
    'question_names': letters,
    'teams': total_teams,
}

with open(f"./jsons/{'-'.join(name.split())}.json", "w") as outfile:
    # json.dump(main_dict, outfile, indent=4)
    json.dump(main_dict, outfile)

