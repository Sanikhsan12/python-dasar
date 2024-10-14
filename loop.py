# loop atau perulangan
# dibagi 2 macam ada for dan while true 


# variable global
list_nama = ["ikhsan","akmal","tri"]
i = 0

# contoh penggunaan for
# for i in range(angka awal perulangan , angka akhir perulangan , increment):
for i in range(3):
    print(list_nama[i]) # print array berdasarkan indeks loop

# contoh penggunaan while 
while i < 3 :
    print(list_nama[i])
    i+=1 # increment ( i = i + 1)

# print list menggunakan for
cars = ["honda","toyota","suzuki"]
for car in cars:
    print(car)

# print list dan index dari array menggunakan enumerate
cars = ['hoda','toyota','bmw','audi']
for index, car in enumerate(cars):
    print(f'Index {index} = {car}')


