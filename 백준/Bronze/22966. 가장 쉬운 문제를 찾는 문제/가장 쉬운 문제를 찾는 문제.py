N = int(input())
quiz = {}
for i in range(N):
    title, score = input().split()
    score = int(score)
    title = title.upper()
    quiz[title] = score

min_score_title = min(quiz, key=quiz.get)

print(min_score_title)