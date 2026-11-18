# Program Kasir Kantin Kampus

print("=== KASIR KANTIN KAMPUS ===")

total_belanja = 0

# 4. Gunakan Perulangan
while True:
    # 1. Input Data
    nama = input("\nMasukkan nama makanan : ")
    
    if nama.lower() == "selesai":
        break
    
    harga = int(input("Masukkan harga makanan: Rp "))
    jumlah = int(input("Masukkan jumlah pembelian: "))

    # 2. Hitung Total per transaksi
    subtotal = harga * jumlah
    total_belanja = total_belanja + subtotal

    print(f"{nama} x {jumlah} = Rp {subtotal}")

# 3. Diskon
if total_belanja > 100000:
    diskon = total_belanja * 0.10
    print("\nAnda mendapatkan diskon 10%!")
else:
    diskon = 0
    print("\nTidak mendapatkan diskon.")

total_pembayaran = total_belanja - diskon

# 5. Hasil
print("\n===== STRUK PEMBAYARAN =====")
print(f"Total Belanja    : Rp {total_belanja}")
print(f"Diskon           : Rp {diskon}")
print(f"Total Pembayaran : Rp {total_pembayaran}")
print("Terima kasih sudah belanja!")