#Open ile dosyayı açabiliyoruz içine hangi dosyayı açacağımızı söylüyoruz
file =open("sample.txt")

#Write: file.write komutu ile yazabiliyoruz. 
#\n ile alt satıra geçirebiliriz.
#append = üzerine ekleme 
#read = okuma
file.writelines("\ndeneme")
print(file.read())

file.close()


