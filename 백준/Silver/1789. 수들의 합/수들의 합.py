S = int(input())

sum = 0
output = 0

for i in range(1, S+1):
  sum += i
  output += 1
  if sum>S:
    output -= 1
    break
    
print(output)