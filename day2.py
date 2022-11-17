print("2.Gün Başlangıç")

#Kullanıcıdan Girdi Alma : 
##########################
#Pyhton da input isimli bir fonksiyon kullanılırız.
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
    #Kullanıcıdan vize ve final notları alacak
    #Vize ve final notları 50.4 gibi ondalıklı sayılar olabilir.
    #Uygulama ortalamayı hesaplayacak ve ortalamaya göre
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
ortalama=((inputVize*0.40 + inputFinal*0.60))

if ortalama >=0 and ortalama <=49:
    print(f"Vize ve Final Sınavlarınızın Ortamalası :{ortalama} ve Harfli notunuz : FF")
elif ortalama >49 and ortalama <=60:
    print(f"Vize ve Final Sınavlarınızın Ortamalası :{ortalama} ve Harfli notunuz : DD")
elif ortalama >60 and ortalama <= 70:
    print(f"Vize ve Final Sınavlarınızın Ortamalası :{ortalama} ve Harfli notunuz : CC")
elif ortalama >70 and ortalama <=80:
    print(f"Vize ve Final Sınavlarınızın Ortamalası :{ortalama} ve Harfli notunuz : BB")
else :
    print(f"Vize ve Final Sınavlarınızın Ortamalası :{ortalama} ve Harfli notunuz : AA")


