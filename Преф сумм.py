# задачки номер 1
mgrgr= int(input())
for i in range(mgrgr):
    dlina,mazila = map(int,input().split())
    otvet = [0]*26
    stroca = input()
    testi = list(map(int,input().split()))
    prsum = [0]*dlina
    for i in testi:
        prsum[i-1] += 1
    for i in range(2,dlina):
        prsum[dlina-i] += prsum[dlina-i+1]
    prsum[0]+=prsum[1]
    for i in range(dlina):
        otvet[ord(stroca[i])-97] += prsum[i] + 1
    print(*otvet)

