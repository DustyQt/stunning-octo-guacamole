import pandas as pd
import random
SKILLS_PER_ROLL = 3
NUMER_OF_ROLLS = 2

def get_skills(dice):
    df = db[(db['minimum_dice'] <= dice) & (db['maximum_dice'] >= dice)]
    if len(df) == 0:
        return 'no_skills_found'
    df['probability']= df['weight'].cumsum()
    results = []
    for i in range(min(SKILLS_PER_ROLL, len(df))):
        skill_index = random.choices(df.index, weights=df['weight'])[0]
        skill = df.loc[skill_index]['skill']
        results.append(skill)
        df.drop(skill_index, inplace=True)
    return results

def select_option(options):
    while True:
        print(f'options: {options}')
        print('select skill number')
        selected_option = int(input())-1
        if 0 <= selected_option < len(options):
            return options[selected_option]
        else:
            print('incorrect_option')

def roll_skill(db, deck):
    while True:
        print('what is your dice?')
        dice = int(input())
        options = get_skills(dice)
        if options != 'no_skills_found':
            skill = select_option(options)
            deck.append(skill)
            print(f'deck: {deck}')
            indexes_to_drop = db[db['skill'] == skill].index
            db.drop(indexes_to_drop, inplace= True)
            break
        else:
            print('no skills found roll again')

db = pd.read_csv('skills.csv')
deck = []
for i in range(NUMER_OF_ROLLS):
    roll_skill(db, deck)

print('---your final deck is:---')
print(deck)

