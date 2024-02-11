from hashlib import sha256
N = input()

print(sha256(N.encode()).hexdigest()) #해시값 출력 참고사항