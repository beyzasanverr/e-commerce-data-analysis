import mysql.connector
import pandas

# MySQL veritabanıma bağlanması için gerekli bilgiler ile bağlantıyı kurdum:

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommercedb",
        auth_plugin="mysql_native_password",
        port=3306,
        charset='utf8mb4'
    )

# Veritabanından gelen verileri ilerleyen aşamalarda veri ön işleme, görselleştirme gibi adımları yapabilmek için pandas kütüphanesi yardımıyla 
# tablo (DataFrame) yapısına dönüştürdüm. Bu fonkisyon anlaşılacağı üzere parametre olarak sql değişkenini alıyor. sql değişkeni ise queries.py 
# adlı dosyada değişken olarak tanımladığım hazır sql cümleleridir. Bu fonksiyon sorguları veritabanında çalıştırır. Yani özetle parametre olarak
# sql sorgusunu alıyor ve ilgili veritabanına bağlanarak sorgu sonucundan dönen verileri tablo (DataFrame) yapısında bana geri döndürüyor.

def run_query_df(sql):
    conn=connection()
    df=pandas.read_sql(sql,conn)
    conn.close()
    return df
