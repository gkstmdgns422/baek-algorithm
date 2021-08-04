text = input()

acronym = ["U","C","P","C"] 
count = 0
i = 0
for letter in text: # 받은 text에서 한글자씩 추출
    if letter.isupper() and letter == acronym[i]: # 추출한 글자가 대문자, 약자에 속하는지 확인
        count += 1 
        i += 1 # 인덱스를 늘려가며 계산
        if count == 4:
            break # 중요 포인트 : UCPC가 되면 바로 스탑 이유는 UCPCC라는 예외사항이 존재할 수 있음
if count == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
