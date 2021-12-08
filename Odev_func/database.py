import sqlite3 as db

veritabani=db.connect('db202516030.db')

imlec=veritabani.cursor()


   
def TabloOlustur(TabloAdi,KolonAd,KolonAd2):
    imlec.execute(f"CREATE TABLE if not exists {TabloAdi} ({KolonAd},{KolonAd2})")
    veritabani.commit()
    print("Tablo oluşturuldu.")
    
def Degerler(TabloAdi,Isim,Soyisim):
    sorgu=f" Insert into {TabloAdi} values(?,?) "
    imlec.execute(sorgu,(Isim,Soyisim))
    veritabani.commit()

def Listele(TabloAdi):
    imlec.execute(f"select*from {TabloAdi}")
    veriler=imlec.fetchall()
    return veriler
    print("Listeleme başarılı.")
        
"""

def TabloSil(TabloAdi):
    imlec.execute(f"Drop table {TabloAdi}")
    print("Tablo Başarıyla Silindi.")
    
    """