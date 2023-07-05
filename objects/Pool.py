from objects.Team import Team

class Pool(object):

    def __init__(self, pool_num : int):
        self.pool_num = pool_num
        self.teams = []

    def addTeam(self, team : Team):
        self.teams.append(team)

    def getTeams(self):
        return self.teams
    
    def printPool(self):
        print(f"Pool {self.pool_num}")
        print("Teams:")
        for team in self.getTeams():
            team.printTeam()
        print()
