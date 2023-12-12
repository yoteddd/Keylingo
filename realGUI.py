import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk, Image

#pip3 install customtkinter
#pip3 install customtkinter --upgrade
#pip install packaging
#pip install Pillow

root = customtkinter.CTk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

class PageSwitcher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

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

        label = tk.Label(self, text="Keylingo Home Page", font=("Comic Sans MS", 36))
        label.pack(pady=10)

        canvas = tk.Canvas(self, width=screenWidth, height=screenHeight - (screenHeight/11))
        canvas.create_rectangle(0, 0, screenWidth, screenHeight, fill="#FFEDA9")
        canvas.place(x=0, y=screenHeight/11)

        # img = ImageTk.PhotoImage(Image.open("bigfatprojectgui/Sam.png"))
        # panel = tk.Label(root, image = img)
        # panel.pack()

#x1 y1 x2 y2
        statsRectangle = canvas.create_rectangle(screenWidth-screenWidth/10,screenHeight-screenHeight/2,screenWidth-screenWidth/2,screenHeight-screenHeight/1.1, outline = "black", fill = "#FFFFFF")
        stats_label = tk.Label(canvas, font=("Comic Sans MS", 20), text="Dashboard & News *WIP*")
        stats_label.place(x = (screenWidth-screenWidth/2.5), y= (screenHeight-screenHeight/1.1))

        coinsRectangle = canvas.create_rectangle(screenWidth-screenWidth/60,(screenHeight-screenHeight/1.1)-60,screenWidth-screenWidth/6,(screenHeight-screenHeight/1.1)-10, fill = "#000000")
        coin_label = tk.Label(canvas, font=("Comic Sans MS", 20), text="69 Coins")
        coin_label.place(x = (screenWidth-screenWidth/6)+25, y= (screenHeight-screenHeight/1.1)-45)

        temp_sam = canvas.create_oval(screenWidth-screenWidth/3.5, screenHeight-screenHeight/4, screenWidth-screenWidth/6.9, screenHeight-screenHeight/2.3, fill="grey", outline="black")
        sam_label = tk.Label(canvas, font=("Comic Sans MS", 20), text="Sam >:)")
        sam_label.place(x = (screenWidth-screenWidth/4), y=(screenHeight-screenHeight/2.8))
        shift_y = 50

        learn_button = tk.Button(self, font=("Helvetica", 18), text="Learn", command=lambda: controller.show_frame("LearnPage"), width=40, height=2)
        learn_button.place(anchor="w", x=screenWidth / 20, y=screenHeight / 11 + shift_y)

        practice_button = tk.Button(self, font=("Helvetica", 18), text="Practice", command=lambda: controller.show_frame("PracticePage"), width=40, height=2)
        practice_button.place(anchor="w", x=screenWidth / 20, y=screenHeight / 11 + shift_y * 2)

        shop_button = tk.Button(self, font=("Helvetica", 18), text="Shop", command=lambda: controller.show_frame("ShopPage"), width=40, height=2)
        shop_button.place(anchor="w", x=screenWidth / 20, y=screenHeight / 11 + shift_y * 3)

        customization_button = tk.Button(self, font=("Helvetica", 18), text="Customization", command=lambda: controller.show_frame("CustomizationPage"), width=40, height=2)
        customization_button.place(anchor="w", x=screenWidth / 20, y=screenHeight / 11 + shift_y * 4)

        translator_button = tk.Button(self, font=("Helvetica", 18), text="Translator", command=lambda: controller.show_frame("TranslatorPage"), width=40, height=2)
        translator_button.place(anchor="w", x=screenWidth / 20, y=screenHeight / 11 + shift_y * 5)

        exit_button = tk.Button(self, font=("Helvetica", 18), text="Exit", command=self.master.destroy, width=40, height=2)
        exit_button.place(anchor="w", x=screenWidth / 20, y=screenHeight / 11 + shift_y * 6)
        



MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

def encrypt_to_morse(text):
    encrypted_text = ''
    for char in text.upper():
        if char != ' ':
            encrypted_text += MORSE_CODE[char] + ' '
        else:
            encrypted_text += ' '
    return encrypted_text

def decrypt_from_morse(morse_code):
    morse_code += ' '
    decrypted_text = ''
    morse_char = ''
    for symbol in morse_code:
        if symbol != ' ':
            i = 0
            morse_char += symbol
        else:
            i += 1
            if i == 2:
                decrypted_text += ' '
            else:
                decrypted_text += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(morse_char)]
                morse_char = ''
    return decrypted_text

class TranslatorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="lightgreen")  
        self.grid_propagate(True)  

        label = tk.Label(self, text="Translator Page", font=("Helvetica", 24))
        label.pack(side="top", fill="x", pady=10)

        entry_label = tk.Label(self, font=("Helvetica", 24), text="Enter Text: ")
        entry_label.pack()

        entry_widget = tk.Entry(self, width = 60)
        entry_widget.pack()

        result_label = tk.Label(self, font=("Helvetica", 24), text="Result: ")
        result_label.pack()

        result_text = tk.Text(self, width= 80)
        result_text.pack()

        encrypt_button = tk.Button(self, font=("Helvetica", 24), text="Translate to Morse Code", command=lambda: self.translate(entry_widget.get(), result_text, encrypt=True))
        encrypt_button.pack(pady=5)

        decrypt_button = tk.Button(self, font=("Helvetica", 24), text="Translate from Morse Code", command=lambda: self.translate(entry_widget.get(), result_text, encrypt=False))
        decrypt_button.pack(pady=5)
        

        switch_button = tk.Button(self, text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)
    def translate(self, text, result_text_widget, encrypt=True):
        if encrypt:
            result = encrypt_to_morse(text)
        else:
            result = decrypt_from_morse(text)
        result_text_widget.delete(1.0, tk.END)
        result_text_widget.insert(tk.END, result)
        
class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="lightcoral")  
        self.grid_propagate(True)  

        label = tk.Label(self, text="Shop Page (Will have customization items for users to buy using coins.) *WIP*", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)

        switch_button = tk.Button(self, font=("Helvetica", 14), text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)

        product_label = tk.Label(self, font=("Helvetica", 24), text="Product:")
        product_label.pack(pady=10)

        product_entry = tk.Entry(self, width=30)
        product_entry.pack(pady=10)

        quantity_label = tk.Label(self, font=("Helvetica", 24), text="Quantity:")
        quantity_label.pack(pady=10)

        quantity_entry = tk.Entry(self, width=10)
        quantity_entry.pack(pady=10)

        add_to_cart_button = tk.Button(self, font=("Helvetica", 24),text="Add to Cart", command=lambda: self.add_to_cart(product_entry.get(), quantity_entry.get()))
        add_to_cart_button.pack(pady=10)

        self.cart_text = tk.Text(self, height=5, width=30)
        self.cart_text.pack(pady=10)

    def add_to_cart(self, product, quantity):
        cart_item = f"Added to Cart: {int(quantity)} x {product}\n"
        self.cart_text.insert(tk.END, cart_item)
        

class LearnPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        switch_button = tk.Button(self, font=("Helvetica", 14), text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)
        label = tk.Label(self, text="Learning Page (Will have lessons for users to learn morse code.) *WIP*", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)
    print("Learn")

class PracticePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        switch_button = tk.Button(self, font=("Helvetica", 14), text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)
        label = tk.Label(self, text="Practice Page (Will have pre-made questions for users to practice their morse code.) *WIP*", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)
    print("Practice")
    
class CustomizationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        switch_button = tk.Button(self, font=("Helvetica", 14), text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)
        label = tk.Label(self, text="Customization Page (Will have display of bought items to put onto the character 'Sam'.) *WIP*", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)
    print("Customization")

if __name__ == "__main__":
    app = PageSwitcher()
    app.mainloop()

    #take photo of code