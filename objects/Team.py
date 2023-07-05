from objects.Player import Player

class Team(object):

    def __init__(self, teamName : str, player_one: Player, player_two: Player):
        self.teamName = teamName
        self.players = [player_one, player_two]

    def getTeamName(self):
        return self.teamName

    def getPoints(self):
        return self.getPlayerOne().getPoints() + self.getPlayerTwo().getPoints()

    def getPlayers(self):
        return self.players

    def getPlayerOne(self):
        return self.players[0]

    def getPlayerTwo(self):
        return self.players[1]
    
    def getPlayerOneName(self):
        return self.getPlayerOne().getName()

    def getPlayerTwoName(self):
        return self.getPlayerTwo().getName()

    def printTeam(self):
        print(f'Team Name: {self.teamName}')
        print(f'Players: {self.getPlayerOne().getName()} and {self.getPlayerTwo().getName()}')
        print(f'Points: {self.getPlayerOne().getPoints() + self.getPlayerTwo().getPoints()}')
        print()
