import copy
import tkinter
from tkinter import *
import threading
import time
import ComputerMoveScore
import MoveList
import Config

if __name__ == '__main__':

    Config.difficulty = "Easy"
    move = "OO"
    # Creates a Tkinter window with, an 8x8 grid of buttons for chess board, images for the pieces, and labels/buttons
    def initializeUI():
        global a8,a7,a6,a5,a4,a3,a2,a1,b8,b7,b6,b5,b4,b3,b2,b1,c8,c7,c6,c5,c4,c3,c2,c1,d8,d7,d6,d5,d4,d3,d2,d1, \
            e8,e7,e6,e5,e4,e3,e2,e1,f8,f7,f6,f5,f4,f3,f2,f1,g8,g7,g6,g5,g4,g3,g2,g1,h8,h7,h6,h5,h4,h3,h2,h1, \
            whiteKing, whiteQueen, whiteKnight, whiteBishop, whiteRook, whitePawn, \
            blackKing, blackQueen, blackKnight, blackBishop, blackRook, blackPawn, window, pixel,\
            firstLabel, secondLabel, easyButton, mediumButton, hardButton, boardButtons, images

        window = tkinter.Tk()
        window.geometry("830x600")

        whiteKing = PhotoImage(file = r"images\WKing.png").subsample(6,6)
        whiteQueen = PhotoImage(file = r"images\WQueen.png").subsample(6,6)
        whiteRook = PhotoImage(file = r"images\WRook.png").subsample(6,6)
        whiteBishop = PhotoImage(file = r"images\WBishop.png").subsample(6,6)
        whiteKnight = PhotoImage(file = r"images\WKnight.png").subsample(6,6)
        whitePawn = PhotoImage(file = r"images\WPawn.png").subsample(6,6)
        blackKing = PhotoImage(file = r"images\BKing.png").subsample(6,6)
        blackQueen = PhotoImage(file = r"images\BQueen.png").subsample(6,6)
        blackRook = PhotoImage(file = r"images\BRook.png").subsample(6,6)
        blackBishop = PhotoImage(file = r"images\BBishop.png").subsample(6,6)
        blackKnight = PhotoImage(file = r"images\BKnight.png").subsample(6,6)
        blackPawn = PhotoImage(file = r"images\BPawn.png").subsample(6,6)
        pixel = PhotoImage(width=1, height=1, file = r"images\BKing.png")

        a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,\
        e1,e2,e3,e4,e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,g7,g8,h1,h2,h3,h4,h5,h6,h7,h8\
        = Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),\
        Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window),Button(window)

        boardButtons = [[a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8],[c1,c2,c3,c4,c5,c6,c7,c8],[d1,d2,d3,d4,d5,d6,d7,d8],
                        [e1,e2,e3,e4,e5,e6,e7,e8],[f1,f2,f3,f4,f5,f6,f7,f8],[g1,g2,g3,g4,g5,g6,g7,g8],[h1,h2,h3,h4,h5,h6,h7,h8]]
        # Sets alternating button colors for chess board
        color = "grey"
        column,row = 0,7
        for buttonRows in boardButtons:
            for button in buttonRows:
                button.config(bg = color, height = 65, width = 65, image = pixel, command = lambda i = str(column) + str(7 - row): buttonPush(i))
                button.grid(column = column + 1, row = row)
                row -= 1
                if color == "white":
                    color = "grey"
                else:
                    color = "white"
                if row == -1:
                    column += 1
                    row = 7
                    if color == "white":
                        color = "grey"
                    else:
                        color = "white"
        aLabel= Label(window, text = "a", font=('Times 16'))
        aLabel.grid(column = 1, row = 8)
        bLabel= Label(window, text = "b", font=('Times 16'))
        bLabel.grid(column = 2, row = 8)
        cLabel= Label(window, text = "c", font=('Times 16'))
        cLabel.grid(column = 3, row = 8)
        dLabel= Label(window, text = "d", font=('Times 16'))
        dLabel.grid(column = 4, row = 8)
        eLabel= Label(window, text = "e", font=('Times 16'))
        eLabel.grid(column = 5, row = 8)
        fLabel= Label(window, text = "f", font=('Times 16'))
        fLabel.grid(column = 6, row = 8)
        gLabel= Label(window, text = "g", font=('Times 16'))
        gLabel.grid(column = 7, row = 8)
        hLabel= Label(window, text = "h", font=('Times 16'))
        hLabel.grid(column = 8, row = 8)
        oneLabel= Label(window, text = " 1 ", font=('Times 16'))
        oneLabel.grid(column = 0, row = 7)
        twoLabel= Label(window, text = "2", font=('Times 16'))
        twoLabel.grid(column = 0, row = 6)
        threeLabel= Label(window, text = "3", font=('Times 16'))
        threeLabel.grid(column = 0, row = 5)
        fourLabel= Label(window, text = "4", font=('Times 16'))
        fourLabel.grid(column = 0, row = 4)
        fiveLabel= Label(window, text = "5", font=('Times 16'))
        fiveLabel.grid(column = 0, row = 3)
        sixLabel= Label(window, text = "6", font=('Times 16'))
        sixLabel.grid(column = 0, row = 2)
        sevenLabel= Label(window, text = "7", font=('Times 16'))
        sevenLabel.grid(column = 0, row = 1)
        eightLabel= Label(window, text = "8", font=('Times 16'))
        eightLabel.grid(column = 0, row = 0)
        firstLabel = Label(window, text = "Choose Difficulty", font=('Times 16'))
        firstLabel.grid(column = 9, row = 1, sticky="w")
        secondLabel = Label(window, text = "", font=('Times 16'))
        secondLabel.grid(column = 9, row = 2, sticky="w")
        easyButton = Button(window, text = "EASY", bg = "grey", font=('Times 13'), fg = "white", command = lambda: difficultySetting(4))
        easyButton.grid(column = 9, row = 2)
        mediumButton = Button(window, text = "MEDIUM", bg = "grey", font=('Times 13'), fg = "white", command = lambda: difficultySetting(6))
        mediumButton.grid(column = 9, row = 3)
        hardButton = Button(window, text = "HARD", bg = "grey", font=('Times 13'), fg = "white", command = lambda: difficultySetting(8))
        hardButton.grid(column = 9, row = 4)
        window.mainloop()
    # Runs the processing of game for display on the UI
    def chess():
        global firstLabel,easyButton,mediumButton,hardButton,\
            bCastleLeft, bCastleRight, wCastleLeft, wCastleRight
        while(Config.It == 0):
            time.sleep(2)
        easyButton.destroy()
        mediumButton.destroy()
        hardButton.destroy()
        board = [['r','k','b','q','x','b','k','r','e'],
                 ['p','p','p','p','p','p','p','p','e'],
                 ['n','n','n','n','n','n','n','n','e'],
                 ['n','n','n','n','n','n','n','n','e'],
                 ['n','n','n','n','n','n','n','n','e'],
                 ['n','n','n','n','n','n','n','n','e'],
                 ['P','P','P','P','P','P','P','P','e'],
                 ['R','K','B','Q','X','B','K','R','e'],
                 ['e','e','e','e','e','e','e','e','e']]
        player = 'w'
        maxTurns = 0
        # Repeats for each human or computer turn until game ends or 220 turns reached
        while(maxTurns < 220):
            wPiecesLeft = piecesCounter(board, 'w')
            bPiecesLeft = piecesCounter(board, 'b')
            updateBoard(board)
            if(player == 'b'):
                firstLabel.config(text = "Black's Turn")
                board = computerTurn(board)
            else:
                firstLabel.config(text = "White's Turn")
                board = humanTurn(board)
            if player == 'w':
                player = 'b'
            else:
                player = 'w'
            maxTurns += 1
            # Checks if resulting move causes a check, checkmate, or stalemate
            if inCheck(board, 'b'):
                if inCheckmate(board, 'b'):
                    firstLabel.config(text = "You Have Won!")
                    updateBoard(board)
                    maxTurns = 221
                else:
                    bCastleRight = False
                    bCastleLeft = False
            if inCheck(board, 'w'):
                if inCheckmate(board, 'w'):
                    firstLabel.config(text = "You Have Lost.")
                    updateBoard(board)
                    maxTurns = 221
                else:
                    wCastleRight = False
                    wCastleLeft = False
            if inStalemate(board, player):
                firstLabel.config(text = "There is a stalemate.")
                maxTurns = 221
            # Checks if the recursion quantity in computer move calculation should be increased
            changeRecursionCount(bPiecesLeft, wPiecesLeft)
    # If the number of remaining pieces meets threshold, recursion quantity in ComputerMoveScore is increased
    def changeRecursionCount(bPiecesLeft, wPiecesLeft):
        piecesLeft = bPiecesLeft + wPiecesLeft
        match Config.difficulty:
            case "Easy":
                if piecesLeft < 12:
                    Config.It = 6
                elif piecesLeft < 7:
                    Config.It = 8
                if bPiecesLeft < 2 or wPiecesLeft < 2:
                    Config.nearEnd = True
                    Config.It = 8
            case "Medium":
                if piecesLeft < 12:
                    Config.It = 8
                elif piecesLeft < 7:
                    Config.It = 10
                if bPiecesLeft < 2 or wPiecesLeft < 2:
                    Config.nearEnd = True
                    Config.It = 10
            case "Hard":
                if piecesLeft < 12:
                    Config.It = 10
                elif piecesLeft < 7:
                    Config.It = 12
                if bPiecesLeft < 2 or wPiecesLeft < 2:
                    Config.nearEnd = True
                    Config.It = 14
    # Takes input from board's buttons indicating location of moving piece, or it's destination
    def buttonPush(loc):
        global move
        move = move + loc
    # Sets difficulty from easy to medium or hard if they're chosen
    def difficultySetting(n):
        # n is used in ComputerMoveScore for deciding recursion count in move calculation
        if n == 6:
            Config.difficulty = "Medium"
        if n == 8:
            Config.difficulty = "Hard"
        Config.It = n
    # Uses the 2D board array to update each UI button image with its piece's image
    def updateBoard(board):
        global boardButtons
        i,j = 0,0
        for rows in boardButtons:
            j = 0
            for pos in rows:
                match board[j][i]:
                    case 'n':
                        pos.config(image = pixel)
                    case 'P':
                        pos.config(image = blackPawn)
                    case 'K':
                        pos.config(image = blackKnight)
                    case 'B':
                        pos.config(image = blackBishop)
                    case 'Q':
                        pos.config(image = blackQueen)
                    case 'X':
                        pos.config(image = blackKing)
                    case 'R':
                        pos.config(image = blackRook)
                    case 'p':
                        pos.config(image = whitePawn)
                    case 'k':
                        pos.config(image = whiteKnight)
                    case 'b':
                        pos.config(image = whiteBishop)
                    case 'q':
                        pos.config(image = whiteQueen)
                    case 'x':
                        pos.config(image = whiteKing)
                    case 'r':
                        pos.config(image = whiteRook)
                j+=1
            i+=1
    # After coloring valid move options in yellow for UI, resets board colors to chess grid
    def resetBoardColors():
        global boardButtons
        color = "grey"
        i = 0
        j = 0
        for rows in boardButtons:
            j = 0
            for pos in rows:
                pos.config(bg = color)
                j+=1
                if color == "grey":
                    color = "white"
                else:
                    color = "grey"
            if color == "grey":
                color = "white"
            else:
                color = "grey"
            i+=1
    # Counts the number of input color's remaining pieces
    def piecesCounter(board, color):
        i,j,piecesCount = 0,0,0
        if color == 'b':
            pieceColors = Config.black
        else:
            pieceColors = Config.white
        while i < 8:
            j = 0
            while j < 8:
                if not board[j][i] == 'n' and not board[j][i] in pieceColors:
                    piecesCount += 1
                j+=1
            i+=1
        return piecesCount
    # Calculates the score of board based on the remaining piece's values and if each player is in check or checkmate
    # Positive score in human's favor and negative in computer's
    def boardScoreCounter(board):
        i,j,score = 0,0,0
        if inCheck(board, 'w'):
            if inCheckmate(board, 'w'):
                score -= 99
            else:
                score -= 1
        if inCheck(board, 'b'):
            if inCheckmate(board, 'b'):
               score += 99
            else:
                score += 1
        while(i < 8):
            j=0
            while(j < 8):
                match board[j][i]:
                    case 'p':
                        score += 1
                    case 'k':
                        score += 3
                    case 'b':
                        score += 3
                    case 'r':
                        score += 5
                    case 'q':
                        score += 8
                    case 'P':
                        score -= 1
                    case 'K':
                        score -= 3
                    case 'B':
                        score -= 3
                    case 'R':
                        score -= 5
                    case 'Q':
                        score -= 8
                j+=1
            i+=1
        return score
    # Checks if input player is not in check with inCheck() == False and all its possible moves result in check with
    # inCheckMate() == True indicating a stalemate
    def inStalemate(board, color):
        if not inCheck(board, color) and inCheckmate(board, color):
            return True
        return False
    # Locates input player's king and checks opponent's possible moves for any with a destination equal to king's
    # location indicating a check
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
            tempBoard = copy.deepcopy(board)
            tempBoard[int(move[3])][int(move[2])] = tempBoard[int(move[1])][int(move[0])]
            tempBoard[int(move[1])][int(move[0])] = 'n'
            if not inCheck(tempBoard, color):
                return False
        return True
    # Colors the possible move locations of the user's chosen piece to yellow
    def colorValidMoves(piecesMoves):
        global boardButtons
        for loc in piecesMoves:
            boardButtons[int(loc[0])][int(loc[1])].config(bg = "yellow")
    # Checks if the chosen move disqualifies castling for the player by taking a rook, moving a rook, moving a king,
    # or performing a castle move
    def castleInvalidator(tempBoard,destY,destX,initY,initX,color):
        if color == 'w':
            # Invalidates castle of side that rook is moved
            if tempBoard[destY][destX] == 'r' and initX == 0 and initY == 0:
                Config.wCastleLeft = False
            elif tempBoard[destY][destX] == 'r' and initX == 0 and initY == 7:
                Config.wCastleRight = False
            # Invalidates opponent castle of a side rook is taken
            elif destX == 7 and destY == 0:
                Config.bCastleLeft = False
            elif destX == 7 and destY == 7:
                Config.bCastleRight = False
            # Invalidates both side castling if king is moved and moves rook appropriately if castle performed
            elif tempBoard[destY][destX] == 'x':
                if destX - initX == 2:
                    tempBoard[0][5] = 'r'
                    tempBoard[0][7] = 'n'
                if initX - destX == 3:
                    tempBoard[0][2] = 'r'
                    tempBoard[0][0] = 'n'
                Config.wCastleLeft,Config.wCastleRight = False, False
        else:
            # Invalidates castle of side that rook is moved
            if tempBoard[destY][destX] == 'R' and initX == 7 and initY == 0:
                Config.bCastleLeft = False
            elif tempBoard[destY][destX] == 'R' and initX == 7 and initY == 7:
                Config.bCastleRight = False
            # Invalidates opponent castle of a side rook is taken
            elif destX == 0 and destY == 0:
                Config.wCastleLeft = False
            elif destX == 0 and destY == 7:
                Config.wCastleRight = False
            # Invalidates both side castling if king is moved and moves rook appropriately if castle performed
            elif tempBoard[destY][destX] == 'X':
                if destX - initX == 2:
                    tempBoard[7][5] = 'R'
                    tempBoard[7][7] = 'n'
                if initX - destX == 3:
                    tempBoard[7][2] = 'R'
                    tempBoard[7][0] = 'n'
                Config.bCastleLeft,Config.bCastleRight = False, False
        return tempBoard
    # Updates the information required for enPassant if it can be performed next move, updates board if enPassant
    # is performed, or turns pawn into queen if end of board is reached
    def enPassantData(tempBoard,destY,destX,initY,color):
        if (tempBoard[destY][destX]) == 'p':
            if color == 'w':
                # If destination is the end of board, pawn turned into queen
                if destY == '0':
                    tempBoard[destY][destX] = 'q'
                    Config.enPassantAllowed = False
                # If pawn has moved 2 spaces forward, enpassant may be perfomed on it next turn and data for it updated
                elif destY - initY == 2:
                    Config.enPassantAllowed = True
                    Config.enPassantPos = str(destX) + str(destY - 1)
                # If enpassant is performed on black's pawn, turns that pawns location to 'n'
                elif int(destX) == int(Config.enPassantPos[0]) and int(destY) == int(Config.enPassantPos[1]):
                    tempBoard[int(destY) - 1][int(Config.enPassantPos[0])] = 'n'
                    Config.enPassantAllowed = False
                else:
                    Config.enPassantAllowed = False
            else:
                # If destination is the end of board, pawn turned into queen
                if destY == '7':
                    tempBoard[destY][destX] = 'Q'
                    Config.enPassantAllowed = False
                # If pawn has moved 2 spaces forward, enpassant may be perfomed on it next turn and data for it updated
                elif initY - destX == 2:
                    Config.enPassantAllowed = True
                    Config.enPassantPos = str(destX) + str(destY + 1)
                # If enpassant is performed on black's pawn, turns that pawns location to 'n'
                elif int(destX) == int(Config.enPassantPos[0]) and int(destY) == int(Config.enPassantPos[1]):
                    tempBoard[int(destY) + 1][int(Config.enPassantPos[0])] = 'n'
                    Config.enPassantAllowed = False
                else:
                    Config.enPassantAllowed = False
        else:
            Config.enPassantAllowed = False
        return tempBoard
    # Takes input from user pushing buttons on UI board for moving
    def humanMoveInput(board):
        global secondLabel, move
        move = ""
        piecesMoves = []
        # Loops until two buttons are chosen resulting in 4 characters being in move
        while(len(move) < 4):
            time.sleep(.4)
            # Takes input from user button pushing for piece to move
            if len(move) == 2:
                match board[int(move[1])][int(move[0])]:
                    case 'x':
                        secondLabel.config(text = "Moving king")
                        piecesMoves = MoveList.king(board, move[0] + move[1])
                    case 'q':
                        secondLabel.config(text = "Moving queen")
                        piecesMoves = MoveList.queen(board, move[0] + move[1])
                    case 'b':
                        secondLabel.config(text = "Moving bishop")
                        piecesMoves = MoveList.bishop(board, move[0] + move[1])
                    case 'k':
                        secondLabel.config(text = "Moving knight")
                        piecesMoves = MoveList.knight(board, move[0] + move[1])
                    case 'r':
                        secondLabel.config(text = "Moving rook")
                        piecesMoves = MoveList.rook(board, move[0] + move[1])
                    case 'p':
                        secondLabel.config(text = "Moving pawn")
                        piecesMoves = MoveList.pawn(board, move[0] + move[1])
                    case _:
                        secondLabel.config(text = "Not your piece")
                        move = ""
                colorValidMoves(piecesMoves)
        resetBoardColors()
    # Has user input a move and if it is valid, move is performed and board is updated and returned
    def humanTurn(board):
        global wCastleLeft, wCastleRight, bCastleLeft, bCastleRight, secondLabel, move
        turnLoop = True
        # Continuously loops until a valid move is input by the user that is not in check
        while(turnLoop):
            humanMoveInput(board)
            tempBoard = copy.deepcopy(board)
            initX = int(move[0])
            initY = int(move[1])
            destX = int(move[2])
            destY = int(move[3])
            piece = board[initY][initX]
            validMove = False
            # Based on user's chosen piece, finds all valid moves and checks if attempted move is one of them
            match piece:
                case 'r':
                    validMoves = MoveList.rook(board, str(initX) + str(initY))
                    if str(destX) + str(destY) in validMoves:
                        tempBoard[destY][destX] = 'r'
                        validMove = True
                case 'k':
                    validMoves = MoveList.knight(board, str(initX) + str(initY))
                    if str(destX) + str(destY) in validMoves:
                        tempBoard[destY][destX] = 'k'
                        validMove = True
                case 'b':
                    validMoves = MoveList.bishop(board, str(initX) + str(initY))
                    if str(destX) + str(destY) in validMoves:
                        tempBoard[destY][destX] = 'b'
                        validMove = True
                case 'x':
                    validMoves = MoveList.king(board, str(initX) + str(initY))
                    if str(destX) + str(destY) in validMoves:
                        tempBoard[destY][destX] = 'x'
                        validMove = True
                case 'q':
                    validMoves = MoveList.queen(board, str(initX) + str(initY))
                    if str(destX) + str(destY) in validMoves:
                        tempBoard[destY][destX] = 'q'
                        validMove = True
                case 'p':
                    validMoves = MoveList.pawn(board, str(initX) + str(initY))
                    if str(destX) + str(destY) in validMoves:
                        if tempBoard[destY - 1][destX] == 'P' and tempBoard[destY][destX] == 'n':
                            tempBoard[destY - 1][destX] = 'n'
                        tempBoard[destY][destX] = 'p'
                        validMove = True
            tempBoard[initY][initX] = 'n'
            # If the attempted move is either not valid or results in check, loop repeats. If move is valid and doesn't
            # result in check, loop is broken.
            if inCheck(tempBoard, 'w'):
                secondLabel.config(text = "Cannot move into check")
            elif validMove:
                turnLoop = False
            else:
                secondLabel.config(text = "")
            validMove = False
        # Checks enPassantData for special case and to update board or enPassant information
        tempBoard = enPassantData(tempBoard,destY,destX,initY,'w')
        # Checks castleInvalidator for possibility that move causes either teams castle opportunities to be cancelled
        tempBoard = castleInvalidator(tempBoard,destY,destX,initY,initX,'w')
        return tempBoard
    # For each of black's moves, determines the score of the resulting board and stores it in an array
    def computerInitialMoveScores(validMoves,tempBoard,board):
        moveData = []
        for move in validMoves:
            tempScore = boardScoreCounter(board)
            tempBoard[int(move[3])][int(move[2])] = tempBoard[int(move[1])][int(move[0])]
            tempBoard[int(move[1])][int(move[0])] = 'n'
            # If black's move doesn't result in check, it's resulting board's score is updated if white piece is taken
            if not inCheck(tempBoard, 'b'):
                match board[int(move[3])][int(move[2])]:
                    case 'p':
                        tempScore -= 1
                    case 'k':
                        tempScore -= 3
                    case 'b':
                        tempScore -= 3
                    case 'q':
                        tempScore -= 8
                    case 'r':
                        tempScore -= 5
                    case 'P':
                        if int(move[3]) == 0:
                            tempScore -= 7
                moveData.append([tempBoard, tempScore, move])
            tempBoard = copy.deepcopy(board)
        return moveData
    # Performs the computers turn by calculating the highest potentially scoring move and updating the board with it
    def computerTurn(board):
        global wCastleLeft, wCastleRight, bCastleLeft, bCastleRight, secondLabel
        tempBoard = copy.deepcopy(board)
        score, bestMove = None, "0000"
        # Retrieves array of possible moves for black
        validMoves = MoveList.moves(board, 'b')
        # Retrieves array of arrays with each board, score, and move for each of the valid moves
        moveData = computerInitialMoveScores(validMoves,tempBoard,board)
        tempBoard = copy.deepcopy(board)
        # Retrieves the miniMax algorithm score for each move in moveData
        moveAndScoreList = ComputerMoveScore.main(moveData)
        # For each move and score, finds the lowest score and best move
        for moveAndScore in moveAndScoreList:
            move  = moveAndScore[0]
            tempScore = moveAndScore[1]
            # If the move's score is lower than the lowest score, replaces lowest score and best move
            if score is None or tempScore < score:
                score = tempScore
                bestMove = move
            # If scores are equal, firstly chooses new move if forward distances is equal but new move is closer
            # to board's center. Secondly, chooses new move if distance forward is greater than current best move but
            # less than 3 forward.
            elif tempScore == score:
                if ((int(bestMove[1]) - int(bestMove[3])) == (int(move[1]) - int(move[3]))) and int(bestMove[3]) >= int(move[3]) and abs(((int(bestMove[2]))) - 4) > abs(((int(move[2]))) - 4):
                    bestMove = move
                elif (int(bestMove[1]) - int(bestMove[3])) < (int(move[1]) - int(move[3])) and (int(move[1]) - int(move[3]))  < 3:
                    bestMove = move
        # Updates board with the found best move
        tempBoard[int(bestMove[3])][int(bestMove[2])] = tempBoard[int(bestMove[1])][int(bestMove[0])]
        tempBoard[int(bestMove[1])][int(bestMove[0])] = 'n'
        # Checks enPassantData for special case and to update board or enPassant information
        tempBoard = enPassantData(tempBoard,int(bestMove[3]),int(bestMove[2]),int(bestMove[1]),'b')
        # Checks castleInvalidator for possibility that move causes either teams castle opportunities to be cancelled
        tempBoard = castleInvalidator(tempBoard,int(bestMove[3]),int(bestMove[2]),int(bestMove[1]),int(bestMove[0]),'b')
        match board[int(bestMove[1])][int(bestMove[0])]:
            case 'P':
                piece = "pawn"
            case 'K':
                piece = "knight"
            case 'B':
                piece = "bishop"
            case 'R':
                piece = "rook"
            case 'Q':
                piece = "queen"
            case 'X':
                piece = "queen"
        secondLabel.config(text = "Black moved " + piece + " " + chr(ord(bestMove[0]) + 17) + str(int(bestMove[1]) + 1) + "-" + chr(ord(bestMove[2]) + 17) + str(int(bestMove[3]) + 1))
        return tempBoard

def main():
    threading.Thread(target = chess, daemon = True).start()
    initializeUI()

if __name__ == '__main__':
    main()