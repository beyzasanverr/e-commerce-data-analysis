import pandas as pd 
from prepare_data import rfm

# Bu dosyada RFM (Recency, Frequency, Monetary) analizi yapmak için gerekli adımları tamamladım. RFM Analizi ile müşterileri satın alma
# alışkanlıklarına göre gruplara/segmentlere ayırdım. Böylece hangi müşterinin sadık, hangi müşterinin çoktan o işletmeyi unuttuğunu, hangi
# müşterilerin riskli (müşteriyi kaybetme riski) olduğunu skorlarla göstermek istedim.

df=rfm()
print(df)
df['yenilik_skor']=pd.qcut(df['yeni_musteriler'],5,labels=[5,4,3,2,1])
print(df['yenilik_skor'].value_counts().sort_index()) # value_counts adı üstünde sütundaki (yenilik_skor) o valuedan kaç tane (count) var onu 
# söyler örneğin 1 puan alan kişilerin sayısı 200 2 puan alan kişilerin sayısı 400-> yani tüm sütuna bakar ve 1 puan alan kişi sayısı: ...
#  2 puan alan kişi sayısı: ... 3 puan alan kişi sayısı: ... 4 puan alan kişi sayısı: ... 5 puan alan kişi sayısı: ... şeklinde bir frekans tablosu
#  gibi bir şey çıkarır. sort_index()-> index'e göre yani bizim label olarak belirlediğimize göre (1,2,3,4,5) sort eder yani sıralar. varsayılan 
# olarak küçükten büyüğe sıralar eğer büyükten küçüğe sıralasın istiyorsan sort_index(ascending=False) diyebilirsin.
print(df.groupby('yenilik_skor')['yeni_musteriler'].agg(['min', 'max'])) # burada groupby('yenilik_skor') SQLde bildiğimiz groupby ile aynı-> 
# yenilik_skor alanını 5 parçaya bölmüştük bu 5 parçayı kendi içinde gruplar (1 puan alanlar, 2 puan alanlar, 3 puan alanlar...) 
# ['yeni_musteriler'].agg(['min', 'max'])-> ifadesi de şunu yapar-> agg(aggregate function) min, max -> min ve max değer bul-> hangi alanın 
# min ve max değerini bulıyım?-> yeni_musteriler alanının. yani yeni_musteriler alanında min ve max değerleri bulunur. 
# groupby('yenilik_skor') kısmı ile de gruplamıştık yani her bir puan grubundan min ve max değerlerini bulup yazar.
# örneğin şöyle bir çıktı geldi-> 
# yenilik_skor: 5  | min: 19 | max: 1875
# Tercümesi: "5 puan verdiğim grupta (en iyiler), mağazaya en son 19 gün önce uğrayan biri var. Bu grubun en eskisi ise 1875 gün önce uğramış.
# Yani 19 ile 1875 gün arasındaki herkes benim için 5 puanlık taze müşteridir."

df['frekans']=pd.qcut(df['musteri_sayisi'].rank(method='first'),5,labels=[1,2,3,4,5])
print(df['frekans'].value_counts().sort_index())
print(df.groupby('frekans')['musteri_sayisi'].agg(['min','max']))

df['money']=pd.qcut(df['toplam_tutar'],5,[1,2,3,4,5])
print(df['money'].value_counts().sort_index())
print(df.groupby('money')['toplam_tutar'].agg(['min','max']))

df['rfm_skoru']=df['yenilik_skor'].astype(str) + df['frekans'].astype(str)
print(df[["yenilik_skor", "frekans", "rfm_skoru"]].head(10))

rfm_map = { # burada ilk parantez yenilik_skor değerini, ikinci parantez frekans değerini gösteriyor. 
r'[1-2][1-2]': 'hibernating', # ilk sayı (ilk parantez->yenilik_skor) 1 veya 2 rakamlarından oluşuyorsa ve ikinci sayı (ikinci parantez-> frekans)
# 1 veya 2 sayılarından oluşuyorsa. Yani kısaca yenilik skoru 1 veya 2 yani düşük-> eski müşteri ve frekans skoru 1 veya 2 yani düşük-> sık 
# ziyaret etmiyor-> yani ham eski müşteri olup hem sık ziyaret etmeyenler-> hibernating (uyuyan/ kış uykusuna yatan... aktif müşteri değil...) 
# bu mantıkla diğerleri anlaşılabilir...
r'[1-2][3-4]': 'at_Risk', 
r'[1-2]5': 'cant_loose',
r'3[1-2]': 'about_to_sleep',
r'33': 'need_attention',
r'[3-4][4-5]': 'loyal_customers',
r'41': 'promising',
r'51': 'new_customers',
r'[4-5][2-3]': 'potential_loyalists',
r'5[4-5]': 'champions'
}

df['rfm_segmenti']=df['rfm_skoru'].replace(rfm_map,regex=True)
print(df[['rfm_skoru', 'rfm_segmenti']].head(10))

analiz=df.groupby('rfm_segmenti').agg({'rfm_skoru':'count', 'yeni_musteriler':'mean', 'musteri_sayisi':'mean','toplam_tutar':'mean'})
analiz.columns=["kisi_sayisi","ort_yeni_musteri_sayisi","ort_musteri_sayisi","ort_kazanc"]
print(analiz.sort_values(by='kisi_sayisi'))