import tkinter as tk
from tkinter import ttk
import customtkinter

#pip3 install customtkinter
#pip3 install customtkinter --upgrade
#pip install packaging
#pip install Pillow


# def open_settings():
#     print("Open Settings")

# def open_about():
#     print("Open About")

# def open_contact():
#     print("Open Contact")

# def open_shop():
#     shop_window = tk.Toplevel(root)
#     shop_window.title("KeyLingo Shop")

#     product_label = tk.Label(shop_window, text="Product:")
#     product_label.grid(row=0, column=0, padx=10, pady=10)

#     product_entry = tk.Entry(shop_window, width=30)
#     product_entry.grid(row=0, column=1, padx=10, pady=10)

#     quantity_label = tk.Label(shop_window, text="Quantity:")
#     quantity_label.grid(row=1, column=0, padx=10, pady=10)

#     quantity_entry = tk.Entry(shop_window, width=10)
#     quantity_entry.grid(row=1, column=1, padx=10, pady=10)

#     add_to_cart_button = tk.Button(shop_window, text="Add to Cart", command=lambda: add_to_cart(product_entry.get(), quantity_entry.get()))
#     add_to_cart_button.grid(row=2, column=0, columnspan=2, pady=10)

# def add_to_cart(product, quantity):
#     print(f"Added to Cart: {quantity} x {product}")

# def open_translator():
#     translator_window = tk.Toplevel(root)
#     translator_window.title("KeyLingo Translator")

#     text_label = tk.Label(translator_window, text="Enter Text:")
#     text_label.grid(row=2, column=0, padx=10, pady=10)

#     text_entry = tk.Entry(translator_window, width=30)
#     text_entry.grid(row=2, column=1, padx=10, pady=10)

#     translate_button = tk.Button(translator_window, text="Translate", command=lambda: translate_text(text_entry.get()))
#     translate_button.grid(row=3, column=0, columnspan=2, pady=10)

# def translate_text(text):
#     translation = f"Translated: {text} to: "
#     print(translation)



# title_label = tk.Label(root, text="Welcome to KeyLingo", font=("Helvetica", 16))
# title_label.pack(pady=10)

# description_label = tk.Label(root, text="Your key to a new language experience!")
# description_label.pack(pady=10)

# settings_button = tk.Button(root, text="Settings", command=open_settings)
# settings_button.pack(pady=5)


# shop_button = tk.Button(root, text="Open Shop", command=open_shop)
# shop_button.pack(pady=5)

# translator_button = tk.Button(root, text="Open Translator", command=open_translator)
# translator_button.pack(pady=5)

# exit_button = tk.Button(root, text="Exit", command=root.destroy)
# exit_button.pack(pady=20)

root = customtkinter.CTk()

class PageSwitcher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()

        self.geometry(f"{screenWidth}x{screenHeight}+0+0")
        root.title("KeyLingo Homepage")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, TranslatorPage, ShopPage, LearnPage, PracticePage, CustomizationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location; first is visible
    
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(bg='white')
        # customtkinter.set_appearance_mode("blue")
        # customtkinter.set_default_color_theme("dark-blue")

        label = tk.Label(self, text="Home Page")
        label.pack(pady=10)

        shop_button = tk.Button(self, text="Learn", command=lambda: controller.show_frame("ShopPage"))
        shop_button.pack(pady=10)

        shop_button = tk.Button(self, text="Practice", command=lambda: controller.show_frame("ShopPage"))
        shop_button.pack(pady=10)

        shop_button = tk.Button(self, text="Shop", command=lambda: controller.show_frame("ShopPage"))
        shop_button.pack(pady=10)

        shop_button = tk.Button(self, text="Customization", command=lambda: controller.show_frame("ShopPage"))
        shop_button.pack(pady=10)

        shop_button = tk.Button(self, text="Translator", command=lambda: controller.show_frame("TranslatorPage"))
        shop_button.pack(pady=10)


class TranslatorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="lightgreen")  
        self.grid_propagate(True)  

        label = tk.Label(self, text="Translator Page", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)
        

        switch_button = tk.Button(self, text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)


class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="lightcoral")  
        self.grid_propagate(True)  

        label = tk.Label(self, text="Shop Page", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)

        switch_button = tk.Button(self, text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)

class LearnPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    print("Learn")

class PracticePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    print("Practice")
    
class CustomizationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    print("Customization")

if __name__ == "__main__":
    app = PageSwitcher()
    app.mainloop()