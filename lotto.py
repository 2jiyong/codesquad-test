import random

def main():
    # arr=makeArr()
    winningBalls=[]
    while len(winningBalls)!=6:
        arr=makeArr()
        balls=shuffleBalls()
        for i in range(1,46):
            if i in winningBalls:
                continue
            x,y=balls[i-1]
            arr[x][y]=i  
        if checkingWinnigBall(arr):
            printArr(arr)
            num=arr[9][9]
            winningBalls.append(num)
            print(winningBalls)

def checkingWinnigBall(arr):
    if arr[9][9]==' ':
        return False
    return True

def shuffleBalls():
    # balls=set()
    ballslist=[]
    while True:
        location=randomXY()
        if location not in ballslist:
            ballslist.append(location)
        if len(ballslist)==45:
            return ballslist
        # balls.add(location)
        # if len(balls)==45:
        #     return list(balls)

def randomXY():
    return (random.randint(0,9),random.randint(0,9))

def printArr(arr):
    print('+'+'-'*40+'+')
    for elems in arr:
        print('|',end='')
        for elem in elems:
            if not elem == ' ':
                print(f'[{elem:2}]',end='')
            else:
                print('    ',end='')
        print('|')
    print('+'+'-'*40+'+')
    
def makeArr():
    arr=[[' ']*10 for _ in range(10)]
    return arr

if __name__ == '__main__':
    main()