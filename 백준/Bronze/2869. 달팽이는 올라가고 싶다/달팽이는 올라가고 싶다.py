import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())
reach = (V-B-1)//(A-B)+1

print(reach)