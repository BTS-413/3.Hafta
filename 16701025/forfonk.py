def kacharf(kelime):
    for harf in kelime:
        print(harf,len(harf))
def lissira(liste):
    for ele in range(len(liste)):
        print(ele,liste[ele])
print("Kelime listesi olusturunuz")
print("quit yazarak cikis yapabilirisniz")
print("Olusan listeyi gormek icin 'lis' yazmaniz gerekir")
topkel = []
while True:
    kel = input("Kelimeleri giriniz :")
    topkel.append(kel)
    if kel == 'lis':
        topkel.remove('lis')
        lissira(topkel)
    if kel == 'quit':
        break
    print("Kelimelerin uzunlugu")
    kacharf(topkel)
