# kondisional
# penggunaan kalkulator

# variable global
A = float(input("Masukan nilai A : ")) 
B = float(input("Masukan nilai B : ")) 
print("Masukan pilihan pekerjaan : ")
print("1.perkalian 2.pembagian 3.penjumlahan 4.pengurangan")
C = int(input())

# penggunaan if else kondisional
if C == 1 :
    D = int(A*B)
    print(f"hasil perkalian dari A x B adalah : {D}")
elif C == 2 :
    D = float(A/B)
    print(f"Hasil pembagian dari A / B adalah : {D}")
elif C == 3 :
    D = int(A+B)
    print(f"Hasil penjumlahan dari A + B adalah : {D}")
else :
    D = int(A-B)
    print(f"Hasil pengurangan dari A - B adalah : {D}")