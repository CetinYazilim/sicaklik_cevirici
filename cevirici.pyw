#!/usr/bin/env python2
from Tkinter import *
#Pencereyi ayarlama
pen = Tk()
#Başlık
pen.title("Sıcaklık Çevirici")
#Pencere boyutları
pen.geometry("400x170+200+200")
#Renk ayarı
pen.tk_setPalette("#e6e6e6")
#İkon
simge = PhotoImage(file="ikon.gif")
pen.tk.call('wm', 'iconphoto', pen._w, simge)
#Veri giriş kutularını oluşturma ve yerleştirme
#Oluşturma
c_entry = Entry(width=25, bg="white")
#Yerleştirme
c_entry.place(relx=0.45, rely=0.1)
f_entry = Entry(width=25, bg="white")
f_entry.place(relx=0.45, rely=0.3)
#Etiketleri oluşturma ve yerleştirme
c_label = Label(text="Santigrat degerini yazin: ")
c_label.place(relx=0.05, rely=0.1)
f_label = Label(text="Fahrenheit degerini yazin: ")
f_label.place(relx=0.03, rely=0.3)
#Santigratı fahrenheit a çeviren komut
def cf_hesapla():
  #Komutu dene:
  try:
    #Santigrat kutusuna girilen veriyi oku
    c_str = c_entry.get()
    #Veriyi ondalık ifadeye çevir
    c = float(c_str)
    #Çevirme formulu
    cf_sonuc = c * 1.8 + 32
    #Sonucu gösteren yazı
    labelicerigi_cf = c, "Santigrat", "=", cf_sonuc, "Fahrenheit"
    #Yazıyı yaz
    sonuc_label['text'] = labelicerigi_cf
    #Giriş kutusunu temizle
    c_entry.delete(0, END)
    #Girilen veri hatalıysa:
  except ValueError:
    #Giriş kutusunu sil ve hata mesajı ver
    c_entry.delete(0, END)
    c_entry.insert(END, "Lütfen geçerli bir değer girin")

#Fahrenheit ı santigrat a çeviren komut
def fc_hesapla():
  #Komutu dene:
  try:
    #Fahrenheit kutusuna yazılan veriyi oku
    f_str = f_entry.get()
    #Veriyi ondalık ifadeye çevir        
    f = float(f_str)
    #Çevirme formulu
    fc_sonuc = (f - 32) // 1.8
    #Sonucu gösteren yazı
    labelicerigi_fc = f, "Fahrenheit", "=", fc_sonuc, "Santigrat"
    #Yazıyı yaz
    sonuc_label['text'] = labelicerigi_fc
    f_entry.delete(0, END)
  #Girilen veri hatalıysa:
  except ValueError:
    #Giriş kutusunu sil ve hata mesajı ver
    f_entry.delete(0, END)
    f_entry.insert(END, "Lütfen geçerli bir değer girin")

#Düğmeleri oluşturma ve yerleştirme
cf_hesap_dm = Button(text="Santigratı Çevir", command=cf_hesapla, bg="blue", fg="white")
cf_hesap_dm.place(relx=0.35, rely=0.63)

fc_hesap_dm = Button(text="Fahrenheitı Çevir", command=fc_hesapla, bg="blue", fg="white")
fc_hesap_dm.place(relx=0.34, rely=0.81)

sonuc_label = Label(text="      Sonuç burada yazacaktır")
sonuc_label.place(relx=0.25, rely=0.50)
#Markayı belirten yazı :)
cetin_yazilim_label = Label(text="Çetin Yazılım 2015")
cetin_yazilim_label.place(relx=0.70, rely=0.9)

mainloop()
