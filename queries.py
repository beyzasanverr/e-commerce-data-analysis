# Bu dosyada gerekli gördüğüm SQL sorgularını değişken tanımlayarak tanımladım. Değişken olarak tutmamın sebebi aynı sorguyu birden fazla
# yerde kullanmam gerektiğinde değişken ismiyle pratik olarak çağırarak kullanmak için. Yine aynı şekilde sorguda değişiklik yapmam gerektiği
# durumlarda her yerde tek tek değiştirmektense tek merkezi bir yerde değişiklik yapmak için.

en_cok_siparis_veren_musteri= """select c.customerid,c.first_name,c.last_name,count(o.orderid) as musteri_sayisi
from orders as o
join customers as c on c.customerid=o.customerid
GROUP BY c.customerid,c.first_name,c.last_name
ORDER BY musteri_sayisi DESC LIMIT 1 """

en_cok_odeme_yapan_musteri=""" SELECT c.customerid,c.first_name,c.last_name,sum(oi.price) as total_price
from order_items as oi 
join orders as o on oi.orderid=o.orderid
join customers as c on c.customerid=o.customerid
GROUP BY c.customerid,c.first_name,c.last_name
ORDER BY total_price DESC LIMIT 1 """

en_cok_satilan_urun= """ SELECT p.productid,p.product_name, sum(oi.quantity) as total_quantity
from products as p 
join order_items as oi on oi.productid=p.productid
GROUP BY  p.productid,p.product_name
ORDER BY total_quantity DESC LIMIT 1 """

en_cok_gelir_getiren_kategori= """ SELECT p.category,sum(oi.price) as total_price
from order_items as oi 
join products as p on oi.productid=p.productid
GROUP BY  p.category
ORDER BY total_price DESC LIMIT 1 """

ay_bazinda_siparis_sayisi=""" SELECT DATE_FORMAT(order_date,'%M') as ay, count(*) as sayi
from orders 
GROUP BY DATE_FORMAT(order_date,'%M')
ORDER BY MONTH(order_date) """

sehire_gore_musteri_sayisi= """ SELECT city, count(*) as musteri_sayisi FROM customers GROUP BY city order by city ASC; """

odeme_yontemine_gore_siparis_sayisi= """ SELECT payment_method, count(*) as siparis_sayisi FROM orders 
GROUP BY payment_method ORDER BY siparis_sayisi """

en_pahali_urunler= """ SELECT product_name,category,unitprice FROM products GROUP BY product_name,category ORDER BY unitprice DESC """

en_fazla_siparis_olan_sehirler=""" SELECT c.city, count(o.orderid) as total_count 
from customers as c
JOIN orders as o on o.customerid=c.customerid
GROUP BY c.city
ORDER BY total_count DESC  """

en_eski_uyelik_musterisi= """ SELECT * from customers ORDER BY signup_date ASC LIMIT 1 """

musteri_toplam_siparis_sayisi= """ SELECT c.customerid, c.first_name, c.last_name, count(o.order_date) as siparis_sayisi 
from orders as o 
JOIN customers as c on o.customerid=c.customerid
GROUP BY c.customerid,c.first_name,c.last_name
ORDER BY siparis_sayisi DESC """

musteri_toplam_harcamasi= """ SELECT c.customerid,c.first_name,c.last_name,sum(oi.price) as total_price 
from order_items as oi
JOIN orders as o on o.orderid=oi.orderid
JOIN customers as c on c.customerid=o.customerid
GROUP BY c.customerid,c.first_name,c.last_name
ORDER BY total_price DESC """

kategori_toplam_geliri= """ SELECT p.category, sum(oi.price) as total_price
from products as p
JOIN order_items as oi on oi.productid=p.productid
GROUP BY p.category
ORDER BY total_price DESC """

urun_toplam_satis_adedi=""" SELECT p.productid, p.product_name, sum(oi.quantity) as total_quantity
from products as p 
JOIN order_items as oi on oi.productid=p.productid
GROUP BY p.productid,p.product_name
ORDER BY total_quantity DESC """

musteri_ilk_siparis_tarihi=""" SELECT c.customerid, c.first_name, MIN(o.order_date) as first_order_date
from customers as c
JOIN orders as o on o.customerid=c.customerid
GROUP BY c.customerid, c.first_name
ORDER BY first_order_date  """

musteri_son_siparis_tarihi=""" SELECT c.customerid, c.first_name, MAX(o.order_date) as last_order_date
from customers as c
JOIN orders as o on o.customerid=c.customerid
GROUP BY c.customerid, c.first_name
ORDER BY last_order_date DESC """

musteri_urun_cesidi_sayisi=""" SELECT c.customerid, c.first_name,c.last_name, COUNT(DISTINCT oi.productid) as urun_cesiti
from order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
JOIN customers as c on c.customerid=o.customerid
GROUP BY c.customerid, c.first_name,c.last_name
ORDER BY urun_cesiti DESC """

sehire_gore_ortalama_siparis_tutari=""" SELECT c.city, AVG(oi.price) as avg_price
from order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
JOIN customers as c on c.customerid=o.customerid
GROUP BY c.city
ORDER BY avg_price DESC """

yillara_gore_siparis_sayisi=""" SELECT DATE_FORMAT(order_date,'%Y') as yil, COUNT(*) as sayi from orders GROUP BY yil ORDER BY yil DESC """

kategori_ortalama_fiyat=""" SELECT category, avg(unitprice) as avg_unitprice FROM products GROUP BY category ORDER BY avg_unitprice DESC """

en_yuksek_ltv_musteri=""" WITH ltv as(
	SELECT c.first_name, c.last_name, o.customerid,sum(oi.price) as total_price 
    from order_items as oi
    JOIN orders as o on oi.orderid=o.orderid
    JOIN customers as c on c.customerid=o.customerid
    GROUP BY c.first_name,c.last_name,o.customerid)
SELECT customerid,first_name,last_name FROM ltv ORDER BY total_price DESC LIMIT 1 """

yillara_gore_gelir_buyume_orani=""" WITH yil as(
	SELECT DATE_FORMAT(o.order_date,'%Y') as year, SUM(oi.price) as total_price
	FROM order_items as oi
    JOIN orders as o on oi.orderid=o.orderid
    GROUP BY year
),
hesap_tablosu as(	
	SELECT year, total_price as bu_yil_geliri,
    LAG(total_price) over (ORDER BY year) as gecen_yil_gelir
    FROM yil
)
SELECT year, bu_yil_geliri, gecen_yil_gelir,
ROUND(((bu_yil_geliri-gecen_yil_gelir)/gecen_yil_gelir)*100,2) as buyume_orani_yuzde 
from hesap_tablosu """

musteri_ortalama_sepet_degeri=""" WITH toplam as(
	SELECT c.first_name, c.last_name, SUM(oi.price) as toplam_harcama, COUNT(DISTINCT oi.orderid) as toplam_siparis_sayisi
    FROM order_items as oi 
    JOIN orders as o on oi.orderid=o.orderid
    JOIN customers as c on o.customerid=c.customerid
    GROUP BY c.first_name, c.last_name
)

SELECT first_name,last_name,toplam_harcama,toplam_siparis_sayisi,
ROUND((toplam_harcama/toplam_siparis_sayisi),2) as ort_sepet_degeri
FROM toplam
ORDER BY ort_sepet_degeri DESC """

musteri_siparis_frekansi=""" SELECT o.customerid, c.first_name,c.last_name, COUNT(o.orderid) as siparis_sayisi
from customers as c 
JOIN orders as o on o.customerid=c.customerid
GROUP BY c.customerid, c.first_name,c.last_name
ORDER BY siparis_sayisi DESC """

urun_karlilik_orani=""" SELECT product_name, SUM(cost) as maliyet, SUM(unitprice) as satis_fiyati,
CASE
	WHEN SUM(unitprice)=0 THEN '0%'
    ELSE CONCAT(ROUND(((SUM(unitprice) - SUM(cost)) / NULLIF(SUM(unitprice), 0)) * 100,2),'%') 
END AS kar_orani
FROM products 
GROUP BY product_name
ORDER BY (SUM(unitprice) - SUM(cost)) / NULLIF(SUM(unitprice), 0) DESC """

musteri_ilk_son_siparis_suresi= """ SELECT c.first_name, c.last_name, DATEDIFF(MAX(o.order_date),MIN(o.order_date)) as gun_farki
FROM customers as c
JOIN orders as o on o.customerid=c.customerid
GROUP BY c.first_name,c.last_name
ORDER BY gun_farki DESC """

tek_seferlik_musteriler=""" WITH tek_seferlik as(
	SELECT c.first_name,c.last_name,COUNT(DISTINCT o.orderid) as sayi
    FROM orders as o 
    JOIN customers as c on c.customerid=o.customerid
    GROUP BY c.first_name,c.last_name
)
SELECT first_name,last_name from tek_seferlik WHERE sayi=1 """

tekrar_siparis_veren_musteriler=""" WITH tekrar_siparis as(
	SELECT c.customerid,c.first_name,c.last_name,COUNT(DISTINCT o.orderid) as tekrar
    FROM orders as o 
    JOIN customers as c on c.customerid=o.customerid
    GROUP BY c.customerid,c.first_name,c.last_name
)
SELECT customerid,first_name,last_name from tekrar_siparis WHERE tekrar>1 """

en_hizli_buyuyen_kategori=""" WITH buyuyen_kategori as(
	SELECT DATE_FORMAT(o.order_date,'%Y') as bu_yil, SUM(oi.price) as total_price, p.category
    FROM orders as o 
    JOIN order_items as oi on o.orderid=oi.orderid
    JOIN products as p on oi.productid=p.productid
    GROUP BY bu_yil,p.category
),

tablo_gecmis as (
	SELECT bu_yil, total_price as bu_yil_geliri,category,
    LAG(total_price) over (PARTITION BY category ORDER BY bu_yil) as gecen_yil_gelir
    FROM buyuyen_kategori
)
SELECT bu_yil,category,bu_yil_geliri,gecen_yil_gelir,
ROUND(((bu_yil_geliri-gecen_yil_gelir)/gecen_yil_gelir)*100,2) as buyume_oranı_yuzde
FROM tablo_gecmis
ORDER BY buyume_oranı_yuzde DESC """

aylik_ortalama_siparis_tutari= """ WITH siparis_listesi as(
	SELECT o.orderid, DATE_FORMAT(o.order_date,'%M') as ay,
    SUM(oi.price) as total_price
    FROM orders as o
    JOIN order_items as oi on oi.orderid=o.orderid
    GROUP BY o.orderid, ay
)

SELECT ay, AVG(total_price) as aylik_ort
FROM siparis_listesi 
GROUP BY ay
ORDER BY aylik_ort DESC """

en_cok_farkli_urun_alan_musteriler= """ SELECT c.customerid, c.first_name, c.last_name, COUNT(DISTINCT p.productid) as farkli_urun
FROM customers as c 
JOIN orders as o on c.customerid=o.customerid
JOIN order_items as oi on oi.orderid=o.orderid
JOIN products as p on p.productid=oi.productid
GROUP BY c.customerid,c.first_name,c.last_name
ORDER BY farkli_urun DESC """

elli_yas_ustu_harcama=""" WITH yas as(
	SELECT customerid,first_name,last_name, (YEAR(NOW())-birth_year) as guncel_yas
    FROM customers where (YEAR(NOW())-birth_year)>50
)
SELECT y.customerid, y.first_name, y.last_name, y.guncel_yas, sum(oi.price) as total_tutar
FROM yas as y
JOIN orders as o on y.customerid=o.customerid
JOIN order_items as oi on oi.orderid=o.orderid
GROUP BY y.customerid, y.first_name, y.last_name, y.guncel_yas
ORDER BY total_tutar DESC  """

yas_araliklarina_gore_gelir=""" WITH yas_aralik as(
	SELECT customerid, first_name, last_name, (YEAR(NOW())-birth_year) as guncel_yas,
    CASE
    	WHEN (YEAR(NOW())-birth_year)<18 THEN '0-18: Adolescent'
    	WHEN (YEAR(NOW())-birth_year) BETWEEN 18 AND 65 THEN '18-65: Adult'
    	WHEN (YEAR(NOW())-birth_year) BETWEEN 65 AND 74 THEN '65-74: Young Old'
    	WHEN (YEAR(NOW())-birth_year) BETWEEN 74 AND 84 THEN '74-84: Elderly'
    	ELSE '85+: Very Old'
    END AS yas_segmenti
    FROM customers
)
SELECT y.customerid, y.first_name, y.last_name, y.yas_segmenti, SUM(price) as toplam_gelir
FROM yas_aralik as y 
JOIN orders as o on y.customerid=o.customerid
JOIN order_items as oi on oi.orderid=o.orderid
GROUP BY y.customerid, y.first_name, y.last_name, y.yas_segmenti
ORDER BY toplam_gelir DESC """

sehire_gore_yillik_siparis_egilimi=""" WITH sehir_yillik AS (
    SELECT 
        c.city, 
        YEAR(o.order_date) as yil, 
        SUM(oi.price) as yillik_gelir
    FROM customers as c
    JOIN orders as o ON c.customerid = o.customerid
    JOIN order_items as oi ON o.orderid = oi.orderid
    GROUP BY c.city, yil
)
SELECT 
    city, 
    yil, 
    yillik_gelir,
    LAG(yillik_gelir) OVER (PARTITION BY city ORDER BY yil) as onceki_yil_gelir,
    ROUND(((yillik_gelir - LAG(yillik_gelir) OVER (PARTITION BY city ORDER BY yil)) 
           / NULLIF(LAG(yillik_gelir) OVER (PARTITION BY city ORDER BY yil), 0)) * 100, 2) as artis_orani
FROM sehir_yillik
ORDER BY city, yil """

musteri_siparis_sirasi_rownum=""" SELECT c.customerid, c.first_name, c.last_name, o.orderid, ROW_NUMBER() OVER (PARTITION BY c.customerid 
order by o.orderid) as musteri_siparis FROM orders as o JOIN customers as c on o.customerid=c.customerid """

musteri_siparis_tutar_rank=""" SELECT c.customerid, c.first_name, c.last_name, oi.price, RANK() OVER (PARTITION BY c.customerid 
order by oi.price DESC) as siparis_tutari
FROM order_items as oi
JOIN orders as o on oi.orderid=o.orderid
JOIN customers as c on o.customerid=c.customerid """

aylik_satis_lag_farki=""" SELECT DATE_FORMAT(o.order_date,'%M') as ay, SUM(oi.price) as bu_ayki_toplam, LAG(SUM(oi.price)) OVER 
(ORDER BY MONTH(o.order_date)) as onceki_ay_toplam, SUM(oi.price)-LAG(SUM(oi.price)) over (ORDER BY MONTH(o.order_date)) as fark
FROM order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
GROUP BY ay, MONTH(o.order_date)
ORDER BY MONTH(o.order_date)    """

aylik_satis_yuzdelik_degisim= """ SELECT DATE_FORMAT(o.order_date,'%M') as ay_ismi, SUM(oi.price) as bu_ay_satis, LAG(SUM(oi.price)) OVER (ORDER BY MONTH(o.order_date)) as gecen_ay_satis,
ROUND((SUM(oi.price) - LAG(SUM(oi.price)) OVER (ORDER BY MONTH(o.order_date)))/ LAG(SUM(oi.price)) OVER (ORDER BY MONTH(o.order_date))* 100, 2) as fark_yuzde
FROM order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
GROUP BY ay_ismi, MONTH(o.order_date)      
ORDER BY MONTH(o.order_date) """

kategori_yillik_gelir_dense_rank=""" SELECT p.category, SUM(oi.price) as gelir, DATE_FORMAT(o.order_date,'%Y') as yil,
DENSE_RANK()OVER(PARTITION BY YEAR(o.order_date) ORDER BY SUM(oi.price)DESC) as siralanmis
FROM order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
JOIN products as p on p.productid=oi.productid
GROUP BY p.category, yil
ORDER BY yil,siralanmis """

urun_satis_yuzde_payi= """ SELECT p.productid, p.product_name, SUM(oi.price) as urunun_top_satis, SUM(SUM(oi.price)) OVER() as tum_urun_genel_top, 
(SUM(oi.price)/ SUM(SUM(oi.price)) OVER())*100 as yuzde from order_items as oi
JOIN products as p on oi.productid=p.productid
GROUP BY p.productid,p.product_name
ORDER BY urunun_top_satis DESC  """

musteri_yillik_harcama_ortalamasi=""" SELECT c.customerid,c.first_name,c.last_name, YEAR(o.order_date) as yil, AVG(SUM(oi.price)) over (PARTITION BY (YEAR(o.order_date))) as yillik_harcama FROM order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
JOIN customers as c on o.customerid=c.customerid
GROUP BY c.customerid, c.first_name, c.last_name, YEAR(o.order_date)
ORDER BY yillik_harcama DESC """

aylik_gelir_kumulatif_toplam=""" SELECT MONTH(o.order_date) as ay, SUM(oi.price) as total,
SUM(SUM(oi.price)) OVER (ORDER BY MONTH(o.order_date)) as kumulatif from order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
GROUP BY MONTH(o.order_date) 
ORDER BY ay """

kategori_bazli_en_pahali_10_siparis= """ SELECT * FROM (
	SELECT p.product_name, p.category, oi.price,
    ROW_NUMBER() OVER (PARTITION BY p.category order by oi.price desc) as en_pahali_urun
    FROM order_items as oi
    JOIN products as p on oi.productid=p.productid) as ham_liste
WHERE en_pahali_urun<=10
ORDER BY category, price DESC """

siparis_adedi_genel_ort_farki=""" SELECT c.customerid, c.first_name, c.last_name, COUNT(o.orderid) as siparis_sayisi, AVG(COUNT(o.orderid)) OVER() as genel_ort,
COUNT(o.orderid) - AVG(COUNT(o.orderid)) OVER() as fark
FROM orders as o 
JOIN customers as c on o.customerid=c.customerid
GROUP BY c.customerid,c.first_name,c.last_name """

rfm=""" SELECT c.customerid,c.first_name,c.last_name, DATEDIFF('2027-12-31',MAX(o.order_date)) as yeni_musteriler, COUNT(DISTINCT o.orderid) as 
musteri_sayisi, SUM(oi.price) as toplam_tutar
FROM order_items as oi 
JOIN orders as o on oi.orderid=o.orderid
JOIN customers as c on o.customerid=c.customerid
GROUP BY customerid, first_name, last_name
ORDER BY yeni_musteriler, musteri_sayisi, toplam_tutar """