#def topla(say1,say2):
#    toplam = say1+say2
#    return toplam
#say1=input("Bir sayi giriniz : ")
#say2=input("ikinci sayi giriniz : ")
#print("------------------")
#print (topla(say1,say2))
#print("------------------")
#
"""
burda fonksiyondan cikan deger neyse onu basar.
i = 5
def f(arg=i):
    print(arg)
i=6
f()
en son fonksiyonu cagirdiginimiz icin 5 basar.

"""
# print("Oguz","Deneme","1998","Adana",sep=" ",end="\n",file=sys.stdout,flush=False)
# print fonksiyonun aldigi parametreler yukardaki gibidir. eger fonksiyon kullanmasaydik.
# her islemi kendimiz yapacatik.

#def kayit_ol(isim,sehir,meslek):
#    print("-"*30)
#    print("isim    : ",isim)
#    print("sehir   : ",sehir)
#    print("meslek  : ",meslek)
#    print("-"*30)
#    return "Kayit eklendi"
#print("kac kayit ekliceksiniz giriniz.")
#n = int(input(":"))
#while n > 0:
#    isim = input("Adiniz : ")
#    sehir= input("Sehir  : ")
#    meslek=input("Meslek : ")
#    print(kayit_ol(isim,sehir,meslek))
#    n -= 1
#
def toplama(*sayilar): #bu sekilde sonsuz parametre ekleyebilirz
    top = 0
    for i in sayilar:
        top += i
    print(top)

toplama(10,15,25)

