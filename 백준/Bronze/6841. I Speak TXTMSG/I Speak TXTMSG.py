emo = ["CU", ":-)", ":-(", ";-)", ":-P", "(~.~)", "TA", "CCC", "CUZ", "TY", "YW", "TTYL"]
tex = ["see you", "I’m happy", "I’m unhappy", "wink", "stick out my tongue", "sleepy", "totally awesome", "Canadian Computing Competition", "because", "thank-you", "you’re welcome", "talk to you later"]
while True:
    txt = input()
    if txt in emo:
        print(tex[emo.index(txt)])
    else:
        print(txt)
    if txt == "TTYL":
        break