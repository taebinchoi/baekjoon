from hashlib import sha384

N = input()
print(sha384(N.encode()).hexdigest())