print("=" *41)
print("          Kalkulator Segitiga")
print("=" *41)

#INPUT DATA

Pilihan = input("Keliling (K) atau Luas (L): ").upper()
if Pilihan == 'K' :
    print("Kamu memilih Keliling")
    Sisi1 = float(input("Masukan Sisi Satu: "))
    Sisi2 = float(input("Masukan Sisi Dua: "))
    Sisi3 = float(input("Masukan Sisi Tiga: "))
    Keliling = Sisi1 + Sisi2 + Sisi3
    print(f"Jadi Keliling Nya Adalah {Keliling}")
elif Pilihan == 'L' :
    print("Kamu memilih Luas") 
    Panjang_Alas = float(input("Masukan Panjang Alas: "))
    Tinggi = float(input("Masukan Tinggi: "))
    Luas = 1/2 * Panjang_Alas * Tinggi
    print(f"Jadi Luas Nya Adalah {Luas}")
    

