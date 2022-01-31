## 1) 정답
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     print("phone_book : ", phone_book)

#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             answer = False
#             break

#     return answer

## 2) 다른 사람 풀이 1 (zip)
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#     # print("zip : ", list(zip(phoneBook, phoneBook[1:])))
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print("p1 | p2 : ", p1 ,p2)
#         if p2.startswith(p1):
#             return False
#     return True

## 3) 다른 사람 풀이 2 (해시)
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print("hash_map : ", hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print("number | temp : ", number, temp, phone_number)
            if temp in hash_map and temp != phone_number:
                return False
    return answer

# phone_book = ["1195524421", "97674223", "119"]
phone_book = ["12","123","1235","567","88"]
# phone_book = ["123","456","789", "245"]
# phone_book = ["2","32","789"]


print(solution(phone_book))