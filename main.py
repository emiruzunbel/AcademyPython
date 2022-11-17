print("Merhaba Etiya")
# String : Metinsel ifadeler tutmamıza yarayan veri tipidir.
text ="Bu bir metindir."
print(text)

# integer : Tam sayı tipinde veriler tutmamızı sağlayan veri tipidir.
number = 5
print(number)

#double ,float ,decimal : Ondalıklı sayılar tutmamızı yarayan veri tipidir.
dnumber = 5.4
print(dnumber)

#bool : Doğru veya yanlış olmak üzere iki farklı geri dönüş sağlar.


#Matematiksel Operatörler : + , - , * , / , %
print(number + 5)
print(number - 5)
print(number * 5)
print(number / 5)
print(number % 5)

#Mantıksal Operatörler /Karşılaştırma Operatörleri : 
# Her mantıksal operatör boolean değer döner 
# < , > , <= , >=  , == , !=
print( 1==2 )
print( 1!=2 )
print( 2>3 )
print( 2<3 )
print( 2<=2)
print (2>=2)


#string Operasyonları :
text = "Merhaba Etiya"
#Upper Fonksiyonu : Yazılan metinsel ifadenin harflerini büyük olarak dönmesini sağlar.
print(text.upper())
#Lower Fonksiyonu : Yazılan metinsel ifadenin harflerini küçük olarak dönmesini sağlar.
print(text.lower())
#Startswith Fonksiyonu : Yazılan metnin belirtilen kısımla başlayıp başlamadığını gösterir .boolean değer döner.
print(text.startswith("Mer"))
#Endswith Fonksiyonu : Yazılan metnin belirtilen kısımla bitip bitmediğini gösterir .boolean değer döner.
print(text.endswith("a"))


name = "Emir"
age=27
company ="Etiya"

print(name + " " + age +" "+"yaşında" +" "+ company + "' da çalişiyor.")
print(f"{name} {age} yaşında {company}'de çalişiyor.")
print(age)


