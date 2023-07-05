
class Player(object):

    def __init__(self, name : str, points : int):
        self.name = name
        self.results = []
        self.points = points

    def getName(self):
        return self.name
    
    def getPoints(self):
        return self.points

    def print(self):
        print(f'Name: {self.name}')
        print(f'Points: {self.getPoints()}')
        print()
    