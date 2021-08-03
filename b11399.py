people_num = int(input())
time = input()

time = list(map(int,time.split()))
time.sort()
total = 0
for i in range(people_num+1):
    total += sum(time[:i])
print(total)