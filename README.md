Tugas Ketiga
Membuat Latihan Pertama, Kedua, dan Ketiga

1. Latihan Pertama

Menampilkan bilangan acak yang lebih kecil dari 0,5 serta menggunakan syntac perulangan dan random

1. Buka aplikasi Pycharm
2. Buka New Scratch File
![1](https://user-images.githubusercontent.com/46743068/53248143-9a903c80-36e7-11e9-86c7-3037734c676e.jpg)
3. ketik syntac Print('Bilangan Acak Yang Lebih Kecil Dari 0,5')
Kita gunakan sebagai Judul dari program yang akan kita buat
![2](https://user-images.githubusercontent.com/46743068/53248453-5d787a00-36e8-11e9-915d-26ae70038aa9.jpg)
4. Ketik Syntax :
import random
n = int(input("masukan Nilai N:"))

a. Import random
berfungsi meng-acak hasil dari perulangan yang akan kita buat

b. n = int(input("masukan Nilai N:"))
sedangkan untuk syntac ini kita gunakan untuk memasukan Variabel pada nilai N
![4](https://user-images.githubusercontent.com/46743068/53248728-f8715400-36e8-11e9-8336-064f8db269ad.jpg)
5. Ketik Syntax :                                                                                                               
a=0                                                                                                                             
for c in range(n) :

a. a=0
sebagai Variabel yang mana nanti gunakan untuk mengurutkan data

b. for c in range(n)
sebagai perintah perulangan data dari variabel (N)
![6](https://user-images.githubusercontent.com/46743068/53248780-1e96f400-36e9-11e9-8d1d-cbe24e2af8c0.jpg)
6. ketik Syntax :                                                                                                               
a+= 1                                                                                                                           
b = random.uniform(.0,.5)                                                                                                       
print('data ke:',a,'==>',b)                                                                                                     
print("selesai")

a. a+= 1 :                                                                                                                      
sebagai bentuk perintah untuk mengurutkan data yang kita buat sebelumnya                                                        

b. b = random.uniform(.0,.5) :                                                                                                  
digunakan sebagai variabel peng-acakan pada nilai (b)

c. print('data ke:',a,'==>',b) :                                                                                                 
digunakan untuk memunculkan hasil data (a) pengurutan dan (b) pengacakan

d. print("selesai") :                                                                                                           
memunculkan pernyataan bahwa hasil telah di temukan dan selesai

Dan jalankan syntax yang sudah di buat dengan menu RUN yang terdapat pada aplikasi Pycharm
![11](https://user-images.githubusercontent.com/46743068/53250915-fbbb0e80-36ed-11e9-89e8-1c2cadf150a6.jpg)
2. Latihan Kedua
Mencari bilangan dan menampilkan bilangan terbesar dari (n) sebuah data yang diinputkan.
Dan Memasukkan angka 0 untuk berhenti.

1. Ketikan Syntax :                                                                                                             
print('====== Menentukan Bilangan Terbesar ======')                                                                             
max=0                                                                                                                           
while True:                                                                                                                     
a=int(input('Masukkan bilangan = '))                                                                                            
if max < a                                                                                                                      
max = a                                                                                                                         
if a==0:                                                                                                                        
break                                                                                                                           
print('Bilangan terbesarnya adalah = ',max)

![b 1](https://user-images.githubusercontent.com/46743068/53249127-fa87e280-36e9-11e9-829d-fac11ffca5ae.jpg)

a. print('====== Menentukan Bilangan Terbesar ======') :
Digunakan untuk memberikan judul dari program yang akan dibuat

b. max=0
Di gunakan untuk memberikan varibel pada max

c. while True:
bentuk syntax Perulangan

d. a=int(input('Masukkan bilangan = '))
di gunakan untuk memasukan bilangan variabel pada nilai (a)

e. if max < a
f. max = a
Di gunakan sebagai penegasan bahwa jika max lebih kecil dari nilai(a) maka max = nilai(a)

g. if a==0:
h. break
dan ini di gunakan untuk perintah apabila nilai (a) di isi (0) maka pencarian nilai berhenti dengan menggunakan break

i. print('Bilangan terbesarnya adalah = ',max)
dan perintah ini untuk menampilkan hasil bilangan yang dimasukan dan terbesar

Pilih menu Run pada menu Pycharm untuk menjalankan hasil dari syntax yang kita buat                                             

![b2](https://user-images.githubusercontent.com/46743068/53249298-57839880-36ea-11e9-864d-bdbc8ddf1d81.jpg)                     

3. Latihan Ketiga

Membuat program sederhana dengan perulangan: "program1".py

1. Seorang pengusaha menginvestasikan uang untuk memulai usahanya dengan modal awal 100 juta,
2. pada bulan pertama dan kedua belum mendapatkan laba.
3. pada bulan ketiga baru mulai mendapatkan laba sebesar 1%
4. dan pada bulan ke 5, pendapatan meningkat 5%,
5. selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%
6. sehingga laba menjadi 3%. 7. Hitung total keuntungan selama 8 bulan berjalan usahanya.*

1.Ketikan syntax :

x=100000000                                                                                                                     
sum=0                                                                                                                           
y=0                                                                                                                             
lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) .5, int(x) * .5, int(x) * .5, int(x) .2]

print('modal awal seorang pengusaha :',x)

for i in lb :                                                                                                                 
sum=sum+i                                                 
y+=1                                                                                                                        
print('laba bulan ke-', y ,'sebesar :',i)

print('total laba yang di dapet adalah :',sum)
![c1](https://user-images.githubusercontent.com/46743068/53251254-d4b10c80-36ee-11e9-9c11-9551cbe8f0e4.jpg)
a. x=100000000                                                                                                                  
di gunakan untuk meberikan variabel pada nilai(x) sebagai modal awal

b. sum=0                                                                                                                        
Digunakan untuk memberikan variabel pada syntax penjumlahan(Sum)

c. y=0                                                                                                                          
Digunakan untuk memberikan variabel pada nilai (y) untuk mengurutkan keterangan laba pada bulan                                 

d. *lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) .5, int(x) * .5, int(x) * .5, int(x) .2]                             
menerangkan bahwa (lb) = hasil atau persenan dari modal awal

e. print('modal awal seorang pengusaha :',x)                                                                                    
menampilkan hasil dari hitungan laba di atas                                                                                    

f. for i in lb :                                                                                                                
syntax ini berfungsi mengulang dan memasukan laba ke dalam nilai(i)                                                             

g. sum=sum+i                                                                                                                    
menjumlah kan nilai laba yang berada di dalam nilai(i)                                                                      

h. y+=1                                                                                                                         
mengurutkan nilai pada laba,

i. print('laba bulan ke-', y ,'sebesar :',i)                                                                                    
menampilkan hasil dari variabel yang di dapat

j. print('total laba yang di dapet adalah :',sum)                                                                               
menampilkan hasil jumlahan variabel atau hasil laba

Pilih menu Run pada menu Pycharm untuk menjalankan hasil dari syntax yang kita buat
![c2](https://user-images.githubusercontent.com/46743068/53251578-92d49600-36ef-11e9-8b48-3106b3b4ff79.jpg)

SEKIAN TUGAS DARI SAYA

MUHAMMAD NASRUDIN
311810731
