# bir şirket çalişanlari verilerini tutan dosya oluşturulacak.
# kullanicidan çalişan sayisi aldirilacak +
# çalişan sayisi kadar isim , soyisim , maaş bilgisi alinacak +
# dosyadaki her satira ad soyad - maaaş kalibinnda çalişan bilgileri eklenecek +
# programin sonunda bu dosyadan bilgileri satir satir okuyup listeleyecek kod yazilacak.
# Eklenen çalişanlar mevcut çalişanlari silmneyecek alt alta eklenecek.
#! try catch unutma : maaş ve çalişan adetini unutma.

try:
    workerCount=int(input("Çalişan sayisi giriniz : "))
except:
    print("Düzgün sayi giriniz")
    exit()

file=open("employees.txt","a+")    
for i in range(workerCount):
    name = str(input(f"{i+1}. çalişanin adini giriniz: "))
    lastName = str(input(f"{i+1}.çalişanin soyadini giriniz : "))
    salary = float(input(f"{i+1}.çalişanin maaşini giriniz : "))    
    file.write(f"{name} {lastName}-{salary}\n")
file.seek(0)
print(file.read())
file.close()




   



