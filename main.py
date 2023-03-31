import tkinter as tk
from tkinter import messagebox

# Sözlük oluşturma
sozluk = {
    'apple': 'elma',
    'banana': 'muz',
    'cherry': 'kiraz',
    'hi':'selam'
}

# Arayüz oluşturma
root = tk.Tk()
root.title("Sözlük Uygulaması")

# Anahtar kelime için etiket ve giriş kutusu
label1 = tk.Label(root, text="Anahtar kelime:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

# Çeviri için etiket ve etiket kutusu
label2 = tk.Label(root, text="Çeviri:")
label2.grid(row=1, column=0)

result = tk.Label(root, text="")
result.grid(row=1, column=1)

# Çeviri işlevi
def ceviri():
    kelime = entry1.get().lower()
    if kelime in sozluk:
        result.config(text=sozluk[kelime])
    else:
        messagebox.showwarning("Hata", "Kelime bulunamadı.")

# Çeviri butonu
button = tk.Button(root, text="Çevir", command=ceviri)
button.grid(row=2, column=1)

root.mainloop()
