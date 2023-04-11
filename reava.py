final = []

N = int(input())
for i in range(0,N):
    resultados = 0
    t = input()
    atividades = t.split(" ")
    for x in range(0,12):
        atividades[x] = float(atividades[x])
    atividades = sorted(atividades, reverse=True)
    for x in range(0,9):
        resultados = resultados + atividades[x]
    resultados = (resultados / 9) * 0.2
    resultados = (5.75 - resultados)/0.4
    if(resultados>10):
        final.append("REPROVADO")
    else:
        final.append(round(resultados,2))

for i in final:
    print(i)