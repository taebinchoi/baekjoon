def pho(str1, str2, str3):
    if set([str1[0], str2[0], str3[0]]) == {'l', 'k', 'p'}:
        return 'GLOBAL'
    else:
        return 'PONIX'

str1 = input()
str2 = input()
str3 = input()

res = pho(str1[0], str2[0], str3[0])
print(res)
