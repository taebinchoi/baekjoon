from hashlib import sha512

N = input()
print(sha512(N.encode()).hexdigest())