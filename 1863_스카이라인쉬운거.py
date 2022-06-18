n = int(input())
sky = []
for _ in range(n):
    sky.append(int(input().split()[1]))
visited = []
answer = 0
for i in range(len(sky)):
    if i in visited:
        continue
    now = sky[i]    
    if now == 0:
        continue
    for j in range(i+1,len(sky)):
        next_ = sky[j]
        if next_ > now:
            continue
        elif next_ == now:
            visited.append(j)
        else:
            break   
    answer += 1 
print(answer)
