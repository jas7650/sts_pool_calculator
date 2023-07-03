import math
import os
import sys
from bs4 import BeautifulSoup
import openpyxl
from tracker.utils.sheet_utils import *
import subprocess
import argparse
 
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
    teams = mergeSort(teams)
    
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
        teamNames.append(team[0])
        playerOnes.append(team[1])
        playerOnePoints.append(team[2])
        playerTwos.append(team[3])
        playerTwoPoints.append(team[4])
        teamPoints.append(team[5])
    data = [teamNames, playerOnes, playerTwos, playerOnePoints, playerTwoPoints, teamPoints]
    wb = writeToSheet(data, wb, "Teams")

    saveWorkBook(wb, 'pool_calculations.xlsx')


def createPoolsSheets(teams, is_major, wb):
    if is_major == True:
        wb = writeToSheet(getPools(teams, 4, True), wb, "Pools of 4")
        wb = writeToSheet(getPools(teams, 5, True), wb, "Pools of 5")
    else:
        wb = writeToSheet(getPools(teams, 4, False), wb, "Pools of 4")
        wb = writeToSheet(getPools(teams, 5, False), wb, "Pools of 5")
        wb = writeToSheet(getPools(teams, 6, False), wb, "Pools of 6")
        wb = writeToSheet(getPools(teams, 7, False), wb, "Pools of 7")

    saveWorkBook(wb, 'pool_calculations.xlsx')


def getPools(teams, pool_size, is_major):
    change = 0
    numPools = int(math.ceil((len(teams)-1)/pool_size))
    numPowerPools = getNumPowerPools(is_major, teams)
    pools = ['Pool']
    teamNames = ['Team Name']
    playerOnes = ['Player One']
    playerTwos = ['Player Two']
    poolNum = 1

    print(f"Pool Size: {pool_size}")
    print(f"Num Pools: {numPools}")
    print(f"Num Power Pools: {numPowerPools}")
    print()

    
    for i in range(len(teams)):
        team = teams[i]
        pools.append(poolNum)
        teamNames.append(team[0])
        playerOnes.append(team[1])
        playerTwos.append(team[3])

        if i < pool_size*numPowerPools-2:
            if change != 2:
                if change == 0:
                    if poolNum < numPowerPools:
                        poolNum += 1
                    else:
                        change = 2
                else:
                    if poolNum > 1:
                        poolNum -= 1
                    else:
                        change = 2
            else:
                if poolNum == numPowerPools:
                    change = 1
                    poolNum -= 1
                else:
                    poolNum += 1
                    change = 0
        elif i == pool_size*numPowerPools-1:
            poolNum = numPowerPools+1
            change = 0
        else:
            if change != 2:
                if change == 0:
                    if poolNum < numPools:
                        poolNum += 1
                    else:
                        change = 2
                else:
                    if poolNum > numPowerPools+1:
                        poolNum -= 1
                    else:
                        change = 2
            else:
                if poolNum == numPools:
                    poolNum -= 1
                    change = 1
                else:
                    poolNum += 1
                    change = 0
        
    return [pools, teamNames, playerOnes, playerTwos]


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
        playerOne = players[0:andIndex]
        playerTwo = players[andIndex+5:]
        playerOnes.append(playerOne)
        playerTwos.append(playerTwo)

    for i in range(len(teamNames)):
        team = []
        team.append(teamNames[i])
        team.append(playerOnes[i])
        playerOnePoints = getPlayerPoints(playerOnes[i], points)
        team.append(playerOnePoints)
        team.append(playerTwos[i])
        playerTwoPoints = getPlayerPoints(playerTwos[i], points)
        team.append(playerTwoPoints)
        team.append(playerOnePoints + playerTwoPoints)
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


def mergeSort(teams : list):
    if len(teams) == 1:
        return [teams[0]]
    else:
        index = int(len(teams)/2)
        left = mergeSort(teams[:index])
        right =  mergeSort(teams[index:])
        return merge(left, right)


def merge(left : list, right : list):
    l = 0
    r = 0
    sorted_list = []
    while l < len(left) and r < len(right):
        if left[l][5] < right[r][5]:
            sorted_list.append(right[r])
            r += 1
        else:
            sorted_list.append(left[l])
            l += 1
    while l < len(left):
        sorted_list.append(left[l])
        l += 1
    while r < len(right):
        sorted_list.append(right[r])
        r += 1
    return sorted_list

 
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

