sugar = int(input()) 
total = 0 

while sugar >= 0:
    if not sugar % 5: # 5의 배수인지 확인
        total += sugar // 5 
        print(total)
        break
    sugar -= 3 # 아니라면 3을 빼가며 5의 배수인지 확인
    total += 1
else: # 결과가 -부호가 뜨면 3과 5로 만들 수 없는 수로 판단
    print(-1) 

    