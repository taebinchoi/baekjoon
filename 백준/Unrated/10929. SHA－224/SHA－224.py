from hashlib import sha224

N = input()
print(sha224(N.encode()).hexdigest())