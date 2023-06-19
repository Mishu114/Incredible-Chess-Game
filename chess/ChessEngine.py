import random
class GameState():
    def __init__(self):
        bb = [
            ["--","--","--","--","--","--","--","--"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["--","--","--","--","--","--","--","--"]
        ]
        sum=1
        while sum%3!=0:
            sum=0
            for i in range (8):
                x = random.randint(0,3)
                y = random.randint(x+2,7)
                sum = sum + (y-x-1)
                for j in range(8):
                    if j==x:
                        bb[j][i]="bp"
                    elif j==y:
                        bb[j][i]="wp"
                    else:
                        bb[j][i]="--"
        self.board = bb
        self.whiteToMove = True
        self.moveLog = []
        self.checkmate = False
        self.mx = 2

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    def getValidMoves(self):
        return self.getAllPossibleMoves()

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn=='b' and not self.whiteToMove):
                    self.getPawnMoves(r,c,moves)
        if len(moves)==0:
            self.checkmate = True
        return moves

    def getPawnMoves(self,r,c,moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c),(r-1,c),self.board))
            if self.board[r-1][c] == "--" and self.board[r-2][c] == "--":
                moves.append(Move((r,c),(r-2,c),self.board))
            if r+1<8:
                moves.append(Move((r,c),(r+1,c),self.board))
            if r+2<8:
                moves.append(Move((r,c),(r+2,c),self.board))

        else:
            if self.board[r + 1][c] == "--":
                moves.append(Move((r, c), (r + 1, c), self.board))
            if self.board[r + 1][c] == "--" and self.board[r + 2][c] == "--":
                moves.append(Move((r, c), (r + 2, c), self.board))
            if r - 1 >= 0:
                moves.append(Move((r, c), (r - 1, c), self.board))
            if r - 2 >= 0:
                moves.append(Move((r, c), (r - 2, c), self.board))



class Move():

    ranksToRows = {"1":7, "2":6, "3":5, "4":4,
                   "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a":0, "b":1, "c":2, "d":3,
                   "e":4, "f":5, "g":6, "h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol

    def __eq__(self, other):
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)

    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]