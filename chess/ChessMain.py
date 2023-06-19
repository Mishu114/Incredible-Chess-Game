import pygame as p
from  chess import ChessEngine,SmartMoveFinder

WIDTH = HEIGHT = 680 #400 dileo valo
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # animation er jnno
IMAGES = {}

def loadImages():
    pieces = ['wp','bp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images-chess/images/" + piece +".png"),(SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    animate = True
    loadImages()
    running = True
    sqSelected = () #[tuple:(r,c)]
    playerClicks = [] # (r1,c1) --> (r2,c2)
    playerOne = True
    playerTwo = False
    gameOver = False
    firstMove = True
    while running:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = p.mouse.get_pos() # mouse er (x,y) location
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE

                    if sqSelected == (row,col):
                        sqSelected = ()
                        playerClicks =[]
                    else:
                        sqSelected = (row,col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks)==2:
                        move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                        if move in validMoves:
                            gs.makeMove(move)
                            moveMade = True
                        sqSelected = ()
                        playerClicks = []

            elif e.type == p.KEYDOWN:
                if e.key == p.K_r:
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False

        #AI move
        if not gameOver and not humanTurn:
            board = gs.board
            space = []
            sum =0
            for c in range(len(board)):
                r = 0
                r2 = 0
                for r in range(len(board)):
                    if board[r][c] == 'bp':
                        break
                for r2 in range (r+1,len(board)):
                    if board[r2][c] == 'wp':
                        break
                sum = sum + (r2-r-1)
                space.append(r2-r-1)

            print(sum)
            AIMove = SmartMoveFinder.findBestMove(validMoves,space)
            gs.makeMove(AIMove)
            moveMade = True

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1],screen,gs.board,clock)
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen,gs, validMoves,sqSelected)

        if gs.checkmate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen,'Black Won')
            else:
                drawText(screen, 'White Won')

        clock.tick(MAX_FPS)
        p.display.flip()


def highlightSquares(screen,gs, validMoves, sqSelected):
    if sqSelected != ():
        r,c = sqSelected
        if gs.board[r][c][0] == ( 'w' if gs.whiteToMove else 'b'):
            s = p.Surface((SQ_SIZE,SQ_SIZE))
            s.set_alpha(100)
            s.fill(p.Color('blue'))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            s.fill(p.Color('yellow'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s,(SQ_SIZE*move.endCol, SQ_SIZE*move.endRow))


def drawGameState(screen,gs,validMoves,sqSelected):
    drawBoard(screen) #draw squares on the board
    highlightSquares(screen,gs,validMoves,sqSelected)
    drawPieces(screen,gs.board)


def drawBoard(screen):
    global colors
    colors= [p.Color("#F0D9B5"),p.Color("#B58863")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece!= "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


def animateMove (move, screen, board, clock):
    global colors
    coords = []
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 8
    frameCount = (abs(dR) + abs(dC)) + framesPerSquare
    for frame in range(frameCount + 1):
        r,c = (move.startRow + dR*frame/frameCount, move.startCol + dC*frame/frameCount)
        drawBoard(screen)
        drawPieces(screen,board)
        color = colors[(move.endRow + move.endCol)%2]
        endSq = p.Rect(move.endCol*SQ_SIZE,move.endRow*SQ_SIZE,SQ_SIZE,SQ_SIZE)
        p.draw.rect(screen,color,endSq)
        screen.blit(IMAGES[move.pieceMoved],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)

def drawText(screen, text):
    font = p.font.SysFont("Helvitca",32,True,False)
    textObject = font.render(text,0,p.Color('Gray'))
    textLocation = p.Rect(0,0,WIDTH,HEIGHT).move(WIDTH/2 - textObject.get_width()/2,HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject,textLocation)
    textObject = font.render(text,0,p.Color('Black'))
    screen.blit(textObject,textLocation.move(2,2))


if __name__ == "__main__":
    main()
