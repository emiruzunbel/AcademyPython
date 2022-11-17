print("2.Gün Başlangiç")

#Kullanicidan Girdi Alma : 
##########################
#Pyhton da input isimli bir fonksiyon kullaniliriz.
userInput=input()
print(f"Girilen Değer : {userInput}")


#Type Conversion :
##########################
numberStr="10"
print(type(numberStr))
number = int(numberStr)
print(number)
print(type(number))

userInput=input()
lessonNote=float(userInput)
print(f"Ders Notunuz : {lessonNote}")

#Conditinoals
if lessonNote>50:
    print("Geçtiniz")
elif lessonNote==50:
    print("Sinidra geçtiniz.")
elif lessonNote == 49:
    print("Sinirda kaldiniz.")
else:
    print("Kaldiniz")

    #Workshop1
    ##################
    #Kullanicidan vize ve final notlari alacak
    #Vize ve final notlari 50.4 gibi ondalikli sayilar olabilir.
    #Uygulama ortalamayi hesaplayacak ve ortalamaya göre
    #Vize 0.40 , final 0.60 etki edecektir.
    #0-49 FF 
    #50-60 DD
    #60-70 CC
    #70-80 BB
    #80-100 AA



print("Vize Notunuzu giriniz.")
inputVize=float(input())
print("Final Notunuzu giriniz.")
inputFinal=float(input())
meanGrade=((inputVize*0.40 + inputFinal*0.60))

if meanGrade >=0 and meanGrade <=49:
    print(f"Vize ve Final Sinavlarinizin Ortamalasi :{meanGrade} ve Harfli notunuz : FF")
elif meanGrade >49 and meanGrade <=60:
    print(f"Vize ve Final Sinavlarinizin Ortamalasi :{meanGrade} ve Harfli notunuz : DD")
elif meanGrade >60 and meanGrade <= 70:
    print(f"Vize ve Final Sinavlarinizin Ortamalasi :{meanGrade} ve Harfli notunuz : CC")
elif meanGrade >70 and meanGrade <=80:
    print(f"Vize ve Final Sinavlarinizin Ortamalasi :{meanGrade} ve Harfli notunuz : BB")
else :
    print(f"Vize ve Final Sinavlarinizin Ortamalasi :{meanGrade} ve Harfli notunuz : AA")


#WORKSHOP 2 
##################
print("Lütfen ortalamasini hesaplamak istediğiniz derslerin adetini giriniz.")
lessonQuantity =int(input())
count=0
successList=[]
failedList=[]



while 0<lessonQuantity:
    midtermGrade=float(input("Vize notunu giriniz : "))
    finalGrade=float(input("Final notunu giriniz :"))
    meanGrade=midtermGrade*0.40 +finalGrade*0.60
    if meanGrade<=50:
        print("Kaldiniz")
        count +=1
        failedList.append([count,meanGrade])
        
    elif 50<meanGrade<=100:
        print("Geçtiniz")
        count +=1
        successList.append([count,meanGrade])
        
    else:
        print("Geçersiz değer girdiniz.")
    lessonQuantity-=1

print(f"Başarili olduğunuz dersler {successList}")
print(f"Başarisiz olduğunuz dersler {failedList}")
    


#For Döngüsü :

for i in range(6):
    print(i)

students = ["Nilüfer","Özlem","Berk","Zakir"]
for i in students:
    print(i)

