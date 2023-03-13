import csv
import datetime
from Decorator import *
from subClasses import *

#Menu yu oluşturmak



 #Pizzayı seçmek için switch case mantığı   
def switcher(secilenPizzaTabanı):
    pizzalar = {
        "klasik" : Klasik(),
        "margarita":Margarita(),
        "turkpizza":TurkPizza(),
        "sadepizza":SadePizza()
    }
    print(f"pizza tabanı secimi: {secilenPizzaTabanı.capitalize()}\n")
    
    return pizzalar.get(secilenPizzaTabanı)

#Ana fonksyon
def main():
    print("Menu :")
    #Menuyu yazdırma
    txt = "* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik/n2: Margarita /n3: TürkPizza /n4: Sade Pizza/n* ve seçeceğiniz sos:/n1: Zeytin/n2: Mantar/n3: Keçi Peyniri /n4: Et \n5: Soğan/n6: Mısır/n* Teşekkür ederiz!"
    txt = txt.replace("/n","\n")
    with open("Menu2.txt","w") as dosya:
        dosya.write(txt)
    with open("Menu2.txt","r") as Menu:
        pizzalar = Menu.readlines()
        for i in range(1,5):
            print(pizzalar[i])


    secilenPizza = ""
    
    print("Lütfen bir pizza tabanı secimi yapınz:\n")
    #Pizza isteğine göre pizzanın kaydedilmesi ve pizza objesi oluşturma
    while(True):
        secilenPizza = str(input()).replace(" ","").strip().lower()
        if secilenPizza.lower() == "klasik" or secilenPizza == "1" or secilenPizza == "2" or secilenPizza ==  "margarita" or secilenPizza ==   "3" or  secilenPizza== "türkpizza" or secilenPizza ==  "4" or secilenPizza ==  "sadepizza":
            break
        else:
            print("Lütfen Geçerli bir pizza tabanı ismi yazınız !!\n")

    sonSecilenPizzaTabanı = switcher(secilenPizza.lower())

    print("Lütfen ek malzeme seçimi yapınız\n")
    #Menuyu yazdırma
    with open("Menu2.txt","r") as Menu:
        pizzalar = Menu.readlines()
        for i in range(6,12):
            print(pizzalar[i])
    #Malzeme ekleme mantığı - malzemeler kısmından her bir malzeme seçildiğinde bu listeden silinir ve eklendi lsitesinde bir objesi oluşur.
    malzemeler = ["zeytin","mantar","kecipeyniri","et","soğan","misir"]
   
    eklendi = []
    #Malzeme varlığı check edildi 
    secilenEkMalzeme = str(input()).lower().strip().replace(" ","")
    while(secilenEkMalzeme !="sipariş ver" or len(eklendi) == 6):
        if secilenEkMalzeme == "zeytin":
            zeytin = Zeytin()
            if not"zeytin" in malzemeler:
                print("Zeytin zaten ekli\n")
            else:
                eklendi.append(zeytin)
                malzemeler.remove("zeytin")
                print(f"Zeytin eklendi")
        elif secilenEkMalzeme == "mantar":
            mantar = Mantar()
            if not"mantar" in malzemeler:
                print("Mantar zaten ekli\n")
            else:
                eklendi.append(mantar)
                malzemeler.remove("mantar")
                print("Mantar eklendi\n")
        
        elif secilenEkMalzeme == "keçipeyniri":
            kecipeyniri = KeciPeyniri()
            if not"kecipeyniri" in malzemeler:
                print("Kecipeyniri zaten ekli\n")
            else:
                eklendi.append(kecipeyniri)
                malzemeler.remove("kecipeyniri")
                print("Kecipeyniri eklendi\n")
        elif secilenEkMalzeme == "et":
            et = Et()
            if not"et" in malzemeler:
                print("Et zaten ekli\n")
            else:
                eklendi.append(et)
                malzemeler.remove("et")
                print("Et eklendi\n")
        
        elif secilenEkMalzeme == "soğan":
            sogan = Sogan()
            if not"soğan" in malzemeler:
                print("Soğan zaten ekli\n")
            else:
                eklendi.append(sogan)
                malzemeler.remove("soğan")
                print("Soğan eklendi\n")
        
        elif secilenEkMalzeme == "mısır":
            misir= Misir()
            if not"misir" in malzemeler:
                print("Mısır zaten ekli\n")
            else:
                eklendi.append(misir)
                malzemeler.remove("misir")
                print("Mısır eklendi\n")
        elif len(eklendi) == 6:
            print("Malzeme sınırına ulaştınız")
            break
        elif secilenEkMalzeme =="siparişver":
            break            
        else:
            print("Lütfen Geçerli bir ek malzeme ismi yazınız !!\n")
        print("Sipariş vermek için sipariş ver yazınız ya da malzeme eklemeye devam edebilirsiniz!!\n")
        secilenEkMalzeme = str(input()).lower().strip().replace(" ","")
    #Sipariş tutarı hesaplandı ve klass methodları kullanıldı
    siparisTutarı = 0 
    for malzeme in eklendi:
        siparisTutarı += malzeme.get_cost()
    siparisTutarı += sonSecilenPizzaTabanı.get_cost()
    print(f"Sipariş tutarı:{siparisTutarı}\nSipariş açıklaması:\n-Pizza Tabanı:{sonSecilenPizzaTabanı.get_description()}\n-Ek malzemeler:",end=" ")
    for i in eklendi:
        print(i.get_description(),end=", ")
    
    print()

    print("Lütfen siparişi onaylamak için İsim, Tc no ve Kredi kartı numaranızı ve şifrenizi yazınız ")

    print("İsminiz : ")
    isim = str(input())
    
    print("Lütfen tc no'nuzu giriniz : ")
    tcNo = str(input())
    while(len(tcNo)!=11):
        if(len(tcNo)<11):
            print("tc no 11 haneden az olamaz")
            tcNo = str(input())
        elif(len(tcNo)>11):
            print("tc no 11 haneden fazla olamaz")
            tcNo = str(input())

    print("Lütfen kredi kartı numaranızı giriniz:")

    krediKartıNo = str(input())
    while(len(krediKartıNo)!=11):
        if(len(krediKartıNo)<11):
            print(" no 11 haneden az olamaz")
            krediKartıNo = str(input())
        elif(len(krediKartıNo)>11):
            print("tc no 11 haneden fazla olamaz")
            krediKartıNo= str(input())

    print("Kedi kartı şifreniz: ")
    krediKartıŞifresi = input()
    ekMalzemelerStringList = []
    
    for i in eklendi:
        ekMalzemelerStringList.append(i.get_description())

    siparisTarihi = datetime.datetime.now()    

    #Csv ye yazmak için datalar bir listeye aktarıldı
    fieldnames = ['isim','tc_no','krediKartı_no','krediKartı_şifre','sipariş_zamanı','Secilen_pizza_tabanı','Secilen_ek_malzemeler']

    dataList =[isim,tcNo,krediKartıNo,krediKartıŞifresi,siparisTarihi,sonSecilenPizzaTabanı.get_description(),ekMalzemelerStringList]
    #dosya açıldı ve yazıldı
    with open ('Orders_database.csv',mode = "w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerow(dataList)
       
    
    print("Teşekkür ederiz")
            
if __name__ == "__main__":
    main()



    







