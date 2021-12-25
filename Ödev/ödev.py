
print("soru1:")
D = 10
F = 60
print(F-D)

print("\nsoru2:")
for x in range(0,40):
    print(x)

print("\nsoru3:")
print("\"Ekonometrik Analiz\nVizde Ödevi Soruları\"")

print("\nsoru4:")
print("Pythonda kullandığımız değişken tipleri: int, float ve String'dir. int tam sayılar, float virgüllü sayılar, string ise metinler içindir")
a = 10    #tam sayı
b = 10.5  #virgüllü sayı
c = "on"  #metin

print("\nsoru5:")
print("**: üst alma")
print("+: toplama")
print("//: kat bölümü (sonucu en yakın tam sayıya yuvarlar)")
print("*: çarpma")
print("işlem sırası: üst alma - parantez içindeki işlem - çarpma veya bölme işlemleri - toplama veya çıkarma işlemleri")
print((2+5)+3**3//5*4)

print("\nsoru6:")

puan = 20
gecme_notu = 50

if puan >= gecme_notu:
    print("tebrikler, dersi geçtin!")
else:
    print("üzgünüm, dersten kaldın")
