import os
import json

jsonfile = None
for filename in os.listdir(os.getcwd()):
    if filename.lower().endswith(".json"):
        jsonfile = filename
        break
if not jsonfile:
    print("\033[1;31mError\033[0m: we can not find any json file!")
    exit(1)

executable_file = os.path.join(os.path.dirname(__file__), "main.py")
script_content = f'''#!/bin/bash\n\npython3 "{executable_file}" "$@"'''
with open('./r', 'w') as f:
    f.write(script_content)
os.chmod('./r', 0o755)  # Add execute permissions to the script

config = {
    'team_curser': None,
    'jsonfile': jsonfile,
    'favorites': [],
}

with open(f"./config.json", "w") as outfile:
    json.dump(config, outfile, indent=4)
