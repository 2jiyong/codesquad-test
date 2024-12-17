# codesquad-test

## 공의 좌표 설정하기
공들의 x,y 좌표를 random함수로 뽑아 리스트에 저장한다.  
만약 좌표가 중복된다면 다시 뽑도록 한다.  
이 공들의 좌표는 추후 arr에 저장된다.  
처음엔 set를 사용해서 구현했는데, 추출된 값에 오류가 생겨 수정해야했지만, 시간이 부족해서 일단 리스트로만 구현했다.  

```python
def shuffleBalls():
    # balls=set()
    ballslist=[]
    while True:
        location=randomXY()
        if location not in ballslist:
            ballslist.append(location)
        if len(ballslist)==45:
            return ballslist
```


## 공 뽑기
10*10 arr배열에서 arr[9][9]에 값이 있다면 공을 뽑도록 한다.  
값이 없을 경우엔 값이 생길때까지 반복해서 섞는다.  
공을 뽑으면 현재 로또 상자를 출력하고, 뽑힌 공 리스트를 출력한다. 
