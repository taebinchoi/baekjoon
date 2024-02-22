while True:
  N = int(input())
  if N == -1:
    break
  num = 2
  M = [1]
  for i in range(2, N):
    if N%i == 0:
      M.append(i)
  tot = str(N) + " = 1" 
  if N == sum(M):
    for j in range(1, len(M)):
      tot += " + " + str(M[j])
    print(tot)
  else:
    print(str(N) + " is NOT perfect.")