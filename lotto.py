def main():
    arr=makeArr()
    printArr(arr)


def printArr(arr):
    for elems in arr:
        for elem in elems:
            print(elem,end='')
        print()
        
def makeArr():
    arr=[['@']*10 for _ in range(10)]
    return arr

if __name__ == '__main__':
    main()