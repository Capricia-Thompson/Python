class Player:
    def __init__(self, attributes):
        self.name = attributes['name']
        self.age = attributes['age']
        self.position = attributes['position']
        self.team = attributes['team']

    def display_player(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}")
        return self

    roster = []

    @classmethod
    def get_team(cls, team_list):
        for player in team_list:
            cls.roster.append(player.display_player())
        return cls.roster


def make_players(set):
    player_insts = []
    for player in set:
        player_insts.append(Player(player))
    return player_insts


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team = make_players(players)

Player.get_team(new_team)
