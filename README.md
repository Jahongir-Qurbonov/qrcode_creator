# QRCode_creator

QR kod generatsiya qiluvchi kichik dastur

## Kerakli paketlarni o'rnatish

```bash
pip install qrcode
```

## Foydalanish

### Dastur  qo'llanmasi

```bash
python manage.py -h
```

### Qabul qiladigan argumentlar

```text
-h, --help                      Qo'llanma
-f FILE, --file FILE            Ma'lumotlar joylashgan fayl
--box_size BOX_SIZE             QR kod qutisining hajmi (x*x)
--border BORDER                 QR kod borderining qalinligi
--image_factory IMAGE_FACTORY   (Keyingi versiyalarda mavjud bo'ladi)
--out_folder OUT_FOLDER         QR kodlarni chiqarish uchun joy
```

### Default qiymatlar bilan

```text
-f FILE, --file FILE            data.txt
--box_size BOX_SIZE             10
--border BORDER                 6
--image_factory IMAGE_FACTORY   (Keyingi versiyalarda mavjud bo'ladi)
--out_folder OUT_FOLDER         images
```

### Foydalanishga misollar

Dastur hozircha faqat .png formatdagi rasmlarni generatsiya qila oladi.
Kiritilmagan argumentlar default qiymatlarni oladi!

Default o'rnatilgan `data.txt` fayli o'qilib qr kodlarni `images` papkasiga joylaydi

```bash
python manage.py
```

Bu yerda `malumotlar.txt` fayli o'qilib qr kodlarni `qr_rasmlar` papkasiga joylanadi

```bash
python manage.py --file malumotlar.txt --out_folder qr_rasmlar
```
