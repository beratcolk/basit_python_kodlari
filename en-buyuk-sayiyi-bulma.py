"""
IF ELSE METODLARINI ÖĞRENMEK İÇİN BİR ALIŞTIRMADIR.
"""

#EN BÜYÜK SAYIYI BULMA.

sayi1 =  int(input("Sayi1: "))

sayi2 = int(input("Sayi2: "))

sayi3 = int(input("Sayi3: "))

if (sayi1 >= sayi2 and sayi1 >= sayi3):
    print("En büyük sayı:",sayi1)
elif (sayi2 >= sayi1 and sayi2 >= sayi3):
    print("En büyük sayı:",sayi2)
elif (sayi3 >= sayi1 and sayi3 >= sayi2):
    print("En büyük sayı:",sayi3)
    
