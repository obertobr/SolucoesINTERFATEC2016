while True:
    heap = []
    v = 1
    vp = 1
    resultado=""

    def retornar(a):
        for i in heap:
            if(i[0] == a):
                return i[1]

    t = input()
    l = t.split(" ")
    heap.append([1,int(l[1]),1])
    for i in range(2, int(l[0])+1,2):
        v=v+1
        vp=vp+1
        heap.append([vp,int(l[i]),v-1])
        if(len(l) < i+2):
            break
        vp=vp+1
        heap.append([vp,int(l[i+1]),v-1])

    heap.reverse()
    for i in heap:
        if(i[0] != 1):
            if(i[1] < retornar(i[2])):
                if(resultado == ""):
                    resultado = "max"
                elif(resultado == "min"):
                    resultado = "nada"
            elif(i[1] > retornar(i[2])):
                if(resultado == ""):
                    resultado = "min"
                elif(resultado == "max"):
                    resultado = "nada"
            else:
                resultado = "nada"
    print(resultado)