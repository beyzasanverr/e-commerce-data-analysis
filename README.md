# 🛒 E-Ticaret Veri Analizi Projesi

### 📝 Proje Hakkında
Bu projede Python’ın **Faker** kütüphanesi ile rastgele gerçek veriler oluşturup bu verileri **MySQL** kullanarak bir veritabanına kaydettim. Gerekli gördüğüm ve ileri SQL sorgularını da barındıran sorguları `queries.py` adlı dosyada yazıp bu sorguların sonuçlarını yine Python’ın **Matplotlib**, **Plotly.Express** gibi görselleştirme kütüphanelerini kullanarak görselleştirdim. 

Bu projede amacım bir e-ticaret sisteminin veri akışını sıfırdan kurgulayıp sadece hazır verilerle çalışmak değil, verinin üretiminden raporlanmasına kadar olan tüm süreci bizzat yönetmeyi öğrenmekti. Projenin tüm teknik detayları ve mantığı, kod dosyaları içerisindeki yorum satırlarında açıklanmıştır.

---

### ⚙️ Proje İş Akışı

* **Veri Üretimi:** `faker_veriler.py` adlı dosya ile Python programlama dilinin Faker kütüphanesi ile gerçeğe yakın veriler oluşturulması.
* **Veritabanı ve Yönetimi:** Faker kütüphanesi ile oluşturulan veriler MySQL veritabanına aktarılması ve `connection.py` dosyası ile bağlantının güvenle sağlanması.
* **Sorgulama:** `queries.py` dosyası ile ileri SQL sorguları (CTE, Window Functions, RFM Analizi, JOIN vb.) kullanarak verinin işlenmesi.
* **Veri Hazırlama:** `prepare_data.py` dosyası ile veri ön işleme adımları/veri temizleme, veri tipi dönüşümleri gibi işlemler ile veriler grafik üretimine uygun hale getirilmesi.
* **Analiz ve Görselleştirme:** `rfm_analizi.py` dosyası ile müşteriler hakkında gerekli analizlerin yapılması ve `grafik.py` dosyası ile sonuçların görsel olarak desteklenmesi.
