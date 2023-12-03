class Mobil:
    def __init__(self, merk, harga_sewa):
        self.merk = merk
        self.harga_sewa = harga_sewa
        self.status = "tersedia"
    
    def __str__(self):
        return f"{self.merk} (Harga sewa: {self.harga_sewa}/hari)"
    
class RentalMobil:
    def __init__(self):
        self.daftar_mobil = []
    
    def tambah_mobil(self, mobil):
        self.daftar_mobil.append(mobil)
    
    def lihat_daftar_mobil(self):
        for mobil in self.daftar_mobil:
            print(mobil)
    
    def sewa_mobil(self, merk):
        for mobil in self.daftar_mobil:
            if mobil.merk == merk and mobil.status == "tersedia":
                mobil.status = "disewa"
                print(f"Mobil {merk} berhasil disewa.")
                return
        print(f"Mobil {merk} tidak tersedia atau sedang disewa.")
    
    def kembalikan_mobil(self, merk):
        for mobil in self.daftar_mobil:
            if mobil.merk == merk and mobil.status == "disewa":
                mobil.status = "tersedia"
                print(f"Mobil {merk} berhasil dikembalikan.")
                return
        print(f"Mobil {merk} tidak ditemukan atau sedang tersedia.")

# membuat objek RentalMobil
rental_mobil = RentalMobil()

# menambahkan mobil ke daftar
rental_mobil.tambah_mobil(Mobil("Avanza", 150000))
rental_mobil.tambah_mobil(Mobil("Xenia", 170000))
rental_mobil.tambah_mobil(Mobil("Innova", 250000))

# melihat daftar mobil yang tersedia
print("Daftar mobil yang tersedia:")
rental_mobil.lihat_daftar_mobil()

# menyewa mobil
rental_mobil.sewa_mobil("Avanza")
rental_mobil.sewa_mobil("Jazz") # mobil ini tidak tersedia

# melihat daftar mobil yang tersedia setelah ada mobil yang disewa
print("Daftar mobil yang tersedia:")
rental_mobil.lihat_daftar_mobil()

# mengembalikan mobil
rental_mobil.kembalikan_mobil("Avanza")
rental_mobil.kembalikan_mobil("Jazz") # mobil ini tidak ditemukan
