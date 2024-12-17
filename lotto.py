import random

def main():
    arr=makeArr()
    balls=shuffleBalls()
    for i in range(45):
        x,y=balls[i]
        arr[x][y]=i+1
    printArr(arr)

def shuffleBalls():
    balls=[]
    for i in range(45):
        location=randomXY()
        balls.append(location)
    return balls

def randomXY():
    return (random.randint(1,10),random.randint(1,10))

def printArr(arr):
    for elems in arr:
        for elem in elems:
            if not elem == ' ' and elem!='-' and elem!='+' and elem!='|':
                print(f'[{elem:2}]',end='')
            elif elem != ' ':
                if elem == '-':
                    print(elem*4,end='')
                else:
                    print(elem,end='')
            else:
                print('    ',end='')
        print()
        
def makeArr():
    arr=[[' ']*12 for _ in range(12)]
    for i in range(12):
        for j in range(12):
            if i==0 or i==11:
                arr[i][j]='-'
            if j==0 or j==11:
                arr[i][j]='|'
            if (i==0 or i==11) and (j==0 or j==11):
                arr[i][j]='+' 
    return arr

if __name__ == '__main__':
    main()