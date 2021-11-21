# BAEKJOON

## 다시 봐야 하는 문제

###### 1931.py

    - 회의실 배정
        * 핵심
        - 1) 정렬 => 끝나는시간의 오름차순
        - 2) 정렬 => 시작하는시간의 오름차순(끝-시 내림차순?)

## 팁

###### input vs sys.stdin.readline

    1)
        - input() 내장 함수는 parameter로 prompt message를 받을 수 있음
        - sys.stdin.readline()은 prompt message를 인수로 받지 않음
    2)
        - input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴
        - sys.stdin.readline()은 개행 문자를 포함한 값을 리턴

    __결론__ => sys.stdin.readline()을 활용해서 입력을 받는 것이 좋음!

## 랭크

- 2021-11-11
  - 브3 96
