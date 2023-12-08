import tkinter as tk
from tkinter import ttk

def open_settings():
    print("Open Settings")

def open_about():
    print("Open About")

def open_contact():
    print("Open Contact")

def open_shop():
    shop_window = tk.Toplevel(root)
    shop_window.title("KeyLingo Shop")

    product_label = tk.Label(shop_window, text="Product:")
    product_label.grid(row=0, column=0, padx=10, pady=10)

    product_entry = tk.Entry(shop_window, width=30)
    product_entry.grid(row=0, column=1, padx=10, pady=10)

    quantity_label = tk.Label(shop_window, text="Quantity:")
    quantity_label.grid(row=1, column=0, padx=10, pady=10)

    quantity_entry = tk.Entry(shop_window, width=10)
    quantity_entry.grid(row=1, column=1, padx=10, pady=10)

    add_to_cart_button = tk.Button(shop_window, text="Add to Cart", command=lambda: add_to_cart(product_entry.get(), quantity_entry.get()))
    add_to_cart_button.grid(row=2, column=0, columnspan=2, pady=10)

def add_to_cart(product, quantity):
    print(f"Added to Cart: {quantity} x {product}")

def open_translator():
    translator_window = tk.Toplevel(root)
    translator_window.title("KeyLingo Translator")

    text_label = tk.Label(translator_window, text="Enter Text:")
    text_label.grid(row=2, column=0, padx=10, pady=10)

    text_entry = tk.Entry(translator_window, width=30)
    text_entry.grid(row=2, column=1, padx=10, pady=10)

    translate_button = tk.Button(translator_window, text="Translate", command=lambda: translate_text(text_entry.get()))
    translate_button.grid(row=3, column=0, columnspan=2, pady=10)

def translate_text(text):
    translation = f"Translated: {text} to: "
    print(translation)

root = tk.Tk()
root.title("KeyLingo Homepage")

title_label = tk.Label(root, text="Welcome to KeyLingo", font=("Helvetica", 16))
title_label.pack(pady=10)

description_label = tk.Label(root, text="Your key to a new language experience!")
description_label.pack(pady=10)

settings_button = tk.Button(root, text="Settings", command=open_settings)
settings_button.pack(pady=5)


shop_button = tk.Button(root, text="Open Shop", command=open_shop)
shop_button.pack(pady=5)

translator_button = tk.Button(root, text="Open Translator", command=open_translator)
translator_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)

class PageSwitcher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x300")
        self.title("Page Switching Example")

        self.home_page = HomePage(self)
        self.translator_page = TranslatorPage(self)
        self.shop_page = ShopPage(self)

        self.show_home_page()

    def show_home_page(self):
        self.translator_page.grid_forget()
        self.shop_page.grid_forget()
        self.home_page.grid()

    def show_translator_page(self):
        self.home_page.grid_forget()
        self.shop_page.grid_forget()
        self.translator_page.grid()

    def show_shop_page(self):
        self.home_page.grid_forget()
        self.translator_page.grid_forget()
        self.shop_page.grid()

class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="Home Page")
        label.pack(pady=10)

        switch_button = tk.Button(self, text="Go to Translator", command=master.show_translator_page)
        switch_button.pack(pady=10)

        shop_button = tk.Button(self, text="Go to Shop", command=master.show_shop_page)
        shop_button.pack(pady=10)

class TranslatorPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(bg="lightgreen")  
        self.grid_propagate(True)  

        label = tk.Label(self, text="Translator Page", font=("Helvetica", 14))
        label.pack(pady=10)

        switch_button = tk.Button(self, text="Go to Home", command=master.show_home_page, width=20, height=2)
        switch_button.pack(pady=10)

class ShopPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(bg="lightcoral")  
        self.grid_propagate(True)  

        label = tk.Label(self, text="Shop Page", font=("Helvetica", 14))
        label.pack(pady=10)

        switch_button = tk.Button(self, text="Go to Home", command=master.show_home_page, width=20, height=2)
        switch_button.pack(pady=10)


if __name__ == "__main__":
    app = PageSwitcher()
    app.mainloop()