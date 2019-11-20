def giris(giris, deneme=4, hatirlatma="tekrar deneyiniz" ):
    while True:
        ok = input(giris)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop'):
            return False
        deneme = deneme - 1
        if deneme < 0:
            print("Hatali giris")
            exit()
            #raise ValueError('Gecersiz')
        print(hatirlatma)
giris('devam etmek istiyormusunuz = ')
