import math
import os
import sys
from bs4 import BeautifulSoup
import openpyxl
from tracker.utils.sheet_utils import *
from objects.Team import Team
from objects.Player import Player
from objects.Pool import Pool
import subprocess
import argparse

REPEAT = 0
INCREASE = 1
DECREASE = 2
 
def main():
    parser = argparse.ArgumentParser(
        description="Utility for calculating pools given an html document",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-t',
        dest="tournament",
        default=None,
        required=True,
        help="Input to specify what tournament to generate pools for [default: %(default)s]"
    )
    parser.add_argument(
        '-m',
        dest="major",
        default=False,
        required=False,
        action="store_true",
        help="Input to specify that the tournament is a major [default: %(default)s]"
    )

    args = parser.parse_args(args=None if sys.argv[1:] else ['-h'])

    file = args.tournament
    is_major = args.major

    cmd = 'python ./tracker/update_sheet.py'
    p = subprocess.Popen(cmd)
    p.wait()

    html_doc = readFile(file)
    soup = BeautifulSoup(html_doc, 'html.parser')
    teams = getTeams(soup)
    teams = sorted(teams, key=lambda x: x.getPoints(), reverse=True)
    
    createPoolsWorkbook(teams, is_major, file)


def createPoolsWorkbook(teams, is_major, file):
    wb = getWorkBook(str(os.path.basename(file)).split(".")[0])
    wb = removeSheets(wb)
    createTeamsSheet(teams, wb)
    createPoolsSheets(teams, is_major, wb)


def createTeamsSheet(teams, wb):
    teamNames = ['Teams']
    playerOnes = ['Player One']
    playerTwos = ['Player Two']
    playerOnePoints = ['Player One Points']
    playerTwoPoints = ['Player Two Points']
    teamPoints = ['Team Points']

    for team in teams:
        teamNames.append(team.getTeamName())
        playerOnes.append(team.getPlayerOne().getName())
        playerOnePoints.append(team.getPlayerOne().getPoints())
        playerTwos.append(team.getPlayerTwo().getName())
        playerTwoPoints.append(team.getPlayerTwo().getPoints())
        teamPoints.append(team.getPlayerOne().getPoints() + team.getPlayerTwo().getPoints())
    data = [teamNames, playerOnes, playerTwos, playerOnePoints, playerTwoPoints, teamPoints]
    wb = writeToSheet(data, wb, "Teams")

    saveWorkBook(wb, 'pool_calculations.xlsx')


def createPoolsSheets(teams, is_major, wb):
    min_pools = math.floor(len(teams)/8)
    max_pools = math.ceil(len(teams)/4)
    num_pools = min_pools
    num_power_pools = getNumPowerPools(is_major, teams)

    # while num_pools < max_pools:
        # wb = writeToSheet(getPools(teams, num_pools, num_power_pools), wb, f"{num_pools + num_power_pools} Pools")
    pools = getPools(teams, num_pools, num_power_pools)
    for pool in pools:
        pool.printPool()
    num_pools += 1

    saveWorkBook(wb, 'pool_calculations.xlsx')


def getPools(teams, num_pools, num_power_pools):
    pools = []
    poolNum = 1
    change = REPEAT

    for i in range(num_pools + num_power_pools):
        pools.append(Pool(i+1))

    for i in range(len(teams)):
        print(f"I: {i}, Len: {len(teams)}")
        team = teams[i]
        pools[poolNum].addTeam(team)

        if i < 4*num_power_pools-2:
            if change != DECREASE:
                if change == 0:
                    if poolNum < num_power_pools:
                        poolNum += 1
                    else:
                        change = DECREASE
                else:
                    if poolNum > 1:
                        poolNum -= 1
                    else:
                        change = DECREASE
            else:
                if poolNum == num_power_pools:
                    change = INCREASE
                    poolNum -= 1
                else:
                    poolNum += 1
                    change = REPEAT
        elif i == 4*num_power_pools-1:
            poolNum = num_power_pools+1
            change = 0
        else:
            if change != DECREASE:
                if change == REPEAT:
                    if poolNum < num_pools:
                        poolNum += 1
                    else:
                        change = DECREASE
                else:
                    if poolNum > num_power_pools+1:
                        poolNum -= INCREASE
                    else:
                        change = DECREASE
            else:
                if poolNum == num_pools:
                    poolNum -= 1
                    change = INCREASE
                else:
                    poolNum += 1
                    change = REPEAT
        
    return pools


def getPowerPoolIndeces(num_power_pools):
    pools = {}
    print(f"Power Pools: {num_power_pools}")
    for i in range(num_power_pools):
        pools[i+1] = [i+1, 2*num_power_pools-i%num_power_pools, 2*num_power_pools+(i%num_power_pools)+1, 4*num_power_pools-i%num_power_pools]
    return pools



def getTeams(soup):
    teams = []
    teamNames = []
    playerOnes = []
    playerTwos = []
    points = getPoints()

    for team in soup.findAll('div', attrs = {'class':'team-name'}):
        teamNames.append(team.text)

    for team in soup.findAll('div', attrs = {'class':'players'}):
        players = team.text
        andIndex = players.find(" and ")
        playerOnes.append(Player(players[0:andIndex], getPlayerPoints(players[0:andIndex], points)))
        playerTwos.append(Player(players[andIndex+5:], getPlayerPoints(players[andIndex+5:], points)))

    for i in range(len(teamNames)):
        team = Team(teamNames[i], playerOnes[i], playerTwos[i])

        teams.append(team)
    return teams


def getNumPowerPools(is_major, teams):
    if is_major:
        if len(teams) < 9:
            return 0
        if len(teams) > 8 and len(teams) < 24:
            return 1
        if len(teams) > 23 and len(teams) < 44:
            return 2
        if len(teams) > 43 and len(teams) < 64:
            return 3
        if len(teams) > 63:
            return 4
    else:
        return 0


def getPlayerPoints(player, points):
    if player in points.keys():
        return points[player]
    return 0

 
def getPoints():
    wb = getWorkBook('./tracker/roundnet_season_tracker.xlsx')
    sheet = getSheetByName(wb, "Players")
    points = {}
 
    for i in range(sheet.max_row):
        key = sheet.cell(row=i+1, column=1).value
        points[str(key)] = sheet.cell(row=i+1, column=2).value

    return points


def readFile(file : str):
    with open(file, "r", encoding="utf8") as f:
        html_doc = f.readlines()
    return html_doc[0]

 
if __name__=="__main__":
    main()

