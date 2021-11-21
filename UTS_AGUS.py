# Nama  : MUHAMMAD AGUS
# Kelas : TI20C
# Nim   : 20200040028

class laptop :
    def __init__(self,merk,harga,inc,garansi):
        self.merk = merk
        self.harga = harga
        self._inc = inc
        self.__garansi = garansi
        
    def laptop_saya(self):
        print('Saya membeli Laptop dengan merk :')
        print(f'Merk : {self.merk}')
        print(f'Harga : {self.harga}')
        print(f'Ukuran layar : {self._inc}')
        print(f'Garansi : {self.__garansi}')
        print('_______________________________________')

class on_off(laptop): 
    def __init__(self,nyalakan,matikan):
        pass
    _nyalakan = 'Dinyalakan'
    _matikan = 'Dimatikan'
        
    def nyalakan_laptop(self):
        print(f'Laptop telah {self._nyalakan}')
        print('_______________________________________')
        
    def matikan_laptop(self):
        print(f'Laptop telah {self._matikan}')
        print('_______________________________________')
        
class cek(laptop):
    def __init__(self,cek_laptop):
        pass
    __cek_laptop ='Mengecek'
        
    def cek_unit(self):
        print(f'Saya sedang {self.__cek_laptop} laptop baru saya')
        print('_______________________________________')
        
beli = laptop('Lenovo','12.000.000',14,'2 tahun')
beli.laptop_saya()

nyala = on_off('nyala',14)
nyala.nyalakan_laptop()

cekin = cek('cek')
cekin.cek_unit()

mati = on_off('mati',14)
mati.matikan_laptop()