import random
def findRandomMove(validMoves):
    return validMoves[random.randint(0,len(validMoves)-1)]

def findBestMove(validMoves, space):
    mod = space % 3
    for i in range(len(validMoves)):
        Move = validMoves[i]
        x = Move.endRow - Move.startRow
        if x == mod and x > 0:
            return Move
    return findRandomMove(validMoves)
