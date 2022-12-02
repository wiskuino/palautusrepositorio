

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists

class Statistics:
    def __init__(self, PlayerReader: object):
        reader = PlayerReader()

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player.name

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many,sortkey=None):
        if sortkey == None:
            sortkey = 1
        match sortkey:
            case 1:
                return sorted(self._players,reverse=True,key=sort_by_points)[:how_many]
                #sorted_players = sorted(
                #    self._players,
                #    reverse=True,
                #    key=sort_by_points
                #)
                #result = []
                #i = 0
                #while i < how_many:
                #    result.append(sorted_players[i])
                #    i += 1
                #return result

            case 2:

                return sorted(self._players,reverse=True,key=sort_by_goals)[:how_many]
               #sorted_players = sorted(
               #    self._players,
               #    reverse=True,
               #    key=sort_by_goals
               #)
               #result = []
               #i = 0
               #while i < how_many:
               #    result.append(sorted_players[i])
               #    i += 1
               #return result

            case 3:
                  
                 return sorted(self._players,reverse=True,key=sort_by_assists)[:how_many]
                 #sorted_players = sorted(self._players,reverse=True,key=sort_by_assists)
                 #result = []
                 #i = 0
                 #while i < how_many:
                 #    result.append(sorted_players[i])
                 #    i += 1
                 #return result