pastas = []
resultadosG = []

def adicionar(n):
    for pasta in pastas:
        if(pasta[0] == n):
            if(pasta[2] != "0"):
                return adicionar(pasta[2]) + "\\" + pasta[1]
            else:
                return "\\" + pasta[1]
    return "roberto"


N = int(input())
for i in range(0,N):
    palavras = ""
    t = input()
    ITP = t.split(" ")
    for p in range(1, len(ITP)-1):
        palavras = palavras + ITP[p] + " " 
    palavras = palavras[:-1]
    pastas.append([ITP[0],palavras,ITP[len(ITP)-1]])

M = int(input())
for i in range(0,M):
    resultados = []
    NR = 0
    S = input()
    for pasta in pastas:
        if(pasta[1].find(S) != -1):
            if(pasta[2]!= "0"):
                resultados.append(adicionar(pasta[2]) + "\\" + pasta[1])
            else:
                resultados.append("\\" + pasta[1])
            NR = NR + 1
    if(NR == 0):
        resultadosG.append("NOT FOUND")
    else:
        resultados = sorted(resultados)
        for r in resultados:
            resultadosG.append(r)

for r in resultadosG:
            print(r)