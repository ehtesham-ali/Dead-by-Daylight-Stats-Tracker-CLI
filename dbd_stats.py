import argparse
import json
import sys

# Setting important variables
character_raw = open('characters.json', 'r').read()
character_dict = json.loads(character_raw)
character_names = [x for x in character_dict['characters'].keys()]
character_names.append('all')
match_number = character_dict['match_number']

# Setting up + adding CLI arguments
parser = argparse.ArgumentParser()

parser.add_argument('show_edit_stats',
                    help='Specify if you want to show or edit stats',
                    choices=['show', 'edit'])

parser.add_argument('name',
                    help='Specify what killer/survivor you want to edit stats for',
                    choices=character_names)

parser.add_argument('--val',
                    help='By what value do you want to change the stats for this killer/survivor? Ex. +1, -5')

parser.add_argument('--match_number',
                    help='By what value do you want to change the amount of matches you\'ve been in to collect data?')
                    
args = parser.parse_args()

# Handling arguments given
if args.show_edit_stats == 'show':
    
    if args.name == 'all':
        character_dict_string = json.dumps(character_dict, indent=2)
        print(character_dict_string)
        sys.exit()
        
    result = character_dict['characters'][args.name]
    print(f'You have faced The {args.name} {result} times in {match_number} rounds')

if args.show_edit_stats == 'edit':
    result = character_dict['characters'][args.name]
    character_dict['characters'][args.name] += int(args.val)

    if args.match_number != None:
        character_dict['match_number'] += int(args.match_number)
        match_number = character_dict['match_number']


    with open('characters.json', 'w') as database:
        character_dict_string = json.dumps(character_dict, indent=2)
        database.write(character_dict_string)

    print(f'{args.name}: {int(result) + int(args.val)} (Prev. {int(result)}) in {match_number} round(s)')

sys.exit()