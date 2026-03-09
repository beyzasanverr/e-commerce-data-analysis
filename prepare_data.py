import pandas as pd
from connection import run_query_df
import queries

# Bu dosyada merkezi bir veri temizleme/ön işleme işlemlerini yapan bir clean_data fonksiyonu tanımladım ve her sorgu için oluşturulan fonksiyonlarda
# bu veri temizleme fonksiyonunu kullandım. Burada sadece grafiğini çizme ihtimalim olan sorguları fonksiyon olarak tanımladım. Bu fonksiyonlar 
# SQL'den gelen veriler string veri tipinde olacağından bu fonksiyonlarda veri tiplerini olması gerektiği şekilde düzenledim. 

def clean_data(df):
    df=df.dropna(how='all')
    df=df.drop_duplicates()
    if 'total_amount' in df.columns:
        df= df[df['total_amount'] > 0]
    if 'price' in df.columns:
        df = df[df['price'] > 0]
    return df

def ay_bazinda_siparis_sayisi():
    df=run_query_df(queries.ay_bazinda_siparis_sayisi)
    df=clean_data(df)
    df['sayi']=df['sayi'].astype(int)
    df['ay'] = df['ay'].astype(str).str.strip()
    aylar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df['ay'] = pd.Categorical(df['ay'], categories=aylar, ordered=True)
    df.sort_values('ay',inplace=True)
    return df
    
def sehire_gore_musteri_sayisi():
    df1=run_query_df(queries.sehire_gore_musteri_sayisi)
    df1=clean_data(df1)
    df1['musteri_sayisi']=df1['musteri_sayisi'].astype(int)
    return df1

def odeme_yontemine_gore_siparis_sayisi():
    df2=run_query_df(queries.odeme_yontemine_gore_siparis_sayisi)
    df2=clean_data(df2)
    df2['siparis_sayisi']=df2['siparis_sayisi'].astype(int)
    return df2

def en_fazla_siparis_olan_sehirler():
    df3=run_query_df(queries.en_fazla_siparis_olan_sehirler)
    df3=clean_data(df3)
    df3['total_count']=df3['total_count'].astype(int)
    return df3

def musteri_toplam_siparis_sayisi():
    df4=run_query_df(queries.musteri_toplam_siparis_sayisi)
    df4=clean_data(df4)
    df4['customerid']=df4['customerid'].astype(int)
    df4['siparis_sayisi']=df4['siparis_sayisi'].astype(int)
    return df4

def musteri_toplam_harcamasi():
    df5=run_query_df(queries.musteri_toplam_harcamasi)
    df5=clean_data(df5)
    df5['customerid']=df5['customerid'].astype(int)
    df5['total_price']=df5['total_price'].astype(int)
    return df5

def kategori_toplam_geliri():
    df6=run_query_df(queries.kategori_toplam_geliri)
    df6=clean_data(df6)
    df6['total_price']=df6['total_price'].astype(float)
    return df6

def urun_toplam_satis_adedi():
    df7=run_query_df(queries.urun_toplam_satis_adedi)
    df7=clean_data(df7)
    df7['productid']=df7['productid'].astype(int)
    df7['total_quantity']=df7['total_quantity'].astype(int)
    return df7

def sehire_gore_ortalama_siparis_tutari():
    df8=run_query_df(queries.sehire_gore_ortalama_siparis_tutari)
    df8=clean_data(df8)
    df8['avg_price']=df8['avg_price'].astype(float)
    return df8

def yillara_gore_siparis_sayisi():
    df9=run_query_df(queries.yillara_gore_siparis_sayisi)
    df9=clean_data(df9)
    df9['yil']=df9['yil'].astype(int)
    df9['sayi']=df9['sayi'].astype(int)
    return df9

def kategori_ortalama_fiyat():
    df10=run_query_df(queries.kategori_ortalama_fiyat)
    df10=clean_data(df10)
    df10['avg_unitprice']=df10['avg_unitprice'].astype(float)
    return df10

def yillara_gore_gelir_buyume_orani():
    df11=run_query_df(queries.yillara_gore_gelir_buyume_orani)
    df11=clean_data(df11)
    df11['year']=df11['year'].astype(int)
    df11['bu_yil_geliri']=df11['bu_yil_geliri'].astype(float)
    df11['gecen_yil_gelir']=df11['gecen_yil_gelir'].astype(float)
    df11['buyume_orani_yuzde']=df11['buyume_orani_yuzde'].astype(float)
    return df11

def musteri_ortalama_sepet_degeri():
    df12=run_query_df(queries.musteri_ortalama_sepet_degeri)
    df12=clean_data(df12)
    df12['toplam_harcama']=df12['toplam_harcama'].astype(float)
    df12['toplam_siparis_sayisi']=df12['toplam_siparis_sayisi'].astype(int)
    df12['ort_sepet_degeri']=df12['ort_sepet_degeri'].astype(float)
    return df12

def musteri_siparis_frekansi():
    df13=run_query_df(queries.musteri_siparis_frekansi)
    df13=clean_data(df13)
    df13['customerid']=df13['customerid'].astype(int)
    df13['siparis_sayisi']=df13['siparis_sayisi'].astype(int)
    return df13

def en_hizli_buyuyen_kategori():
    df14=run_query_df(queries.en_hizli_buyuyen_kategori)
    df14=clean_data(df14)
    df14['bu_yil']=df14['bu_yil'].astype(int)
    df14['bu_yil_geliri']=df14['bu_yil_geliri'].astype(float)
    df14['gecen_yil_gelir']=df14['gecen_yil_gelir'].astype(float)
    df14['buyume_oranı_yuzde']=df14['buyume_oranı_yuzde'].astype(float)
    return df14

def aylik_ortalama_siparis_tutari():
    df15=run_query_df(queries.aylik_ortalama_siparis_tutari)
    df15=clean_data(df15)
    aylar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df15['ay'] = pd.Categorical(df15['ay'], categories=aylar, ordered=True)
    df15.sort_values('ay',inplace=True)
    df15['aylik_ort']=df15['aylik_ort'].astype(float)
    return df15

def yas_araliklarina_gore_gelir():
    df16=run_query_df(queries.yas_araliklarina_gore_gelir)
    df16=clean_data(df16)
    yas_sirasi=['0-18: Adolescent', '18-65: Adult', '65-74: Young Old', '74-84: Elderly','85+: Very Old']
    df16['yas_segmenti'] = pd.Categorical(df16['yas_segmenti'], categories=yas_sirasi, ordered=True)
    df16=df16.sort_values('yas_segmenti')
    df16['customerid']=df16['customerid'].astype(int)
    df16['toplam_gelir']=df16['toplam_gelir'].astype(float)
    return df16

def sehire_gore_yillik_siparis_egilimi():
    df17=run_query_df(queries.sehire_gore_yillik_siparis_egilimi)
    df17=clean_data(df17)
    df17['yil']=df17['yil'].astype(int)
    df17['yillik_gelir']=df17['yillik_gelir'].astype(float)
    df17['onceki_yil_gelir']=df17['onceki_yil_gelir'].astype(float)
    df17['artis_orani']=df17['artis_orani'].astype(float)
    return df17

def aylik_satis_lag_farki():
    df18=run_query_df(queries.aylik_satis_lag_farki)
    df18=clean_data(df18)
    aylar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df18['ay'] = pd.Categorical(df18['ay'], categories=aylar, ordered=True)
    df18.sort_values('ay',inplace=True)
    df18['bu_ayki_toplam']=df18['bu_ayki_toplam'].astype(float)
    df18['onceki_ay_toplam']=df18['onceki_ay_toplam'].astype(float)
    df18['fark']=df18['fark'].astype(float)
    return df18

def aylik_satis_yuzdelik_degisim():
    df19=run_query_df(queries.aylik_satis_yuzdelik_degisim)
    df19=clean_data(df19)
    aylar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df19['ay_ismi'] = pd.Categorical(df19['ay_ismi'], categories=aylar, ordered=True)
    df19.sort_values('ay_ismi',inplace=True)
    df19['bu_ay_satis']=df19['bu_ay_satis'].astype(float)
    df19['gecen_ay_satis']=df19['gecen_ay_satis'].astype(float)
    df19['fark_yuzde']=df19['fark_yuzde'].astype(float)
    return df19

def kategori_yillik_gelir_dense_rank():
    df20=run_query_df(queries.kategori_yillik_gelir_dense_rank)
    df20=clean_data(df20)
    df20['gelir']=df20['gelir'].astype(float)
    df20['yil']=df20['yil'].astype(int)
    df20['siralanmis']=df20['siralanmis'].astype(int)
    return df20

def urun_satis_yuzde_payi():
    df21=run_query_df(queries.urun_satis_yuzde_payi)
    df21=clean_data(df21)
    df21['productid']=df21['productid'].astype(int)
    df21['urunun_top_satis']=df21['urunun_top_satis'].astype(float)
    df21['tum_urun_genel_top']=df21['tum_urun_genel_top'].astype(float)
    df21['yuzde']=df21['yuzde'].astype(float)
    return df21

def musteri_yillik_harcama_ortalamasi():
    df22=run_query_df(queries.musteri_yillik_harcama_ortalamasi)
    df22=clean_data(df22)
    df22['customerid']=df22['customerid'].astype(int)
    df22['yil']=df22['yil'].astype(int)
    df22['yillik_harcama']=df22['yillik_harcama'].astype(float)
    return df22

def aylik_gelir_kumulatif_toplam():
    df23=run_query_df(queries.aylik_gelir_kumulatif_toplam)
    df23=clean_data(df23)
    df23['ay']=df23['ay'].astype(int)
    df23['total']=df23['total'].astype(float)
    df23['kumulatif']=df23['kumulatif'].astype(float)
    return df23

def rfm():
    df24=run_query_df(queries.rfm)
    df24=clean_data(df24)
    df24['customerid']=df24['customerid'].astype(int)
    df24['yeni_musteriler']=df24['yeni_musteriler'].astype(int)
    df24['musteri_sayisi']=df24['musteri_sayisi'].astype(int)
    df24['toplam_tutar']=df24['toplam_tutar'].astype(float)
    return df24
