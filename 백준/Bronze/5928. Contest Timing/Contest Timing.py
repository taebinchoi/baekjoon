D, H, M = map(int, input().split())

spend = (D-11)*1440 + (H-11)*60 + (M-11)
if spend >= 0:
    print(spend)
else:
    print(-1)