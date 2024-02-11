N, A, B, C, D = map(int, input().split())

cost_X = (N // A) * B + (N % A != 0) * B
cost_Y = (N // C) * D + (N % C != 0) * D

print(min(cost_X, cost_Y))