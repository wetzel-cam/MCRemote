from mcrcon import MCRcon


class RemoteConnection:
    def __init__(self, host=None, password=None):
        if host is not None and password is not None:
            self.host = host
            self.password = password
            self.client = MCRcon(host, password)
            self.connect()
        else:
            self.host = None
            self.password = None
            self.client = None

    def connect(self):
        if self.client is None:
            if self.host is not None and self.password is not None:
                self.client = MCRcon(self.host, self.password)
            else:
                self.set_host(input("Enter Host IP: "))
                self.set_password(input("Enter Password: "))
                self.client = MCRcon(self.host, self.password)

            self.client.connect()
        else:
            self.client.connect()

    def disconnect(self):
        self.client.disconnect()

    def set_host(self, host_data):
        self.host = host_data

    def set_password(self, password_data):
        self.password = password_data

    def advancement(self, action_choice, target, advancement_choice):
        actions = {'grant', 'revoke'}
        advancement_targets = {'only', 'until', 'from', 'through', 'everything'}
        # Make a json file with all the advancements and have a method decode and set this key-pair
        advancements_list = []

        action = actions[action_choice]
        advancement_target = advancement_targets[advancements_list]

        if action == 'grant':
            if advancement_target == 'only':
                pass
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
            pass
        elif action == 'revoke':
            pass

    def ban(self, reason, targets=...):
        pass

    def ban_ip(self, target, reason):
        pass

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
        return self.client.command('/deop ' + player)

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

    def gamemode(self):
        pass

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
        return self.client.command('/op ' + player)

    def pardon(self):
        pass

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
        response = self.client.command('/say ' + message)
        print(response)

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

    def weather(self):
        pass

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
info = {}
i = 0

for line in file:
    info[i] = line.strip('\n')
    i += 1

client = RemoteConnection(info[0], info[1])
