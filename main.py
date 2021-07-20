import json
from difflib import get_close_matches

with open('data.json') as f:
    data = json.load(f)


def print_data(word):
    print(f'{word.title()}:')
    for i in data[word]:
        print('-' + i)


key = input('Enter the word you want to translate\n').strip().lower()
found = False
if key in data:
    found = True
    print_data(key)
else:
    for j in get_close_matches(key, data.keys(), n=10):
        choice = input(f'Is this the word you meant: {j} (select y/n to accept/decline)?\n').strip().lower()
        if choice == 'y':
            found = True
            print_data(j)
            break
if not found:
    print("can't find that word or similar")
