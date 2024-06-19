from tkinter import *
import subprocess
from tkinter import messagebox
import os

# Pencereyi oluştur
pencere1 = Tk()
pencere1.title("Alt Domain Bulma")
pencere1.geometry("400x400")

def domain():
    domain_name = entr1.get()

    try:
        # Sublist3r komutunu çalıştır
        result = subprocess.run(
            ["sublist3r", "-d", domain_name, "-o", "alt_domainler.txt"],
            capture_output=True,
            text=True
        )
        
        # Çıktıyı kontrol et
        if result.returncode == 0:
            messagebox.showinfo("Bilgi", f"Alt domain arama tamamlandı. Sonuçlar alt_domainler.txt dosyasına kaydedildi.")
        else:
            messagebox.showerror("Hata", f"Alt domain arama sırasında bir hata oluştu:\n{result.stderr}")
    
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Kullanıcı arayüzü bileşenlerini oluştur
label1 = Label(pencere1, text="Lütfen domain adresini giriniz")
label1.pack()

entr1 = Entry(pencere1)
entr1.pack()

buton1 = Button(pencere1, text="Alt domain bulmak için tıklayın", command=domain)
buton1.pack()

# Pencereyi çalıştır
pencere1.mainloop()
