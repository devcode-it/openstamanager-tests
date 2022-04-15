import os
import json

directory = __file__
directory = os.path.dirname(directory)

filename = directory + '/config.json'

with open(filename, 'r') as json_file:
    tests = json.load(json_file)

for test in tests:
    os.system("python3 -m unittest " + test)
