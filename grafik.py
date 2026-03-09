import matplotlib.pyplot 
import prepare_data
import plotly.express
import rfm_analizi
import numpy

# Bu dosyada ilgili sorgulardan dönen sonuçlara göre grafikler oluşturdum.

# Yıllara göre sipariş eğilimi:
# Bu grafik için çizgi grafiği (plot) tercih ettim çünkü zamana bağlı olarak herhangi bir değişken karşısında artışı veya azalışı en net gösteren
# grafik türü çizgi grafiğidir.
yillik_siparis=prepare_data.yillara_gore_siparis_sayisi()
matplotlib.pyplot.figure(figsize=(5,8))
matplotlib.pyplot.plot(yillik_siparis['yil'], yillik_siparis['sayi'],marker='o',color="green",linewidth=2,linestyle='-',markersize=4,markerfacecolor="black",markeredgecolor="black")
matplotlib.pyplot.title("Yıllara Göre Sipariş Eğilimi")
matplotlib.pyplot.xlabel("Yıllar")
matplotlib.pyplot.ylabel("Sipariş Sayıları")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.xticks(yillik_siparis['yil'])
matplotlib.pyplot.show()

# Aylık sipariş trendi grafiği:
# Yine bu grafik de zamana bağlı olarak sipariş sayısının artışı veya azalışı hakkında bilgi verdiğinden bu grafikte de çizgi grafiği tercih ettim.
aylik_siparis= prepare_data.ay_bazinda_siparis_sayisi()
matplotlib.pyplot.figure(figsize=(5,8))
matplotlib.pyplot.plot(aylik_siparis['ay'],aylik_siparis['sayi'], marker='o',linestyle='-',color='red',linewidth='1',markersize=3,markerfacecolor="blue",markeredgecolor="blue")
matplotlib.pyplot.title('Aylık Sipariş Trendi:', fontsize=10)
matplotlib.pyplot.xlabel('Aylar')
matplotlib.pyplot.ylabel('Sipariş Sayıları')
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()

# Şehirlere Göre Müşteri Sayısı:
# Kategorik değişkenlerde (şehirler, ürünler gibi...) sayısal sonuçları karşılaştırmak için sütun grafiği tercih edildiğinden bu grafikte sütun
# (bar) grafiğini kullandım. Burada matplotlib kütüphanesinin bar grafiğini kullandım ilk başta fakat şehir verilerim oldukça fazla olduğundan 
# grafik okunmuyordu bu sebeple daha interaktif olması için Plotly.Express kütüphanesini kullandım.
sehirlere_gore_musteri=prepare_data.sehire_gore_musteri_sayisi()
fig=plotly.express.bar(sehirlere_gore_musteri,x='city',y='musteri_sayisi',title="Şehirlere Göre Müşteri Sayısı",color="musteri_sayisi",color_continuous_scale='Viridis')
fig.update_layout(xaxis=dict(rangeslider=dict(visible=True), type='category'), xaxis_range=[0, 30])
fig.show()

# En Çok Satılan Ürünler:
# Ürünler değişkeni de kategorik bir değişken olduğundan ve ürünlerin satış adedine (sayısal bir sonuca) göre bir grafik olduğundan sütun grafiği 
# tercih ettim. Burada da ürünlerim oldukça fazla olduğu için yine matplotlib kütüphanesini kullanamadım grafik yine okunamayacak seviyede oldu
# bu sebeple yine grafik interaktif olsun diye Plotly.Express kütüphanesini kullandım. Bunun dışında bazı ürün isimleri uzun olduğundan ürün
# isimlerinin rahat okunabilmesi için x ve y eksenlerini yer değiştirerek grafiği yatay sütun grafiği olarak kullandım.
en_cok_satilan_urunler=prepare_data.urun_satis_yuzde_payi()
fig=plotly.express.bar(en_cok_satilan_urunler,x='yuzde',y='product_name',title="En Çok Satılan Ürünler",color="yuzde",color_continuous_scale='Viridis')
fig.update_layout(xaxis=dict(rangeslider=dict(visible=True), type='category'), yaxis_range=[0, 30])
fig.show()

# Kategori Bazlı Ortalama Gelir:
# Yine kategorik değişkende ortalama gelir gibi sayısal sonucun miktarsal farkları karşılaştırmak istediğimden bu grafikte de sütun grafiği tercih
# ettim. Burada yatay sütun grafiği (barh) tercih ettim çünkü kategorilerin isimleri uzundu ve dikey sütun grafiğinde kategori isimleri okunmuyordu.
kategori_gelir=prepare_data.kategori_ortalama_fiyat()
matplotlib.pyplot.figure(figsize=(5,8))
matplotlib.pyplot.barh(kategori_gelir['category'],kategori_gelir['avg_unitprice'],color="blue",linewidth=3)
matplotlib.pyplot.title("Kategori Bazlı Ortalama Gelir")
matplotlib.pyplot.xlabel("Ortalama Gelirler")
matplotlib.pyplot.ylabel("Kategoriler")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()

# Müşteri Harcama Dağılımı:
# Burada da verilerin dağılım sıklığını ve hangi harcama aralıklarında yoğunlaştığını tespit edip göstermek için histogram grafiği tercih ettim.
musteri_harcama=prepare_data.musteri_toplam_harcamasi()
matplotlib.pyplot.figure(figsize=(5,8))
matplotlib.pyplot.hist(musteri_harcama['total_price'],bins=40,color="green",edgecolor="black")
matplotlib.pyplot.title("Müşteri Harcama Dağılımı")
matplotlib.pyplot.xlabel("Harcama Tutarları")
matplotlib.pyplot.ylabel("Müşteri Sayısı")
matplotlib.pyplot.show()

# Yaş Dağılımı:
# Burada her bir yaş segmentinin işletmeye kattığı toplam gelir değerini göstermek istediğim için sütun grafiği tercih ettim.
# Not: Y eksenindeki rakamlar bilimsel gösterimdedir (1e7 = 10 Milyon).
yas_dagilim=prepare_data.yas_araliklarina_gore_gelir()
gelir_analizi = yas_dagilim.groupby('yas_segmenti')['toplam_gelir'].sum().reset_index()
matplotlib.pyplot.figure(figsize=(5,8))
matplotlib.pyplot.bar(gelir_analizi['yas_segmenti'], gelir_analizi['toplam_gelir'], color="blue", edgecolor="black")
matplotlib.pyplot.title("Yaş Dağılımına Göre Gelir")
matplotlib.pyplot.xlabel("Yaş Dağılımları")
matplotlib.pyplot.ylabel("Gelir")
matplotlib.pyplot.show()

# RFM Segment Dağılımı:
# Yine burada da rfm_segmentine göre (kategorik) kişi sayısının (sayısal sonucun) miktarsal farkları karşılaştırmalı olarak göstermeyi 
# hedeflendiğimden sütun grafiğini tercih ettim.
rfm_segment=rfm_analizi.rfm()
rfm_analiz=rfm_analizi.analiz
matplotlib.pyplot.figure(figsize=(5,8))
matplotlib.pyplot.bar(rfm_analiz.index,rfm_analiz['kisi_sayisi'],color="red")
matplotlib.pyplot.title("RFM Segment Dağılımı")
matplotlib.pyplot.xlabel("Segmentler")
matplotlib.pyplot.ylabel("Kişi Sayısı")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()

# Ödeme Yöntemine Göre Sipariş Sayısı:
# Burada hangi ödeme yönteminin genel orandan (sipariş sayısı) ne kadar pay aldığını göstermeyi hedeflediğimden pasta grafiği tercih ettim.
odeme_siparis=prepare_data.odeme_yontemine_gore_siparis_sayisi()
matplotlib.pyplot.figure(figsize=(15,15))
renk_paleti = matplotlib.pyplot.get_cmap('tab20b')(numpy.linspace(0, 1, len(odeme_siparis)))
matplotlib.pyplot.pie(odeme_siparis['siparis_sayisi'],labels=odeme_siparis["payment_method"],autopct='%1.1f%%',colors=renk_paleti)
matplotlib.pyplot.title("Ödeme Yöntemine Göre Sipariş Sayısı")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()