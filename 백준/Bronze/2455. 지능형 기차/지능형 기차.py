train = []
tot = 0

for i in range(4):
    I, O = map(int,input().split())
    tot = tot-I+O
    train.append(tot)
        
print(max(train))