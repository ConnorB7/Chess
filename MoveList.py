import Config
# Cycles through board and for each piece matching color finds and adds all it's valid moves to array
def moves(board, color):
    fullValidMoves,validMoves = [],[]
    i,j = 0,0
    if color == 'w':
        color = Config.white
    else:
        color = Config.black
    while(i < 8):
        j=0
        while(j < 8):
            if board[j][i] in color:
                match board[j][i]:
                    case 'p':
                        validMoves = pawn(board,str(i) + str(j))
                    case 'k':
                        validMoves = knight(board,str(i) + str(j))
                    case 'b':
                        validMoves = bishop(board,str(i) + str(j))
                    case 'q':
                        validMoves = queen(board,str(i) + str(j))
                    case 'x':
                        validMoves = king(board,str(i) + str(j))
                    case 'r':
                        validMoves = rook(board,str(i) + str(j))
                    case 'P':
                        validMoves = pawn(board,str(i) + str(j))
                    case 'K':
                        validMoves = knight(board,str(i) + str(j))
                    case 'B':
                        validMoves = bishop(board,str(i) + str(j))
                    case 'Q':
                        validMoves = queen(board,str(i) + str(j))
                    case 'X':
                        validMoves = king(board,str(i) + str(j))
                    case 'R':
                        validMoves = rook(board,str(i) + str(j))
                for move in validMoves:
                    fullValidMoves.append(str(i) + str(j) + move)
            j+=1
        i+=1
    return fullValidMoves
# Based on board provided, adds all valid moves for the king to array
def king(board, pos):
    validMoves = []
    x,y = int(pos[0]),int(pos[1])
    # Sets up variables based on color of piece being moved
    if(board[y][x]) in Config.white:
        color = Config.black
        castleRight = Config.wCastleRight
        castleLeft = Config.wCastleLeft
        castleY = 0
    else:
        color = Config.white
        castleRight = Config.bCastleRight
        castleLeft = Config.bCastleLeft
        castleY = 7
    # If castling is still allowed and there are no pieces between king and rook adds castling move
    if castleRight is True and board[castleY][5] == 'n' and board[castleY][6] == 'n':
        validMoves.append(str(6) + str(castleY))
    if castleLeft is True and board[0][1] == 'n' and board[0][2] == 'n' and board[0][3] == 'n':
        validMoves.append(str(1) + str(castleY))
    # Allows king to move 1 space in all 8 directions if the space is blank or an enemy piece
    if board[y + 1][x + 1] in color or board[y + 1][x + 1] == 'n':
        validMoves.append(str(x + 1) + str(y + 1))
    if board[y + 1][x - 1] in color or board[y + 1][x - 1] == 'n':
        validMoves.append(str(x - 1) + str(y + 1))
    if board[y - 1][x + 1] in color or board[y - 1][x + 1] == 'n':
        validMoves.append(str(x + 1) + str(y - 1))
    if board[y - 1][x - 1] in color or board[y - 1][x - 1] == 'n':
        validMoves.append(str(x - 1) + str(y - 1))
    if board[y][x + 1] in color or board[y][x + 1] == 'n':
        validMoves.append(str(x + 1) + str(y))
    if board[y][x - 1] in color or board[y][x - 1] == 'n':
        validMoves.append(str(x - 1) + str(y))
    if board[y + 1][x] in color or board[y + 1][x] == 'n':
        validMoves.append(str(x) + str(y + 1))
    if board[y - 1][x] in color or board[y - 1][x] == 'n':
        validMoves.append(str(x) + str(y - 1))
    return validMoves
# Based on board provided, adds all valid moves for the queen to array
def queen(board, pos):
    validMoves = []
    tempY,tempX = int(pos[1]),int(pos[0])
    # Sets up color variable based on color of piece being moved
    if(board[tempY][tempX]) in Config.white:
        color = Config.black
    else:
        color = Config.white
    # Allows moves to be added in all 8 directions as long as space is blank or an enemy piece. If enemy piece is
    # encountered, spaces beyond it are not allowed.
    while tempY + 1 < 8 and tempX + 1 < 8:
        if(board[tempY + 1][tempX + 1]) == 'n':
            tempY += 1
            tempX += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY + 1][tempX + 1]) in color:
            validMoves.append(str(tempX + 1) + str(tempY + 1))
            tempY = 8
        else:
            tempY = 8
    # Resets location variables back to queen's location
    tempY,tempX = int(pos[1]),int(pos[0])
    while tempY - 1 > -1 and tempX + 1 < 8:
        if(board[tempY - 1][tempX + 1]) == 'n':
            tempY -= 1
            tempX += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY - 1][tempX + 1]) in color:
            validMoves.append(str(tempX + 1) + str(tempY - 1))
            tempY = -1
        else:
            tempY = -1
    tempY,tempX = int(pos[1]),int(pos[0])
    while tempY - 1 > -1 and tempX - 1 > -1:
        if(board[tempY - 1][tempX - 1]) == 'n':
            tempY -= 1
            tempX -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY - 1][tempX - 1]) in color:
            validMoves.append(str(tempX - 1) + str(tempY - 1))
            tempY = - 1
        else:
            tempY = -1
    tempY,tempX = int(pos[1]),int(pos[0])
    while tempY + 1 < 8 and tempX - 1 > -1:
        if(board[tempY + 1][tempX - 1]) == 'n':
            tempY += 1
            tempX -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY + 1][tempX - 1]) in color:
            validMoves.append(str(tempX - 1) + str(tempY + 1))
            tempY = 8
        else:
            tempY = 8
    tempY,tempX = int(pos[1]),int(pos[0])
    while(tempY - 1) > -1:
        if(board[tempY - 1][tempX]) == 'n':
            tempY -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY - 1][tempX]) in color:
            validMoves.append(str(tempX) + str(tempY - 1))
            tempY = -1
        else:
            tempY = -1
    tempY = int(pos[1])
    while(tempY + 1) < 8:
        if(board[tempY + 1][tempX]) == 'n':
            tempY += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY + 1][tempX]) in color:
            validMoves.append(str(tempX) + str(tempY + 1))
            tempY = 8
        else:
            tempY = 8
    tempY = int(pos[1])
    while(tempX - 1) > -1:
        if(board[tempY][tempX - 1]) == 'n':
            tempX -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY][tempX - 1]) in color:
            validMoves.append(str(tempX - 1) + str(tempY))
            tempX = -1
        else:
            tempX = -1
    tempX = int(pos[0])
    while(tempX + 1) < 8:
        if(board[tempY][tempX + 1]) == 'n':
            tempX += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY][tempX + 1]) in color:
            validMoves.append(str(tempX + 1) + str(tempY))
            tempX = 8
        else:
            tempX = 8
    return validMoves
# Based on board provided, adds all valid moves for the rook to array
def rook(board, pos):
    validMoves = []
    tempY,tempX = int(pos[1]),int(pos[0])
    # Sets up color variable based on color of piece being moved
    if(board[tempY][tempX]) in Config.white:
        color = Config.black
    else:
        color = Config.white
    # Allows moves to be added in 4 directions (up, down, left, right) as long as space is blank or an enemy piece.
    # If enemy piece is encountered, spaces beyond it are not allowed.
    while(tempY - 1) > -1:
        if(board[tempY - 1][tempX]) == 'n':
            tempY -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY - 1][tempX]) in color:
            validMoves.append(str(tempX) + str(tempY - 1))
            tempY = -1
        else:
            tempY = -1
    # Resets location variable back to rook's location
    tempY = int(pos[1])
    while(tempY + 1) < 8:
        if(board[tempY + 1][tempX]) == 'n':
            tempY += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY + 1][tempX]) in color:
            validMoves.append(str(tempX) + str(tempY + 1))
            tempY = 8
        else:
            tempY = 8
    tempY = int(pos[1])
    while(tempX - 1) > -1:
        if(board[tempY][tempX - 1]) == 'n':
            tempX -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY][tempX - 1]) in color:
            validMoves.append(str(tempX - 1) + str(tempY))
            tempX = -1
        else:
            tempX = -1
    tempX = int(pos[0])
    while(tempX + 1) < 8:
        if(board[tempY][tempX + 1]) == 'n':
            tempX += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY][tempX + 1]) in color:
            validMoves.append(str(tempX + 1) + str(tempY))
            tempX = 8
        else:
            tempX = 8
    return validMoves
# Based on board provided, adds all valid moves for the bishop to array
def bishop(board, pos):
    validMoves = []
    x,y = int(pos[0]),int(pos[1])
    tempY,tempX = y,x
    # Sets up color variable based on color of piece being moved
    if(board[y][x]) in Config.white:
        color = Config.black
    else:
        color = Config.white
    # Allows moves to be added in 4 diagonal directions as long as space is blank or an enemy piece.
    # If enemy piece is encountered, spaces beyond it are not allowed.
    while tempY + 1 < 8 and tempX + 1 < 8:
        if(board[tempY + 1][tempX + 1]) == 'n':
            tempY += 1
            tempX += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY + 1][tempX + 1]) in color:
            validMoves.append(str(tempX + 1) + str(tempY + 1))
            tempY = 8
        else:
            tempY = 8
    # Resets location variables back to bishop's location
    tempY,tempX = int(pos[1]),int(pos[0])
    while tempY - 1 > -1 and tempX + 1 < 8:
        if(board[tempY - 1][tempX + 1]) == 'n':
            tempY -= 1
            tempX += 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY - 1][tempX + 1]) in color:
            validMoves.append(str(tempX + 1) + str(tempY - 1))
            tempY = -1
        else:
            tempY = -1
    tempY,tempX = int(pos[1]),int(pos[0])
    while tempY - 1 > -1 and tempX - 1 > -1:
        if(board[tempY - 1][tempX - 1]) == 'n':
            tempY -= 1
            tempX -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY - 1][tempX - 1]) in color:
            validMoves.append(str(tempX - 1) + str(tempY - 1))
            tempY = -1
        else:
            tempY = -1
    tempY,tempX = int(pos[1]),int(pos[0])
    while tempY + 1 < 8 and tempX - 1 > -1:
        if(board[tempY + 1][tempX - 1]) == 'n':
            tempY += 1
            tempX -= 1
            validMoves.append(str(tempX) + str(tempY))
        elif(board[tempY + 1][tempX - 1]) in color:
            validMoves.append(str(tempX - 1) + str(tempY + 1))
            tempY = 8
        else:
            tempY = 8
    return validMoves
# Based on board provided, adds all valid moves for the knight to array
def knight(board, pos):
    validMoves = []
    x = int(pos[0])
    y = int(pos[1])
    # Sets up color variable based on color of piece being moved
    if(board[y][x]) in Config.white:
        color = Config.black
    else:
        color = Config.white
    # Checks if each of the 8 L shaped knight moves are possible. If a move is on the board and blank or an enemy
    # piece, move is allowed.
    if y + 2 < 8 and x - 1 > -1 and (board[y + 2][x - 1] in color or board[y + 2][x - 1] == 'n'):
        validMoves.append(str(x - 1) + str(y + 2))
    if y + 2 < 8 and x + 1 < 8 and (board[y + 2][x + 1] in color or board[y + 2][x + 1] == 'n'):
        validMoves.append(str(x + 1) + str(y + 2))
    if y + 1 < 8 and x - 2 > -1 and (board[y + 1][x - 2] in color or board[y + 1][x - 2] == 'n'):
        validMoves.append(str(x - 2) + str(y + 1))
    if y + 1 < 8 and x + 2 < 8 and (board[y + 1][x + 2] in color or board[y + 1][x + 2] == 'n'):
        validMoves.append(str(x + 2) + str(y + 1))
    if y - 2 > -1 and x - 1 > -1 and (board[y - 2][x - 1] in color or board[y - 2][x - 1] == 'n'):
        validMoves.append(str(x - 1) + str(y - 2))
    if y - 2 > -1 and x + 1 < 8 and (board[y - 2][x + 1] in color or board[y - 2][x + 1] == 'n'):
        validMoves.append(str(x + 1) + str(y - 2))
    if y - 1 > -1 and x - 2 > -1 and (board[y - 1][x - 2] in color or board[y - 1][x - 2] == 'n'):
        validMoves.append(str(x - 2) + str(y - 1))
    if y - 1 > -1 and x + 2 < 8 and (board[y - 1][x + 2] in color or board[y - 1][x + 2] == 'n'):
        validMoves.append(str(x + 2) + str(y - 1))
    return validMoves
# Based on board provided, adds all valid moves for the pawn to array
def pawn(board, pos):
    validMoves = []
    x = int(pos[0])
    y = int(pos[1])
    # If moving pawn is white, code below is performed
    if(board[y][x]) in Config.white:
        # If the computer player moved their pawn 2 spaces last turn, enpassant may be possible and code is implemented
        if Config.enPassantAllowed:
            # If pawn being moved is next to computer's pawn that just moved 2 spaces, enpassant move is added to array
            if x + 1 == int(Config.enPassantPos[0]) and y + 1 == int(Config.enPassantPos[1]):
                validMoves.append(str(x + 1) + str(y + 1))
            if x - 1 == int(Config.enPassantPos[0]) and y + 1 == int(Config.enPassantPos[1]):
                validMoves.append(str(x - 1) + str(y + 1))
        # If space 1 ahead of pawn is blank, 1 space move is added to array
        if board[y + 1][x] == 'n':
            validMoves.append(str(x) + str(y + 1))
        # If space 2 ahead of pawn is blank and pawn is in starting position, 2 space move is added to array
        if y + 2 < 8 and board[y + 2][x] == 'n' and board[y + 1][x] == 'n' and y == 1:
            validMoves.append(str(x) + str(y + 2))
        # If enemy piece is diagonally in front of pawn, diagonal attack move is added to array
        if board[y + 1][x - 1] in Config.black:
            validMoves.append(str(x - 1) + str(y + 1))
        if x + 1 < 8 and board[y + 1][x + 1] in Config.black:
            validMoves.append(str(x + 1) + str(y + 1))
    # If moving pawn is black, code below is performed
    else:
        # If the user moved their pawn 2 spaces last turn, enpassant may be possible and code is implemented
        if Config.enPassantAllowed:
            # If pawn being moved is next to user's pawn that just moved 2 spaces, enpassant move is added to array
            if x + 1 == int(Config.enPassantPos[0]) and y - 1 == int(Config.enPassantPos[1]):
                validMoves.append(str(x + 1) + str(y - 1))
            if x - 1 == int(Config.enPassantPos[0]) and y - 1 == int(Config.enPassantPos[1]):
                validMoves.append(str(x - 1) + str(y - 1))
        # If space 1 ahead of pawn is blank, 1 space move is added to array
        if board[y - 1][x] == 'n':
            validMoves.append(str(x) + str(y - 1))
        # If space 2 ahead of pawn is blank and pawn is in starting position, 2 space move is added to array
        if y - 2 > -1 and board[y - 2][x] == 'n' and board[y - 1][x] == 'n' and y == 6:
            validMoves.append(str(x) + str(y - 2))
        # If enemy piece is diagonally in front of pawn, diagonal attack move is added to array
        if board[y - 1][x - 1] in Config.white:
            validMoves.append(str(x - 1) + str(y - 1))
        if x + 1 < 8 and board[y - 1][x + 1] in Config.white:
            validMoves.append(str(x + 1) + str(y - 1))
    return validMoves