import numpy as np

matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

LineLength = len(matrix[0])
matrixLength = len(matrix) - 1
matrixLastIndex = LineLength - 1
matrixFirstIndex = 0

particleDirection = np.random.randint(0, 3)
print("move particle", particleDirection)

matrixLine = 0
print("matrixLine", matrixLine)

def generateParticle():
    generateParticle = np.random.randint(0, LineLength)
    matrix[0][generateParticle] = 1
    print("particle Gerated", generateParticle)
    print(matrix[0])
    return generateParticle


def particleDirection():
    particleDirection = np.random.randint(0, 3)
    print("move particle", particleDirection)
    return particleDirection

def moveToRigth(matrixLine, matrixFirstIndex):
    global currentIndex
    indexAfterMove = currentIndex
    if currentIndex == matrixFirstIndex:
        matrix[matrixLine][0] = 0
        matrix[matrixLine][matrixLastIndex] = 1
        print("particle moved throgh")
        indexAfterMove = matrixLastIndex
        return indexAfterMove 
    else:
        print("particle will move to rigth")
        matrix[matrixLine][currentIndex] = 0
        matrix[matrixLine][currentIndex - 1] = 1
        indexAfterMove -= 1
    return indexAfterMove

def moveToLeft(matrixLine, matrixLastIndex ):
    global currentIndex
    indexAfterMove = currentIndex
    if currentIndex == matrixLastIndex:
        print("particle moved throgh")
        matrix[matrixLine][matrixLastIndex] = 0
        matrix[matrixLine][0] = 1
        indexAfterMove = 0
        return indexAfterMove    
    else:
        print("particle will move to left")
        matrix[matrixLine][currentIndex] = 0
        matrix[matrixLine][currentIndex + 1] = 1 
        indexAfterMove += 1
        return indexAfterMove


def moveDown(matrixLine):

    indexAfterMove = currentIndex
    print("particle moved down")
    matrix[matrixLine][currentIndex] = 0
    matrix[matrixLine + 1][currentIndex] = 1
    return indexAfterMove


def moveParticle(particleDirection,matrixLine, matrixFirstIndex, matrixLastIndex): 
    global currentIndex
    if particleDirection == 0:
        currentIndex = moveToRigth(matrixLine, matrixFirstIndex)
    if particleDirection == 1:
        currentIndex = moveToLeft(matrixLine,  matrixLastIndex)
    if particleDirection == 2:
        currentIndex = moveDown(matrixLine,)





print("matrixLine here", matrixLine)



currentIndex = generateParticle()

Direction = particleDirection()


print("linha 1", matrix[0])
print("linha 2", matrix[1])
print("linha 2", matrix[2])
Direction = particleDirection()
moveParticle(Direction,matrixLine, matrixFirstIndex,matrixLastIndex)
print("linha 1", matrix[0])
print("linha 2", matrix[1])
print("linha 2", matrix[2])
