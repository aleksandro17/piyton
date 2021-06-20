 1. set variabel kota, jarak, ongkirperkm, totongkir
  File "<stdin>", line 1
    1. set variabel kota, jarak, ongkirperkm, totongkir
       ^
SyntaxError: invalid syntax
>>> 2. input pilihan kota
  File "<stdin>", line 1
    2. input pilihan kota
       ^
SyntaxError: invalid syntax
>>> 3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
  File "<stdin>", line 1
    3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
       ^
SyntaxError: invalid syntax
>>> jika kota Bdg, jarak = 452, ongkirperkm=4000
  File "<stdin>", line 1
    jika kota Bdg, jarak = 452, ongkirperkm=4000
         ^
SyntaxError: invalid syntax
>>> 4. totongkir = jarak * ongkirperkm
  File "<stdin>", line 1
    4. totongkir = jarak * ongkirperkm
       ^
SyntaxError: invalid syntax
>>> 5. tampilkan kota, totongkir
  File "<stdin>", line 1
    5. tampilkan kota, totongkir
       ^
SyntaxError: invalid syntax
>>> """
... print ("=============================================")
... print(" TRANSKASI BIAYA EKSPEDISI ")
... print ("=============================================")
... print(" Kode = A. Surabaya")
... print(" Kode = B. Bandung")
... print ("=============================================")
...
... #jika menggunakan list Kode dibawah ini, maka metode yang digunakan
... #adalah mendeteksi indeks value yang terpilih pada list kode.
... #caranya: melakukan pencarian pada list kode menggunakan
... # nilai kode yang diinputkan
... #salah satu metode : gunakan while
... kode =['a','b']
... #algoritma:
... # baca berulang2 index dalam list kode, jika value sama dengan
... # value pilihan, ambil index nya
...
... kota = ['surabaya','bandung']
... jarak = [169,452]
... ongkirperkm = [2500,4000]
...
... pilihan = input(">> Masukkan Kode Tujuan = ")
... #identifikasi pilihan
... if pilihan=="a":
...     idx = 0
... elif pilihan=="b":
...     idx = 1
... else:
...     idx = 0
...
... #cetak tampilan layar
... print(">>> Pilihan Tujuan = " + kota[idx])
... print(">>> Jarak          = " + str(jarak[idx]) + " km")
... print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))
...
... #hitung transksi
... fixjarak = jarak[idx]
... fixongkirkm = ongkirperkm[idx]
... totongkir = fixjarak * fixongkirkm
...
... #tampilkan total ongkir
... print(">>>-------------------------------------")
... print(">>> Total Biaya     = Rp." + str(totongkir))
