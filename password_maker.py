import random

# Parola karakterlerini tanımlayın
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Kullanıcıdan parola uzunluğunu alın
parola_uzunlugu = int(input("Parola uzunluğunu girin: "))

# Parolayı saklayacak değişkeni oluşturun
parola = ""

# Parola uzunluğu kadar döngü oluşturarak rastgele karakterler ekleyin
for i in range(parola_uzunlugu):
    rastgele_karakter = random.choice(characters)
    parola += rastgele_karakter

# Oluşturulan parolayı ekrana yazdırın
print("Oluşturulan Parola:", parola)
