incio = ""
fim = ""
n = int(input())

for i in range(0,n):
    if(incio==""):
        incio = "2"
    else:
        incio = incio + "0"
    fim = fim + "9"

for i in range(int(incio),int(fim)):
    v = 0
    t = str(i)
    for x in range(1,n+1):
        for y in range(2,int(t[:x])-1):
            if(t[:x] != str(y) and int(t[:x])%y == 0):
                v = v + 1
                break
        if(v>0):
            break
    if(v == 0):
        print(t)