K = input()

if len(K)<=2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    N = 1
    M = int(K[0])-int(K[1])
    for i in range(1, len(K)-1):
        if int(K[i])-int(K[i+1]) != M:
            N = 0
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!" if N else "흥칫뿡!! <(￣ ﹌ ￣)>")