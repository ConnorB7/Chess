from typing import Any

import copy
from tkinter import *
from concurrent.futures import ProcessPoolExecutor
import MoveList
import Config

def main(inputList):
    if __name__ != "__mp_main__":
        # Using the boards, initial scores, and moves data as inputs for multiprocessing Minimax algorithm
        if not Config.nearEnd:
            x = 0
            recursionCount = [Config.It for i in range(len(inputList))]
            results = []
            boards = []
            scores = []
            m = []
            for elem in inputList:
                boards.append(elem[0])
                scores.append(elem[1])
                m.append(elem[2])
            with ProcessPoolExecutor(max_workers=61) as executor:
                result = executor.map(miniMax,boards,recursionCount,scores)
            for r in result:
                results.append([m[x],r])
                x += 1
            return results
        # If one of the players has two or fewer pieces left, the Minimax algorithm multiprocessing only takes four
        # processes at a time. If a path to checkmate is found by computer, no further processing is performed.
        else:
            i,x = 0,0
            results = []
            recursionCount = [Config.It for i in range(len(inputList))]
            while(i < len(inputList)):
                subList = []
                while(i < len(inputList)) and len(subList) < 4:
                    subList.append(inputList[i])
                    i += 1
                boards = []
                scores = []
                m = []
                for elem in subList:
                    boards.append(elem[0])
                    scores.append(elem[1])
                    m.append(elem[2])
                with ProcessPoolExecutor(max_workers=7) as executor:
                    result = executor.map(miniMax,boards,recursionCount,scores)
                for r in result:
                    results.append([m[x],r])
                    if r <= -99:
                        return results
                    x += 1
        return results
# If the input n is an even number the highest scoring white move's score is returned, if odd the lowest scoring black move's score
# is returned. White never has the last move as its input 'n' value for miniMax() is at least 1.
def miniMax(board, n, score):
    if n <= 0:
        if inCheck(board, 'w'):
            if inCheckmate(board, 'w'):
                return -99
        return score
    if n % 2 == 0:
        if inCheck(board, 'w'):
            if inCheckmate(board, 'w'):
                return -99 - n
        finalScore = -150
        validMoves = MoveList.moves(board, 'w')
        for move in validMoves:
            if finalScore >= 106 + n:
                return finalScore
            tempScore = score
            tempBoard = copy.deepcopy(board)
            tempBoard[int(move[3])][int(move[2])] = tempBoard[int(move[1])][int(move[0])]
            tempBoard[int(move[1])][int(move[0])] = 'n'
            # If pawn is moved to end of board, score increased for turning it into a queen
            if int(move[3]) == 7 and board[int(move[1])][int(move[0])] == 'p':
                tempScore += 7
            # If the move results in taking a black piece, score is increased and subtraction to recursion
            # count is lessened.
            if board[int(move[3])][int(move[2])] in Config.black:
                match board[int(move[3])][int(move[2])]:
                    case 'P':
                        tempScore += 1
                    case 'K':
                        tempScore += 3
                    case 'B':
                        tempScore += 3
                    case 'R':
                        tempScore += 5
                    case 'Q':
                        tempScore += 8
                if n - 3 > 0:
                    tempScore = miniMax(tempBoard, n - 3, tempScore)
                else:
                    tempScore = miniMax(tempBoard, 1, tempScore)
            else:
                if n - 5 > 0:
                    tempScore = miniMax(tempBoard, n - 5, tempScore)
                else:
                    tempScore = miniMax(tempBoard, 1, tempScore)
            # If the resulting score from miniMax is more than current highest score, replaces
            # higher score as it's better for black.
            if tempScore > finalScore:
                finalScore = tempScore
    else:
        if inCheck(board, 'b') and inCheckmate(board, 'b'):
                return 99 + n
        finalScore = 150
        validMoves = MoveList.moves(board, 'b')
        for move in validMoves:
            if finalScore <= -106 - n:
                return finalScore
            tempScore = score
            tempBoard = copy.deepcopy(board)
            tempBoard[int(move[3])][int(move[2])] = tempBoard[int(move[1])][int(move[0])]
            tempBoard[int(move[1])][int(move[0])] = 'n'
            # If pawn is moved to end of board, score decreased for turning it into a queen
            if int(move[3]) == 0  and board[int(move[1])][int(move[0])] == 'P':
                tempScore -= 7
            # If the move results in taking a white piece, score is decreased and subtraction to recursion
            # count is lessened.
            if board[int(move[3])][int(move[2])] in Config.white:
                match board[int(move[3])][int(move[2])]:
                    case 'p':
                        tempScore -= 1
                    case 'k':
                        tempScore -= 3
                    case 'b':
                        tempScore -= 3
                    case 'r':
                        tempScore -= 5
                    case 'q':
                        tempScore -= 8
                tempScore = miniMax(tempBoard, n - 3, tempScore)
            else:
                tempScore = miniMax(tempBoard, n - 5, tempScore)
            # If the resulting score from miniMax is less than current lowest score, replaces
            # lowest score as it's better for black.
            if tempScore < finalScore:
                finalScore = tempScore
    return finalScore
# Locates input player's king and checks opponent's possible moves for any with a destination equal to king's
# location and indicating a check
def inCheck(board, color):
    i,j,x,y = 0,0,0,0
    if color == 'b':
        king = 'X'
        opponent = 'w'
    else:
        king = 'x'
        opponent = 'b'
    while(i < 8):
        j=0
        while(j < 8):
            if board[j][i] == king:
                x = i
                y = j
            j += 1
        i += 1
    validMoves = MoveList.moves(board, opponent)
    for move in validMoves:
        if int(move[3]) == y and int(move[2]) == x:
            return True
    return False
# Attempts all valid moves of input player and uses inCheck to see if any of these result in player not being
# in check
def inCheckmate(board, color):
    validMoves = MoveList.moves(board, color)
    for move in validMoves:
        tempBoard: Any = copy.deepcopy(board)
        tempBoard[int(move[3])][int(move[2])] = tempBoard[int(move[1])][int(move[0])]
        tempBoard[int(move[1])][int(move[0])] = 'n'
        if not inCheck(tempBoard,color):
            return False
    return True
