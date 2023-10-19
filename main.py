from tkinter import *
import tkinter as tk
import customtkinter
import random

# Ekran Ayarları
ekran = tk.Tk()
ekran.title("Sayı Tahmin Etmece")
ekran.geometry("400x200")

# Tahmin
def tahmin():
    randoms = random.randrange(11)
    tahmn = textb.get("1.0", "end-1c")
    tahmn = int(tahmn)  # Doğru dönüşüm
    if tahmn > randoms:
        label.configure(text="Daha Küçük!")
    elif tahmn < randoms:
        label.configure(text="Daha Büyük!")
    else:
        label.configure(text="Doğru Sayı!!!")

# Label
label = customtkinter.CTkLabel(master=ekran, text="Sayı Tahmin Etmece")
label.pack(side=TOP, pady=20)

# Text Box
textb = customtkinter.CTkTextbox(master=ekran, height=20)
textb.place(x=100, y=75)

# Buton
buton = customtkinter.CTkButton(master=ekran, text="OK", command=tahmin)
buton.pack(side=BOTTOM, pady=30)

mainloop()
