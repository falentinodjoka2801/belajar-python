class MakhlukHidup:
    """Class untuk semua jenis makhluk hidup, seperti manusia, hewan dan tumbuhan"""

    def makan(self):
        print('Makhluk hidup perlu makan')
    
    def bernafas(self):
        print('Mahkluk hidup perlu bernafas')

    def beradaptasi(self):
        print('Mahkluk hidup perlu beradaptasi')

class Manusia(MakhlukHidup):
    def caraMakan(self):
        print('Manusia makan dengan cara mengunyah')

_manusia    =   MakhlukHidup()
_tino   =   Manusia()
print(dir(_tino))
print(dir(_manusia))
