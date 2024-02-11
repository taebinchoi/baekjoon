App = 0
Baa = 0

for i in range(3, 0, -1):
  App += i * int(input())
for i in range(3, 0, -1):
  Baa += i * int(input())

if App == Baa:
  print('T')
elif App > Baa: 
  print('A')
else:
  print('B')