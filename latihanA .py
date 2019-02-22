print(' Bilangan Acak Yang Lebih Kecil Dari 0.5')
import random
n = int(input("masukan Nilai N:"))
a = 0
for c in range(n):
    a += 1
    b = random.uniform(.0, .5)
    print('data ke:', a, '==>', b)
print("selesai")
