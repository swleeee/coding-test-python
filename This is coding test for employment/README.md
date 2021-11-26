# 이것은 취업을 위한 코딩 테스트다 (with Python)

## 폴더 설명

#### ch3 : 그리디 이론

#### ch11 : 그리디 문제

###### 만들 수 없는 금액

###### 볼링공 고르기

###### 무지의 먹방 라이브

        - heapq
            - Min Heap의 구조
            - 가장 작은 요소가 heap[0]에 위치
            - 모든 k에 대해 heap[k] <= heap[2*k+1] or heap[k] <= heap[2*k+2] 만족

#### ch4 : 구현 이론

#### ch12 : 구현 문제

###### 문자열 압축

#### 1

```
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
```

#### 2

```
    heapq.heappush(q, (food_times[i], i+1))
    q[0][0]
    heapq.heappop(q)[0]
```
