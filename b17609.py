import sys
T = int(sys.stdin.readline())

for tc in range(T):
    word = sys.stdin.readline().rstrip()
    N = len(word)
    left_word = list(word)
    right_word = list(word)
    if word == word[::-1]: # 이전과 동일하게 회문확인
        print(0)
    else:                  # 유사회문 인지 판별
        i = 0
        while True:        # 기존 방식은 모든 값을 하나씩 빼서 구분했지만 새로운 방식은 왼쪽 오른쪽 구분해서 시간복잡도를 낮춤
            if word[i] != word[N-1-i]: #왼쪽 오른쪽 구분해야함
                left_word.pop(i)
                right_word.pop(N-1-i)
                if left_word == left_word[::-1] or right_word == right_word[::-1]:
                    print(1)
                    break
                else:
                    print(2)
                    break
            else:
                i += 1


# 시간 초과
# 아마도 word의 길이가 100,000이라 최적화가 필요한듯함.
for tc in range(T):
    word = sys.stdin.readline().rstrip()
    N = len(word)
    
    if word == word[::-1]:
        print(0)
    else:
        for i in range(N):
            letter = list(word)
            letter.pop(i)
            if letter == letter[::-1]:
                print(1)
                break
        else:
            print(2)

