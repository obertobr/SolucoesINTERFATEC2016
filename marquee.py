t = input()
MT = t.split(" ")
texto = input()
E = input()
marquee = texto[:int(MT[0])]
j = 0
for i in range(0, int(E)):
    j = j + 1
    v = j + int(MT[0])
    if(v>int(MT[1])):
        j = j - int(MT[1])
        v = v - int(MT[1])
    marquee = marquee[1:]
    marquee = marquee + texto[v-1:v]
print(marquee)