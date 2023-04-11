#não finalizado

Ncasos = int(input())

for nc in range(0, Ncasos):
    jogo = []
    LA = input()
    LA = LA.split(" ")
    for i in range(0,int(LA[0])):
        jogo.append(input())
        if(jogo[i].find("J") != -1):
            J = [jogo[i].find("J") , i, 0]
        if(jogo[i].find("M") != -1):
            M = [jogo[i].find("M") , i, 0]
        if(jogo[i].find("B") != -1):
            B = [jogo[i].find("B") , i, 0]

    for rodadas in range(0,1000):
        if(int(LA[1]) >= B[1]+1):
            if(jogo[B[0]][B[1]+1]=="D"):
                B[3]= B[3] + 1
                break
            elif(jogo[B[0]][B[1]+1]!="#"):
                B[1] = B[1] + 1

        elif(0 <= B[1]-1 and jogo[B[0]][B[1]-1]=="D"):
            B[3]= B[3] + 1
            break
        elif(0 <= B[1]-1 and jogo[B[0]][B[1]-1]!="#"):
            B[1] = B[1] - 1

        elif(0 <= B[0]-1 and jogo[B[0]-1][B[1]]=="D"):
            B[3]= B[3] + 1
            break
        elif(0 <= B[0]-1 and jogo[B[0]-1][B[1]]!="#"):
            B[0] = B[0] - 1

        elif(int(LA[0]) >= B[0]+1 and jogo[B[0]+1][B[1]]=="D"):
            B[3]= B[3] + 1
            break
        elif(int(LA[0]) >= B[0]+1 and jogo[B[0]+1][B[1]]!="#"):
            B[0] = B[0] + 1
    print(B[3])
    print(jogo)
