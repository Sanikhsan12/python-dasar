# array
# array itu berbasis indeks , dimana dimulai dari 0 ke n
# contoh array : umur = [10,20,30,40,50]
# dengan indeks masing" 0 -> 1 -> 2 -> dan seterusnya


# contoh penggunaan list array dengan 1 tipe data
nama = ["ikhsan","akmal","faris","tri"]
print(nama[1])

# contoh penggunaan banyak list array
ikhsan = ["nama : ikhsan ",",umur : 20 ", ",tinggi badan : 170 cm"]
akmal = ["nama : akmal ",",umur : 20 ", ",tinggi badan : 173 cm"]
tri = ["nama : tri ",",umur : 20 ", ",tinggi badan : 168 cm"]
print(ikhsan[0]+ikhsan[1]+ikhsan[2])
print(akmal[0]+akmal[1]+akmal[2])
print(tri[0]+tri[1]+tri[2])

# contoh penggunaan list array dengan banyak tipe data
arr = ["ikhsan ",20,170.0] # disini ada 3 tipe data [str,int,float]
print(f"{arr[0]} {arr[1]} {arr[2]}") # harus pake metode konversi data

# contoh penggunaan len untuk mengecek panjang data array
print(len(arr))