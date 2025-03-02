"""
# ---------------------------- Python'da Sayılar ----------------------------

# Tamsayılar (Integer)
# Matematikte gördüğümüz tüm sayılar (negatif, pozitif) Python'da bir veri tipidir.
# Tamsayılar, İngilizce olarak "Integer" olarak bilinir.
# Örnekler: -1000, 34, 2, 0

# Ondalıklı Sayılar (Float)
# Ondalıklı Sayılar veya diğer adıyla Kayan Sayılar, İngilizce olarak "Float" olarak bilinir.
# Örnekler: 3.14, 3.554546, -13.54

# ---------------------------- Basit Matematiksel Operatörler ----------------------------

# Toplama
toplama = 3 + 4
print("Toplama:", toplama)  # Sonuç: 7

# Çıkarma
cikarma = 5 - 17
print("Çıkarma:", cikarma)  # Sonuç: -12

# Çarpma
carpma = 13 * 4
print("Çarpma:", carpma)  # Sonuç: 52

# Bölme
bolme = 4 / 2
print("Bölme:", bolme)  # Sonuç: 2.0 (float sonucu)

# ---------------------------- Değişkenler ve Değişken Tanımlama ----------------------------

# Değişken ismi ve Değişkenin değeri
i = 10
print("Değişken i:", i)

# Değişkeni kullanma
print("i'nin küpü:", i * i * i)  # Sonuç: 1000

# Değişkenin değerini değiştirme
i = 15
print("Yeni i:", i)

# Farklı Değişkenler
a = 4
b = 3
c = a + 2 * b
print("c'nin değeri:", c)  # Sonuç: 10

# ---------------------------- Değişken İsimlendirme Kuralları ----------------------------

# Değişken isimleri şu kurallara dikkat edilerek verilmelidir:
# 1. Değişken isimleri bir sayı ile başlayamaz.
# 2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
# 3. :'",<>/?|\()!@#$%^&*~-+ gibi semboller değişken ismi içinde kullanılamaz (Sadece _ sembolü kullanılabilir).
# 4. Python'da tanımlı anahtar kelimeler (while, not, vs.) değişken ismi olarak kullanılamaz.

# ---------------------------- Değişken Değerlerini Değiştirme ----------------------------

# Python'da iki değişkenin değerini birbirleriyle değiştirmek için pratik bir yöntem:
a = 4
b = 3
print("Değişkenler (önce): a =", a, ", b =", b)

# Değişkenlerin değerlerini değiştirme
a, b = b, a
print("Değişkenler (sonra): a =", a, ", b =", b)

# ---------------------------- Değişken Artırma ----------------------------

# Değişkenin değerini artırmak için kullanılan pratik bir yöntem:
a = 5
a += 1  # Bu işlem "a = a + 1" ile aynı anlama gelir
print("Artırılmış a:", a)  # Sonuç: 6

# ---------------------------- Yorum Satırları ----------------------------

# Yorum satırları, programlarımıza açıklama eklememizi sağlar. Yorum satırları Python tarafından çalıştırılmaz.

# Tekli Yorum Satırı
# Bu satır bir açıklamadır.

# Çoklu Yorum Satırı
"""
"""
Bu birden fazla satırdan oluşan yorum bloğudur.
Python tarafından göz ardı edilir ve çalıştırılmaz.

"""

# ---------------------------- Karakter Dizileri (Stringler) ----------------------------
"""

# Python'da bir veri tipi olan Stringler veya Türkçe ismiyle karakter dizileri, gerçek hayatta kullandığımız yazıların aynısıdır.
# Bu veri tipi aslında her biri bir karakter olan bir dizidir. Örnek olarak, "ali" stringi sırasıyla
# a, l, i harflerinden veya karakterlerden oluşmaktadır. Bu konuda stringleri ve stringlerin özelliklerini
# görmeye çalışacağız.

# ---------------------------- String Oluşturma ----------------------------
"""

# Python'da string oluşturmanın birkaç yolu vardır. Hangisini kullanacağınız tamamen size bağlıdır.

# 1. Tek tırnak ile string oluşturma
'Erkan Yurtoğlu'

# 2. Çift Tırnak ile string oluşturma
"Erkan Yurtoğlu"

# 3. Üçlü Tırnak ile string oluşturma
"""Erkan Yurtoğlu""""""

# Eğer çift tırnak ile başlıyorsak, çift tırnakla bitirmek gerekiyor. Aksi takdirde hata alırız.
# Hatalı Kod:
# "Merhaba'
#  SyntaxError: EOL while scanning string literal

# Hatalı Kod:
# 'Merhaba"
#  SyntaxError: EOL while scanning string literal

# Şimdi de bir tane string veri tipinde değişken oluşturalım.
a = "Merhaba"
print(a)  # Çıktı: Merhaba

naber = "Naber iyi misin ?"
print(naber)  # Çıktı: Naber iyi misin ?

# ---------------------------- String İndeksleme ve Parçalama ----------------------------

# Stringler birer karakter dizisi oldukları için her bir karakterin aslında string içinde bir yeri vardır.
# Pythonda ve çoğu programlama dilinde (Octave hariç) stringlerin indekslenmesi "0"dan başlar.

# 0. elemana ulaşalım. Bunun için [] operatörünü kullanacağız.
a = "ali"
print(a[0])  # Çıktı: 'a'

# 1. eleman
print(a[1])  # Çıktı: 'l'

# 2. eleman
print(a[2])  # Çıktı: 'i'

# Pythonda stringler sondan da indekslenebilirler. Sondan başlayarak -1, -2, -3... şeklinde indekslenirler.

# Sondaki eleman "-1" eleman
a = "murat"
print(a[-1])  # Çıktı: 't'

# -2. eleman
print(a[-2])  # Çıktı: 'a'

# -3. eleman
print(a[-3])  # Çıktı: 'r'

# -4. eleman
print(a[-4])  # Çıktı: 'u'

# -5. eleman
print(a[-5])  # Çıktı: 'm'

# ---------------------------- String Parçalama ----------------------------

# Bir string'in sadece belirli bir kısmını elde etmek için : ve [] işaretlerini kullanacağız.
# Formülümüz şu şekilde:

# [başlama indeksi : bitiş indeksi : atlama değeri]

a = "Python Programlama Dili"
# 4. indeksten başla, 10. indekse kadar (dahil değil) al.
print(a[4:10])  # Çıktı: 'on Pro'

# Başlangıç değeri belirtilmemişse, en baştan başlayarak alır.
print(a[:10])  # Çıktı: 'Python Pro'

# Bitiş değeri belirtilmemişse, en sonuna kadar alır.
print(a[4:])  # Çıktı: 'on Programlama Dili'

# İki değer de belirtilmemişse, tüm stringi alır.
print(a[:])  # Çıktı: 'Python Programlama Dili'

# Son karaktere kadar alır.
print(a[:-1])  # Çıktı: 'Python Programlama Dil'

# Baştan sona 2 değer atlaya atlaya stringi alır.
print(a[::2])  # Çıktı: 'Pto rgalm ii'

# 4. indeksten 12. indekse 3'er atlayarak stringi alır.
print(a[4:12:3])  # Çıktı: 'oPg'

# Baştan sona -1 atlayarak stringi alır (string'i ters çevirme).
print(a[::-1])  # Çıktı: 'iliD amalmargorP nohtyP'

# ---------------------------- String Özellikleri ----------------------------

# Bir string'in uzunluğunu nasıl buluruz? Bunun için Python'da len() fonksiyonu bulunmaktadır.
a = "Python Programlama Dili"
print(len(a))  # Çıktı: 23

# ---------------------------- String Karakter Değiştirme ----------------------------

# Bir string'in belli bir karakterini direkt olarak değiştiremezsiniz.
a = "Murat"
# Python buna izin vermez
# Hata verir: TypeError: 'str' object does not support item assignment
# a[0] = 'T'

# ---------------------------- String Birleştirme ----------------------------

# Stringleri birbirine eklemek mümkündür.
a = "Python "
b = "Programlama "
c = "Dili"
print(a + b + c)  # Çıktı: 'Python Programlama Dili'

# String ile bir sayıyı çarpmak mümkündür.
# Python * 3 aslında Python + Python + Python işlemine eşdeğerdir.
print("Python" * 3)  # Çıktı: 'PythonPythonPython'

"""
"""
### ---------------------------- Tamsayıyı Ondalıklı Sayıya Çevirme ----------------------------
# Bir tamsayıyı float'a çevirmek için float() fonksiyonunu kullanabiliriz.

# Örnekler:
a = 43
print(float(a))  # Çıktı: 43.0

print(float(-1))  # Çıktı: -1.0

print(float(9))   # Çıktı: 9.0

### ---------------------------- Ondalıklı Sayıyı Tamsayıya Çevirme ----------------------------
# Bir float'ı tamsayıya çevirmek için int() fonksiyonunu kullanabiliriz.
# Ancak, sadece tam kısmı alınır, ondalıklı kısım silinir.

print(int(4.7))  # Çıktı: 4

print(int(3.14))  # Çıktı: 3

print(int(10.99))  # Çıktı: 10

a = 4
b = 2
print(int(a / b))  # Çıktı: 2

### ---------------------------- Sayıları String'e Çevirme ----------------------------
# Sayıları string formatına çevirmek için str() fonksiyonunu kullanabiliriz.

a = 32324324
b = str(a)
print(b)       # Çıktı: '32324324'
print(len(b))  # Çıktı: 8

t = 3.14343
y = str(t)
print(y)       # Çıktı: '3.14343'
print(len(y))  # Çıktı: 7

### ---------------------------- Stringleri Tamsayıya Çevirme ----------------------------
# Bir string'i tamsayıya çevirmek için int() fonksiyonunu kullanabiliriz.
# Ancak string'in sadece rakamlardan oluşması gerekir.

a = "32434324324234"
b = int(a)
print(b)  # Çıktı: 32434324324234

# Hatalı kullanım:
# a = "dasdasd343435"
# b = int(a)  # HATA: ValueError

### ---------------------------- Stringleri Ondalıklı Sayıya Çevirme ----------------------------
# Bir string'i float'a çevirmek için float() fonksiyonunu kullanabiliriz.

a = "3.1444545"
b = float(a)
print(b)  # Çıktı: 3.1444545

# Hatalı kullanım:
# a = "3.14.324324"  # Hatalı format
# b = float(a)  # HATA: ValueError

"""

"""
# ---------------------------- print() Fonksiyonu ----------------------------

# print() fonksiyonu ekrana veri yazdırmak için kullanılır.
print(35)  # Çıktı: 35
print(3.14)  # Çıktı: 3.14
a = 4
b = 15
print(a + b)  # Çıktı: 19
print("Erkan Yurtoğlu")  # Çıktı: Erkan Yurtoğlu

# ---------------------------- Birden Fazla Değer Yazdırma ----------------------------

# Birden fazla değeri yazdırmak için aralarına , koyabilirsiniz.
print("Erkan", 12, 545, 66767, 3.56)  # Çıktı: Erkan 12 545 66767 3.56
print("Erkan", "Poyraz", "Yurtoğlu")  # Çıktı: Erkan Poyraz Yurtoğlu

# ---------------------------- Stringlerdeki Özel Karakterler ----------------------------

# \n karakteri, alt satıra geçer.
print("Merhaba\nNasılsın\nİyi misin")
# Çıktı:
# Merhaba
# Nasılsın
# İyi misin

# \t karakteri, tab boşluğu ekler.
print("Ocak\tMart\tŞubat")
# Çıktı: Ocak    Mart    Şubat

# ---------------------------- type() Fonksiyonu ----------------------------

# type() fonksiyonu bir değişkenin veri tipini gösterir.
a = 65
print(type(a))  # Çıktı: <class 'int'>

a = 5.87
print(type(a))  # Çıktı: <class 'float'>

a = "Murat"
print(type(a))  # Çıktı: <class 'str'>

# ---------------------------- print() Fonksiyonunun Özellikleri ----------------------------

# sep parametresi ile yazdırılan değerler arasına istediğimiz karakteri koyabiliriz.
print(3, 4, 5, 6, 7, 8, 9)  # Çıktı: 3 4 5 6 7 8 9
print(3, 4, 5, 6, 7, 8, 9, sep=".")  # Çıktı: 3.4.5.6.7.8.9
print("06", "04", "2015", sep="/")  # Çıktı: 06/04/2015
print("Erkan", "Poyraz", "Yurtoğlu", sep="\n")  # Çıktı:
# Erkan
# Poyraz
# Yurtoğlu

# ---------------------------- Yıldızlı Parametreler ----------------------------

# * işaretiyle bir string'in her bir karakterini ayrı ayrı yazdırabiliriz.
print(*"Python")  # Çıktı: P y t h o n
print(*"Python", sep="\n")  # Çıktı:
# P
# y
# t
# h
# o
# n
print(*"TBMM", sep=".")  # Çıktı: T.B.M.M

# ---------------------------- Formatlama ----------------------------

# format() fonksiyonu, bir string içinde değişken değerlerini yerleştirmek için kullanılır.
print("{} {} {}".format(3.1423, 5.324, 7.324324))  # Çıktı: 3.1423 5.324 7.324324

a = 3
b = 4
print("{} + {} 'nin toplamı {} 'dır".format(a, b, a + b))  # Çıktı: 3 + 4 'nin toplamı 7 'dır

# Süslü parantezlerdeki indeksler ile sırayı değiştirebiliriz.
print("{1} {0} {2}".format(43, "Murat", 54))  # Çıktı: Murat 43 54

# Ondalık kısmı sınırlamak için format fonksiyonunu kullanabiliriz.
print("{:.2f} {:.2f} {:.3f}".format(3.1463, 5.324, 7.324324))
# Çıktı: 3.15 5.32 7.324

"""

