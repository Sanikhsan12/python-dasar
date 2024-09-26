# tipe data
# penggunaan print harus 1 tipe data

# int
a = 10
b = 20
c = (b - a)
print(c)

# string 
a = "halo"
b = input("masukan nama anda : ")
print(a+b) 
print(a,b)
# kalo pake '+' hasilnya gk ada spasi
# kalo pake ',' hasilnua ada spasi

# boolean
a = True
b = False 
c = (a + b)
print(c)

# float
tinggi = 170
print("tinggi badan anda : " + tinggi + " cm") # penggunaan seperti ini salah
print("tinggi badan anda : "+ str(tinggi) + " cm") # alternatif 1 ( lebih ribet )
print(f"tinggi badan anda : {tinggi} cm") # alternatif 2 ( lebih rapih )

