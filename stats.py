import argparse
import json

# Setting important variables
killerstats = json.loads(open('killerstats.json', 'r').read())
survivorstats = json.loads(open('survivorstats.json', 'r').read())
killernames = [x for x in survivorstats['characters'].keys()]
survivornames = [x for x in killerstats['characters'].keys()]
killermatches = killerstats['match_number']
survivormatches = survivorstats['match_number']
killernames.append('all')
survivornames.append('all')
characternames = killernames + survivornames

# Setting up + adding CLI arguments
parser = argparse.ArgumentParser()

parser.add_argument('show_edit_stats',
                    help='Specify if you want to show or edit stats',
                    choices=['show', 'edit'])

parser.add_argument('killer_survivor_info',
                    help='Specify if you want to view/modify killer or survivor stats',
                    choices=['killer', 'survivor'])

parser.add_argument('name',
                    help='Specify what killer/survivor you want to view/edit stats for',
                    choices=characternames)

parser.add_argument('--val',
                    help='By what value do you want to change the stats for this killer/survivor? Ex. +1, -5')

parser.add_argument('--match_number',
                    help='By what value do you want to change the amount of matches you\'ve been in to collect data?')
                    
args = parser.parse_args()

# Handling arguments given
if args.show_edit_stats == 'show':
    if args.killer_survivor_info == 'killer':
        if args.name == 'all':
            viewer = json.dumps(killerstats, indent=2)
            print(f'All survivors you have hunted in {killermatches} matches:')
            print(viewer)
        
        else:
            print(f'You have hunted {args.name} {killerstats["characters"].get(args.name)} times in {killermatches} matches')

    if args.killer_survivor_info == 'survivor':
        if args.name == 'all':
            viewer = json.dumps(survivorstats, indent=2)
            print(f'All killers you have faced in {survivormatches} matches:')
            print(viewer)
        
        else:
            print(f'You have faced The {args.name} {survivorstats["characters"][args.name]} times in {survivormatches} matches')

if args.show_edit_stats == 'edit':
    if args.killer_survivor_info == 'killer':
        result = killerstats['characters'][args.name]
        killerstats['characters'][args.name] += int(args.val)

        if args.match_number != None:
            killerstats['match_number'] += int(args.match_number)
            killermatches = killerstats['match_number']

        with open('killerstats.json', 'w') as database:
            viewer = json.dumps(killerstats, indent=2)
            database.write(viewer)
        
        print(f'You have hunted {args.name} {killerstats["characters"][args.name]} times in {killermatches} matches (Prev. {result})')

    if args.killer_survivor_info == 'survivor':
        result = survivorstats['characters'][args.name]
        survivorstats['characters'][args.name] += int(args.val)

        if args.match_number != None:
            survivorstats['match_number'] += int(args.match_number)
            survivormatches = survivorstats['match_number']

        with open('survivorstats.json', 'w') as database:
            viewer = json.dumps(survivorstats, indent=2)
            database.write(viewer)
        
        print(f'You have faced The {args.name} {survivorstats["characters"][args.name]} times in {survivormatches} matches (Prev. {result})')