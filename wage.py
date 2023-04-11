t = input()
valores = t.split(" ")
HBV = float(valores[0])
HEV = float(valores[1])
QH = float(valores[2])
DPB = float(valores[3])
DPE = float(valores[4])
CT = float(valores[5])

BR = 0
ES = 0

R = ((HBV * QH) - (HBV * QH)*(DPB/100))
BR = (BR + R)*1.01
BR = (BR + R)*1.01
BR = (BR + R)*1.01
R = (((HEV * QH) - (HEV * QH)*(DPE/100)) * CT)
ES = (ES + R)*1.01
ES = (ES + R)*1.01
ES = (ES + R)*1.01

print(str(round(BR,2))+"BR "+str(round(ES,2))+"ES")