# function
# penggunaan function dalam kalkulator

# variable global
A = float(input("Masukan nilai A : ")) 
B = float(input("Masukan nilai B : ")) 
print("1.perkalian 2.pembagian 3.penjumlahan 4.pengurangan")
C = int(input("Masukan pilihan pekerjaan : "))

# func perkalian 
def perkalian():
    D = int(A*B)
    print(f"hasil perkalian dari A x B adalah : {D}")

# func pembagian
def pembagian():
    D = float(A/B)
    print(f"Hasil pembagian dari A / B adalah : {D}")

# func penjumlahan
def penjumlahan():
    D = int(A+B)
    print(f"Hasil penjumlahan dari A + B adalah : {D}")

# func pengurnagan
def pengurangan():
    D = int(A-B)
    print(f"Hasil pengurangan dari A - B adalah : {D}")


# kondisonal (hanya improvisasi)
if C == 1 :
    perkalian()
elif C == 2 :
    pembagian()
elif C == 3 :
    penjumlahan()
else :
    pengurangan()