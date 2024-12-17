import random

def main():
    arr=makeArr()
    printArr(arr)
    a,b=randomXY()
    print(a,b)
    
def randomXY():
    return (random.randint(1,45),random.randint(1,45))

def printArr(arr):
    for elems in arr:
        for elem in elems:
            print(elem,end='')
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