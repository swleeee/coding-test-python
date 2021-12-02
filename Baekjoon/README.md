# BAEKJOON

## 다시 봐야 하는 문제

###### 1931.py

    - 회의실 배정
        * 핵심
        - 1) 정렬 => 끝나는시간의 오름차순
        - 2) 정렬 => 시작하는시간의 오름차순(끝-시 내림차순?)

###### 1715.py

    - 카드 정렬하기
        * 우선순위 큐

## 팁

###### input vs sys.stdin.readline

    1)
        - input() 내장 함수는 parameter로 prompt message를 받을 수 있음
        - sys.stdin.readline()은 prompt message를 인수로 받지 않음
    2)
        - input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴
        - sys.stdin.readline()은 개행 문자를 포함한 값을 리턴

    __결론__ => sys.stdin.readline()을 활용해서 입력을 받는 것이 좋음!

###### list의 마지막 요소

    - arr[len(arr)-1]
    - arr[-1]   => 중요

###### 우선순위 큐

    - 우선 순위가 가장 높은 data를 가장 먼저 꺼낼 수 있는 자료 구조
    - 입력 순서에 상관없이 우선순위에 따라 작동
    => 값이 입력되고 삭제될 때마다 자료구조가 내부적으로 정렬해줘야 하기 때문에
    구현 방법과 시간 복잡도에서 차이가 있음
    ※ 리스트 : 삽입 O(1) 삭제 O(N)
    ※ 힙 : 삽입 O(logN) 삭제 O(logN)
    ※ 스택, 큐 : 삽입 O(1) 삭제 O(1)

###### deque

    - 앞, 뒤 방향에서 element를 추가하거나 제거할 수 있음
    - push/pop 연산이 빈번한 알고리즘에서 리스트보다 월등한 속도를 자랑

    ```
        from collections import deque

        deq = deque()

        deq.appendleft(10)
        deq.append(0)
        deq.popleft()
        deq.pop()
    ```

## 랭크

- 2021-11-21
  - 브3 96
- 2021-11-22
  - 브3 116
- 2021-11-24
  - 실5 213
- 2021-12-01
  - 실5 279
- 2021-12-02
  - 실5 291
