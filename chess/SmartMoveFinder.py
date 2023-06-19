import random
def findRandomMove(validMoves):
    return validMoves[random.randint(0,len(validMoves)-1)]

def CalculateVal(space):
    x = 0
    for i in range(len(space)):
        x = x^(space[i]%3)
    return x


def findBestMove(validMoves, space):
    front = 0
    theMove = validMoves[0]
    endState = [0,0,0,0,0,0,0,0]
    for i in range(len(validMoves)):
        Move = validMoves[i]
        moveSq = Move.endRow - Move.startRow
        if moveSq>0:
            if moveSq > endState[Move.startCol]:
                endState[Move.startCol] = moveSq
                theMove = Move

    for i in range(len(endState)):
        if endState[i]>0:
            front = front + 1

    if front == 1:
        return theMove

    x = CalculateVal(space)
    if x==0:
        return findRandomMove(validMoves)
    else:
        for i in range(len(validMoves)):
            Move = validMoves[i]
            tmpSpace = space
            moveSq = Move.endRow - Move.startRow
            if moveSq>0:
                tmpSpace[Move.startCol] = tmpSpace[Move.startCol] - moveSq
            else:
                continue
            val = CalculateVal(tmpSpace)
            if val == 0:
                return Move
        return findRandomMove(validMoves)


