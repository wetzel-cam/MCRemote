from mcrcon import MCRcon
import json

class RemoteConnection:
    # TODO: Create import system for json data to advancement_list

    def __init__(self, host=None, password=None):
        if host is not None and password is not None:
            self._host = host
            self._password = password
            self._client = MCRcon(host, password)
            self.connect()
        else:
            self._host = None
            self._password = None
            self._client = None

        self._adv_file, self.adv_categories = self._load_advancements()

    def _get_advancement(self, category, general_name):
        return self._adv_file[self.adv_categories[category]][general_name]

    def _load_advancements(self):
        return json.loads(open('advancements.json').read()), list(json.loads(open('advancements.json').read()))

    def connect(self):
        if self._client is None:
            if self._host is not None and self._password is not None:
                self._client = MCRcon(self._host, self._password)
            else:
                self.set_host(input("Enter Host IP: "))
                self.set_password(input("Enter Password: "))
                self._client = MCRcon(self._host, self._password)

            self._client.connect()
        else:
            self._client.connect()

    def disconnect(self):
        self._client.disconnect()

    def set_host(self, host_data):
        self._host = host_data

    def set_password(self, password_data):
        self._password = password_data

    def advancement(self, action_choice, target, advancement_target_choice, advancement):
        actions = ['grant', 'revoke']
        advancement_targets = ['only', 'until', 'from', 'through', 'everything']
        # Make a json file with all the advancements and have a method decode and set this key-pair

        action = actions[action_choice]
        advancement_target = advancement_targets[advancement_target_choice]

        if action == 'grant':
            if advancement_target == 'only':
                sub_cmd = target + ' ' + 'only ' + 'minecraft:' + advancement['id']

            elif advancement_target == 'until':
                pass
            elif advancement_target == 'from':
                pass
            elif advancement_target == 'through':
                pass
            elif advancement_target == 'everything':
                pass
            else:
                pass
            cmd = 'grant ' + sub_cmd
        elif action == 'revoke':
            pass

        return self._client.command('/advancement ' + cmd)

    def ban(self, targets, reason='No reason given!'):
        return self._client.command('/ban ' + targets + ' ' + reason)

    def ban_ip(self, target, reason):
        return self._client.command('/ban ' + target + ' ' + reason)

    def banlist(self, choice):
        pass

    def bossbar(self, choice):
        pass

    def clear(self):
        pass

    def clone(self):
        pass

    def data(self):
        pass

    def datapack(self):
        pass

    def debug(self):
        pass

    def defaultgamemode(self):
        pass

    def deop(self, player):
        return self._client.command('/deop ' + player)

    def difficulty(self, choice):
        pass

    def effect(self, choice):
        pass

    def enchant(self, enchantment, level, target=...):
        pass

    def execute(self, choice):
        pass

    def experience(self, choice):
        pass

    def fill(self):
        pass

    def function(self):
        pass

    def gamemode(self, gamemode_choice, target):
        gamemodes = ['survival', 'creative', 'adventure', 'spectator']

        mode = gamemodes[gamemode_choice]

        return self._client.command('/gamemode ' + mode + ' ' + target)

    def gamerule(self):
        pass

    def give(self):
        pass

    def help(self):
        pass

    def kick(self):
        pass

    def kill(self):
        pass

    def list(self):
        pass

    def locate(self):
        pass

    def me(self):
        pass

    def msg(self):
        pass

    def op(self, player):
        return self._client.command('/op ' + player)

    def pardon(self, target):
        return self._client.command('/pardon ' + target)

    def pardon_ip(self):
        pass

    def particle(self):
        pass

    def playsound(self):
        pass

    def recipe(self):
        pass

    def reload(self):
        pass

    def replaceitem(self):
        pass

    def save_all(self):
        pass

    def save_off(self):
        pass

    def save_on(self):
        pass

    def say(self, message):
        print(self._client.command('/say ' + message))

    def scoreboard(self):
        pass

    def seed(self):
        pass

    def setblock(self):
        pass

    def setidletimeout(self):
        pass

    def setworldspawn(self):
        pass

    def spawnpoint(self):
        pass

    def spreadplayers(self):
        pass

    def stop(self):
        pass

    def stopsound(self):
        pass

    def summon(self):
        pass

    def tag(self):
        pass

    def team(self):
        pass

    def teleport(self):
        pass

    def tell(self):
        pass

    def tellraw(self):
        pass

    def time(self):
        pass

    def title(self):
        pass

    def tp(self):
        pass

    def w(self):
        pass

    def weather(self, weather_choice=0, duration=None):
        weather_conditions = ['clear', 'rain', 'thunder']

        return self._client.command('/weather ' + weather_conditions[weather_choice])

    def whitelist(self):
        pass

    def worldborder(self):
        pass

    def xp(self):
        pass

# Create a file called 'server.info' and put the info for the server in as follows
# ------------------------------
# <ip>
# <password>
# ------------------------------
# I did this so I can upload the code to Github with out people seeing my server info; no peeky!


file = open("server.info", 'r')
info = []
i = 0

for line in file:
    info.append(line.strip('\n'))
    i += 1

client = RemoteConnection(info[0], info[1])
print(client.advancement(0, 'cam_the_cam', 0, client._get_advancement(0, 'mine_stone')))
