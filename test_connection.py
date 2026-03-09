import queries
from connection import run_query_df

# Bu dosyada connection dosyasında tanımlanan bağlantı gerçekten doğru bir şekilde çalışıyor mu onu her sorgu için test ettim. Amaç yani tamamen 
# SQL bağlantısının doğru bir şekilde çalışıp çalışılmadığını görmek.

df=run_query_df(queries.en_cok_siparis_veren_musteri)
print(df)

df=run_query_df(queries.en_cok_odeme_yapan_musteri)
print(df)

df=run_query_df(queries.en_cok_satilan_urun)
print(df)

df=run_query_df(queries.en_cok_gelir_getiren_kategori)
print(df)

df=run_query_df(queries.ay_bazinda_siparis_sayisi)
print(df)

df=run_query_df(queries.sehire_gore_musteri_sayisi)
print(df)

df=run_query_df(queries.odeme_yontemine_gore_siparis_sayisi)
print(df)

df=run_query_df(queries.en_pahali_urunler)
print(df)

df=run_query_df(queries.en_fazla_siparis_olan_sehirler)
print(df)

df=run_query_df(queries.en_eski_uyelik_musterisi)
print(df)

df=run_query_df(queries.musteri_toplam_siparis_sayisi)
print(df)

df=run_query_df(queries.musteri_toplam_harcamasi)
print(df)

df=run_query_df(queries.kategori_toplam_geliri)
print(df)

df=run_query_df(queries.urun_toplam_satis_adedi)
print(df)

df=run_query_df(queries.musteri_ilk_siparis_tarihi)
print(df)

df=run_query_df(queries.musteri_son_siparis_tarihi)
print(df)

df=run_query_df(queries.musteri_urun_cesidi_sayisi)
print(df)

df=run_query_df(queries.sehire_gore_ortalama_siparis_tutari)
print(df)

df=run_query_df(queries.yillara_gore_siparis_sayisi)
print(df)

df=run_query_df(queries.kategori_ortalama_fiyat)
print(df)

df=run_query_df(queries.en_yuksek_ltv_musteri)
print(df)

df=run_query_df(queries.yillara_gore_gelir_buyume_orani)
print(df)

df=run_query_df(queries.musteri_ortalama_sepet_degeri)
print(df)

df=run_query_df(queries.musteri_siparis_frekansi)
print(df)

df=run_query_df(queries.urun_karlilik_orani)
print(df)

df=run_query_df(queries.musteri_ilk_son_siparis_suresi)
print(df)

df=run_query_df(queries.tek_seferlik_musteriler)
print(df)

df=run_query_df(queries.tekrar_siparis_veren_musteriler)
print(df)

df=run_query_df(queries.en_hizli_buyuyen_kategori)
print(df)

df=run_query_df(queries.aylik_ortalama_siparis_tutari)
print(df)

df=run_query_df(queries.en_cok_farkli_urun_alan_musteriler)
print(df)

df=run_query_df(queries.elli_yas_ustu_harcama)
print(df)

df=run_query_df(queries.yas_araliklarina_gore_gelir)
print(df)

df=run_query_df(queries.sehire_gore_yillik_siparis_egilimi)
print(df)

df=run_query_df(queries.musteri_siparis_sirasi_rownum)
print(df)

df=run_query_df(queries.musteri_siparis_tutar_rank)
print(df)

df=run_query_df(queries.aylik_satis_lag_farki)
print(df)

df=run_query_df(queries.aylik_satis_yuzdelik_degisim)
print(df)

df=run_query_df(queries.kategori_yillik_gelir_dense_rank)
print(df)

df=run_query_df(queries.urun_satis_yuzde_payi)
print(df)

df=run_query_df(queries.musteri_yillik_harcama_ortalamasi)
print(df)

df=run_query_df(queries.aylik_gelir_kumulatif_toplam)
print(df)

df=run_query_df(queries.kategori_bazli_en_pahali_10_siparis)
print(df)

df=run_query_df(queries.siparis_adedi_genel_ort_farki)
print(df)

df=run_query_df(queries.rfm)
print(df)