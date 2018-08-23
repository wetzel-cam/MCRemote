import json
import os

os.chdir('..')
adv_file = json.loads(open('advancements.json').read())
print(adv_file)
print(list(adv_file['story']))


