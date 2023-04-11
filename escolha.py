vezes = 31
while True:
    n = input()
    n = int(n)
    if(n==-1):
        break
    if(n > vezes):
        print(vezes)
    else:
        print(vezes % n)