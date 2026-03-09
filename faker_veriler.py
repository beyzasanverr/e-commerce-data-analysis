from faker import Faker
from datetime import date
import random
fake=Faker("en_US")

# hazır veritabanını kullanmak yerine gerçek hayat senaryolarında karşılaşabileceğim eksik veri- veri tipi tutarsızlığı gibi durumları görebilmek 
# ve nasıl yöneteceğimi anlayabilmek için Faker kütüphanesi yardımıyla verileri kendim hazırlatmak istedim. Bu dosyada da Faker
# kütüphanesi yardımıyla verilerin üretildiği aşamalar yer alıyor.
# veriler üretildikten sonra txt dosyasında kaydedildi bunu da txt dosyasında var olan verileri veritabanına sorgu ile "toplu veri aktarımı" 
# durumunu deneyimlemek istediğim için yaptım.

# cutomers tablosu için ilgili veriler:

with open("out_customers.txt", "w", encoding="utf-8") as f:
    for i in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name}.{last_name}@example.com"
        phone=fake.phone_number()
        city=fake.city()
        start_date=date(1997,1,1)
        end_date=date(2027,12,31)
        d=fake.date_between(start_date=start_date,end_date=end_date).strftime("%Y-%m-%d")
        birth_year=(fake.date_of_birth(minimum_age=15,maximum_age=80).strftime("%Y"))
        f.write(f"('{first_name}', '{last_name}', '{email}','{phone}','{city}', '{d}', '{birth_year}'), \n")

# products tablosu için ilgili veriler:
# Faker kütüphanesinde eşyaların/ürünlerin rastgele üretileceği bir fonksiyon olmadığından ürünleri kendim liste olarak tanımladım:
products = [
    "Wireless Bluetooth Speaker","Gaming Mouse","Mechanical Keyboard","4K UHD Monitor","Laptop Stand","Smartwatch","USB-C Fast Charger","Powerbank 20000mAh","Noise Cancelling Headphones","HD Web Camera","Portable SSD 1TB","Fitness Tracker Band","Wireless Earbuds","Smart TV 55 Inch","Robot Vacuum Cleaner","Electric Toothbrush","Digital DSLR Camera","Action Camera 4K","Bluetooth Car Adapter","Smart Doorbell","HDMI Cable 2M","Gaming Chair","VR Headset","Portable Projector","Waterproof Bluetooth Speaker","Wireless Gaming Controller","Laptop Backpack",
    "Foldable Drone","Smart Thermostat","USB Desk Fan","LED Desk Lamp","Air Purifier","Electric Kettle","Espresso Coffee Machine","Cordless Hair Clipper","Smart Light Bulb","Bluetooth Sleep Headphones","Electric Scooter","Ceramic Space Heater","Insulated Water Bottle","Rechargeable Hand Warmer","Memory Foam Pillow","Outdoor Camping Tent","Inflatable Air Mattress", "Yoga Mat Non Slip","Adjustable Dumbbells","Foam Roller Set","Golf Training Net","Tennis Racket Graphite","Noise Isolating Earphones","Car Phone Mount",
    "Smart Bike Helmet","Kids Tablet Android","Educational Coding Kit","Board Game Strategy","Puzzle 1000 Pieces","LED String Lights","Scented Soy Candles","Organic Cotton Sheets","Memory Foam Mattress","Wooden Coffee Table","Decorative Wall Art","Ceramic Vase Pottery","Indoor Plant Stand","Bamboo Cutting Board","Cast Iron Skillet","Stainless Steel Knife Set","Nonstick Cookware Set","Silicone Baking Mats","Refrigerator Water Dispenser","Microwave Oven","Air Fryer XL","Slow Cooker","Rice Cooker","Blender Professional","Juicer Extractor",
    "Hand Mixer","Electric Griddle","Vacuum Sealer Machine","Dish Drying Rack","Baby Stroller Foldable","Baby Monitor Video","Convertible Car Seat","Kids Ride-On Toy","Adjustable High Chair","Children's Story Book Set","Educational Flash Cards","Plush Teddy Bear","Toddler Building Blocks","Girls Fashion Sneakers","Men Running Shoes","Leather Belt","Wool Scarf","Baseball Cap","Sunglasses Polarized","Sport Socks Pack","Fitness Shorts Men","Yoga Pants Women","Denim Jacket Unisex","Classic T-Shirt",
    "Casual Hooded Sweatshirt","Slim Fit Jeans","Formal Dress Shirt","Knit Beanie Hat","Leather Wallet","Travel Duffel Bag","Luggage Set 3pcs","Camping Sleeping Bag","Hiking Backpack","Waterproof Hiking Boots","Trail Running Shoes","Outdoor Sunglasses","Tactical Flashlight","Multi-Tool Pocket Knife","Survival Gear Kit","Home Security Camera","Smart Lock Keypad","GPS Tracker Device","Car Jump Starter","Tire Pressure Gauge","Car Vacuum Cleaner","Dash Cam Full HD","Roof Cargo Box","Electric Pressure Washer",
    "Garden Hose Reel","Plant Watering System","Lawn Mower Electric","Cordless Leaf Blower","Patio Outdoor Furniture Set","Hammock Swing Chair","BBQ Grill Gas","Picnic Blanket Waterproof","Inflatable Pool","Pool Floats Set","Beach Umbrella","Kids Water Toys","Snorkeling Set Full","Swim Goggles Anti-Fog","Surfboard Beginner","Kayak Single Sit-On-Top","Electric Bike Mountain", "Portable Car Battery Charger", "Solar Power Bank","LED Flashlight Rechargeable","Camping Cookware Set","Hiking Trekking Poles","Smartphone Screen Protector","Wireless Charging Pad","Laptop Cooling Pad","Tablet Keyboard Case","USB Hub 7 Ports","Bluetooth FM Transmitter","Car Air Purifier","Dash Mount Phone Holder"
]

with open("out_products.txt","w",encoding="utf-8") as f:
    for i in range(1000):
        product_name=(random.choice(products))
        product_unitprices=fake.random_int(min=100, max=5000)
        cost= product_unitprices*0.07
        f.write(f"('{product_name}', {product_unitprices}, {cost}),\n")

start_date=date(1997,1,1)
end_date=date(2027,12,31)

# yine ödeme yöntemlerinin rastgele üretildiği hazır bir fonksiyon bulunmadığından Ödeme Yöntemleri için kendim liste tanımladım:
payment_methods = ["Credit Card","Debit Card","Visa","Mastercard","American Express","Discover","Maestro","PayPal","Apple Pay",
    "Google Pay","Samsung Pay","Amazon Pay","Bank Transfer","Wire Transfer","Direct Debit","Cash on Delivery","Card on Delivery","Gift Card",
    "Store Credit","Klarna","Afterpay","Affirm","Bitcoin","Ethereum","USDT"]

# orders tablosu için gerekli veriler:

customer_ids = list(range(1, 1001))
with open("out_orders.txt","w",encoding="utf-8") as f:
     for i in range(1000):
        order_date=fake.date_between(start_date=start_date,end_date=end_date).strftime("%Y-%m-%d")
        orders_payments=(random.choice(payment_methods))
        total_amount=fake.random_int(min=0, max=50)
        customer_id = random.choice(customer_ids) 
        f.write(f"({customer_id},'{order_date}','{orders_payments}', {total_amount}),\n")

# order_items tablosu için gerekli veriler:

order_ids = list(range(1, 1001))
product_ids=list(range(1, 1001))
with open("out_order_items.txt","w",encoding="utf-8") as f:
     for i in range(1000):
        order_id = random.choice(order_ids) 
        product_id=random.choice(product_ids)
        quantity=fake.random_int(min=1,max=50)
        price=quantity*product_unitprices
        f.write(f"({order_id}, {product_id}, {quantity}, {price}),\n")
