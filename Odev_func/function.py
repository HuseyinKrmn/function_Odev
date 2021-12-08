import database
import sqlite3 as db


sql=database.veritabani
cursor=database.imlec

database.TabloOlustur('Kisiler', 'Ad', 'Soyad')
database.Degerler('Kisiler', 'Hüseyin', 'Karaman')
database.Listele('Kisiler')


database.Degerler('Kisiler', 'Murat', 'Şahin')