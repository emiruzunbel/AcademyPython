#exception
#runtime exception ve compile-time exception olmak üzere iki farklı exception var.
try:
    examNote = float(input("Lütfen sınav notunuzu giriniz : "))
    print(examNote)
except ValueError:
    print("Deneme 123")
except ZeroDivisionError:
    print("Hiç bir sayı 0'a bölünemez")
except:
    print("Doğru bir girdi girmediniz")
finally:
    print("Try except bloğu düzgün bir şekilde çalıştı.")
