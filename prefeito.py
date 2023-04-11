# Uma implementação recursiva ingênua
#Nº de 0-1 Problema da mochila
 
# Retorna o valor máximo que
# pode ser colocado em uma mochila de
# capacidade W
def knapSack(W, wt, val, n):
 
    # caso base
    if n == 0 or W == 0:
        return 0
 
    # Se o peso do item N for
    # mais que Mochila de capacidade W,
    # então este item não pode ser incluído
    # na solução ótima
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # retornar o máximo de dois casos:
    # (1) n item incluído
    # (2) não incluído
    else:
        return max(
            val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),knapSack(W, wt, val, n-1))
 
Ncasos = int(input())

for nc in range(0, Ncasos):
    wt = []
    val = []
    t = input()
    TL = t.split(" ")
    W = int(TL[0])
    for i in range(0, int(TL[1])):
        t = input()
        CV = t.split(" ")
        wt.append(int(CV[0]))
        val.append(int(CV[1]))
    print(knapSack(W, wt, val, len(val)))