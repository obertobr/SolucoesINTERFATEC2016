dna = ""
while True:
    n = 0
    A = input()
    B = input()
    C = input()
    t = int(input())
    for i in range(0, len(A)-(t-1)):
        temp = A[i:i+t]
        if(B.find(temp) != -1 and C.find(temp) != -1):
            n=n+1
    print(n)