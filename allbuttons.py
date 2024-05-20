import tkinter as tk
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

#pip3 install customtkinter
#pip3 install customtkinter --upgrade
#pip install packaging
#pip install Pillow

#type these in terminal to install everything needed

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="light blue")

        self.button_frame_map = {
            "ShopPage": "ShopPage",
            "CustomizationPage": "CustomizationPage",
            "PracticePage": "PracticePage",
            "LearnPage": "LearnPage",
            "TranslatorPage": "TranslatorPage"
        }

        home_label = tk.Label(self, text="Welcome to Keylingo", font=("Comic Sans MS", 36), bg="light blue", fg="teal")
        home_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        home_label = tk.Label(self, text="Shop", font=("Comic Sans MS", 36), bg="teal", fg="white")
        home_label.place(relx=0.35, rely=0.40, anchor=tk.CENTER)

        home_label = tk.Label(self, text="Customize Sam", font=("Comic Sans MS", 36), bg="teal", fg="white")
        home_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        home_label = tk.Label(self, text="Practice", font=("Comic Sans MS", 36), bg="teal", fg="white")
        home_label.place(relx=0.65, rely=0.40, anchor=tk.CENTER)

        home_label = tk.Label(self, text="Learn", font=("Comic Sans MS", 36), bg="teal", fg="white")
        home_label.place(relx=0.15, rely=0.80, anchor=tk.CENTER)

        home_label = tk.Label(self, text="Translate", font=("Comic Sans MS", 36), bg="teal", fg="white")
        home_label.place(relx=0.85, rely=0.80, anchor=tk.CENTER)


        button_zones = {
    "ShopPage": {"zone": (50, 50, 200, 150), "image_path": "bigfatprojectgui/shop.png"},
    "CustomizationPage": {"zone": (500, 100, 650, 200), "image_path": "bigfatprojectgui/Sam.png"},
    "PracticePage": {"zone": (900, 300, 1050, 400), "image_path": "bigfatprojectgui/practice.png"},
    "LearnPage": {"zone": (200, 400, 350, 500), "image_path": "bigfatprojectgui/learn.png"},
    "TranslatorPage": {"zone": (700, 500, 850, 600), "image_path": "bigfatprojectgui/translate.png"}
}
        self.images = {}
        for button, data in button_zones.items():
            image = tk.PhotoImage(file=data["image_path"])
            self.images[button] = image

        shop_button = tk.Label(self, image=self.images["ShopPage"], bg="light blue")
        shop_button.image = self.images["ShopPage"]  
        shop_button.place(relx=0.35, rely=0.265, anchor=tk.CENTER) 
        shop_button.bind("<Button-1>", lambda event: self.handle_click(event, "ShopPage"))

        custom_button = tk.Label(self, image=self.images["CustomizationPage"], bg="light blue")
        custom_button.image = self.images["CustomizationPage"]
        custom_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)  
        custom_button.bind("<Button-1>", lambda event: self.handle_click(event, "CustomizationPage"))

        practice_button = tk.Label(self, image=self.images["PracticePage"], bg="light blue")
        practice_button.image = self.images["PracticePage"]
        practice_button.place(relx=0.65, rely=0.25, anchor=tk.CENTER)  
        practice_button.bind("<Button-1>", lambda event: self.handle_click(event, "PracticePage"))

        learn_button = tk.Label(self, image=self.images["LearnPage"], bg="light blue")
        learn_button.image = self.images["LearnPage"]
        learn_button.place(relx=0.15, rely=0.65, anchor=tk.CENTER)  
        learn_button.bind("<Button-1>", lambda event: self.handle_click(event, "LearnPage"))

        translator_button = tk.Label(self, image=self.images["TranslatorPage"], bg="light blue")
        translator_button.image = self.images["TranslatorPage"]
        translator_button.place(relx=0.85, rely=0.68, anchor=tk.CENTER)  
        translator_button.bind("<Button-1>", lambda event: self.handle_click(event, "TranslatorPage"))           
    def handle_click(self, event, button_name):
        print(f"{button_name} was clicked")
        frame_name = self.button_frame_map.get(button_name)
        if frame_name:
            self.controller.show_frame(frame_name)

class PracticePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        switch_button = tk.Button(self, font=("Helvetica", 14), text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)

        self.controller = controller
        self.questions = [
            ("What is 'a' in Morse Code?", ".-"),
            ("What is 'b' in Morse Code?", "-..."),
            ("What is 'c' in Morse Code?", "-.-."),
            ("What is 'd' in Morse Code?", "-.."),
            ("What is 'e' in Morse Code?", "."),
            ("What is 'f' in Morse Code?", "..-."),
            ("What is 'g' in Morse Code?", "--."),
            ("What is 'h' in Morse Code?", "...."),
            ("What is 'i' in Morse Code?", ".."),
            ("What is 'j' in Morse Code?", ".---"),
            ("What is 'k' in Morse Code?", "-.-"),
            ("What is 'l' in Morse Code?", ".-.."),
            ("What is 'm' in Morse Code?", "--"),
            ("What is 'n' in Morse Code?", "-."),
            ("What is 'o' in Morse Code?", "---"),
            ("What is 'p' in Morse Code?", ".--."),
            ("What is 'q' in Morse Code?", "--.-"),
            ("What is 'r' in Morse Code?", ".-."),
            ("What is 's' in Morse Code?", "..."),
            ("What is 't' in Morse Code?", "-"),
            ("What is 'u' in Morse Code?", "..-"),
            ("What is 'v' in Morse Code?", "...-"),
            ("What is 'w' in Morse Code?", ".--"),
            ("What is 'x' in Morse Code?", "-..-"),
            ("What is 'y' in Morse Code?", "-.--"),
            ("What is 'z' in Morse Code?", "--.."),
            ("Translate 'how' to Morse Code?", ".... --- .--"),
            ("Translate 'the' to Morse Code?", "- .... ."),
            ("Translate 'who' to Morse Code?", ".-- .... ---"),
            ("Translate 'one' to Morse Code?", "--- -. ."),
            ("Translate 'two' to Morse Code?", "- .-- ---"),
            ("Translate 'three' to Morse Code?", "- .... .-. . ."),
            ("Translate 'four' to Morse Code?", "..-. --- ..- .-."),
            ("Translate 'five' to Morse Code?", "..-. .. ...- ."),
            ("Translate 'six' to Morse Code?", "... .. -..-"),
            ("Translate 'seven' to Morse Code?", "... . ...- . -."),
            ("Translate 'eight' to Morse Code?", ". .. --. .... -"),
            ("Translate 'nine' to Morse Code?", "-. .. -. ."),
            ("Translate 'ten' to Morse Code?", "- . -."),
            ("Translate 'eleven' to Morse Code?", ". .-.. . ...- . -."),
            ("Translate 'one and two' to Morse Code?", "--- -. . / .- -. -.. / - .-- ---"),
            ("Translate '-.-. .... .- .-.. .-.. . -. --. .' to English?", "-.-. .... .- .-.. .-.. . -. --. ."),
            ("Translate '-.-- --- ..- / .- .-. . / --. .- -.--' to English?", "-.-- --- ..- / .- .-. . / --. .- -.--"),
            ("Translate '.. ... / -.-- --- ..- .-. / .-- .- -.-- ...' to English?", ".. ... / -.-- --- ..- .-. / .-- .- -.-- ..."),
            ("Translate '-... . -.-. .- ..- ... . / ..-. ..- -.' to English?", "-... . -.-. .- ..- ... . / ..-. ..- -."),
            ("Translate '-- -.-- / -... . .-.. ..- .' to English?", "-- -.-- / -... . .-.. ..- ."),
            ("Translate '.... .. ... / .-- . .-. . / .. ... / - --- -.-. -.-' to English?", ".... .. ... / .-- . .-. . / .. ... / - --- -.-. -.-"),
            ("Translate '-.-- --- ..- .-. . .--. .-.. -.-- ..--..' to English?", "-.-- --- ..- .-. . .--. .-.. -.-- ..--.."),
        ]
        self.current_question_index = 0
        self.attempts = 0

        self.question_label = tk.Label(self, text="", font=("Helvetica", 24))
        self.question_label.pack(pady=10)

        self.answer_label = tk.Label(self, font=("Helvetica", 24), text="Your Answer:")
        self.answer_label.pack(pady=10)

        self.answer_entry = tk.Entry(self, width=30)
        self.answer_entry.pack(pady=10)

        self.result_label = tk.Label(self, font=("Helvetica", 24), text="")
        self.result_label.pack(pady=10)

        check_answer_button = tk.Button(self, font=("Helvetica", 24), text="Check Answer", command=lambda: self.check_answer())
        check_answer_button.pack(pady=5)

        reveal_answer_button = tk.Button(self, font=("Helvetica", 24), text="Reveal Answer", command=lambda: self.reveal_answer())
        reveal_answer_button.pack(pady=5)

        self.next_question_button = tk.Button(self, font=("Helvetica", 24), text="Next Question", command=lambda: self.next_question())
        self.next_question_button.pack(pady=5)

        self.load_question_gui()

    def go_to_home(self):
        self.controller.show_frame("HomePage")

    def load_question_gui(self):
        self.result_label.config(text="")
        if self.current_question_index < len(self.questions):
            question_text, _ = self.questions[self.current_question_index]
            self.question_label.config(text=question_text)
        else:
            self.question_label.config(text="No more questions!")

    def check_answer(self):
        if self.current_question_index < len(self.questions):
            _, correct_answer = self.questions[self.current_question_index]
            user_answer = self.answer_entry.get().strip()
            self.attempts += 1

            if user_answer == correct_answer:
                self.result_label.config(text="Correct!")
            else:
                self.result_label.config(text=f"Wrong! Attempts: {self.attempts}")

    def reveal_answer(self):
        if self.current_question_index < len(self.questions):
            _, correct_answer = self.questions[self.current_question_index]
            self.result_label.config(text=f"The correct answer is: {correct_answer}")
            self.next_question_button.pack(pady=5)  

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.attempts = 0
            self.load_question_gui()  
            self.result_label.config(text="")  
            self.next_question_button.pack_forget()
        else:
            self.question_label.config(text="No more questions!")
    print("Practice")

class CustomizationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        character_canvas = tk.Canvas(self, width=400, height=600, bg="gray")
        character_canvas.pack(side="left", padx=20, pady=20)

        options_frame = tk.Frame(self)
        options_frame.pack(side="left", padx=20, pady=20)

        tab_control = customtkinter.CTkTabview(options_frame)
        tab_control.pack(pady=20)

        costume_tab = tab_control.add("Costume")
        costume_options_frame = tk.Frame(costume_tab)
        costume_options_frame.pack(padx=20, pady=20)

        body_tab = tab_control.add("Body")
        body_options_frame = tk.Frame(body_tab)
        body_options_frame.pack(padx=20, pady=20)

        emote_tab = tab_control.add("Emotes")
        emote_options_frame = tk.Frame(emote_tab)
        emote_options_frame.pack(padx=20, pady=20)

        switch_button = tk.Button(self, text="Go to Home", command=lambda: controller.show_frame("HomePage"), width=20, height=2)
        switch_button.pack(pady=10)



class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="teal")

        label = tk.Label(self, text="Clothing Shop", font=("Comic Sans MS", 36), bg="teal")
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        manlabel = tk.Label(self, text="Samantha - 50 Coins", font=("Helvetica", 24), bg="teal")
        manlabel.place(relx=0.30, rely=.80, anchor=tk.CENTER)

        manlabelReal = tk.Label(self, text="Old Sam - 50 Coins", font=("Helvetica", 24), bg="teal")
        manlabelReal.place(relx=0.70, rely=.80, anchor=tk.CENTER)

        items = [
            {"name": "Item 1", "image_path": "/Users/yoted/Library/CloudStorage/GoogleDrive-sngu0400@students.kleinisd.net/My Drive/Code/bigfatprojectgui/girl outfit.png", "position": (300, 200)},
            {"name": "Item 2", "image_path": "/Users/yoted/Library/CloudStorage/GoogleDrive-sngu0400@students.kleinisd.net/My Drive/Code/bigfatprojectgui/otheroutfit.png", "position": (800, 200)}
        ]

        for item in items:
            item_image = Image.open(item["image_path"])
            item_photo = ImageTk.PhotoImage(item_image)

            item_label = tk.Label(self, image=item_photo, bg="teal")
            item_label.image = item_photo  

            x, y = item["position"]
            item_label.place(x=x, y=y)

        home_button = tk.Button(self, text="Go to Home", font=("Helvetica", 18), command=lambda: controller.show_frame("HomePage"))
        home_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        coins_label = tk.Label(self, text="Coins: 100", font=("Helvetica", 18), bg="teal")
        coins_label.place(relx=1, rely=0, anchor=tk.NE, x=-10, y=10)

    def item_clicked(self, item_name):
        print(f"You clicked {item_name}")

class LearnPage(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.questions = [
            ("\"a\" in Morse code is '.-', Type the letter \"a\" in Morse code", ".-"),
            ("\"b\" in Morse code is '-...', Type the letter \"b\" in Morse code", "-..."),
            ("\"c\" in Morse code is '-.-.', Type the letter \"c\" in Morse code", "-.-."),
            ("\"d\" in Morse code is '-..', Type the letter \"d\" in Morse code", "-.."),
            ("\"e\" in Morse code is '.', Type the letter \"e\" in Morse code", "."),
            ("\"f\" in Morse code is '..-.', Type the letter \"f\" in Morse code", "..-."),
            ("\"g\" in Morse code is '--.', Type the letter \"g\" in Morse code", "--."),
            ("\"h\" in Morse code is '....', Type the letter \"h\" in Morse code", "...."),
            ("\"i\" in Morse code is '..', Type the letter \"i\" in Morse code", ".."),
            ("\"j\" in Morse code is '.---', Type the letter \"j\" in Morse code", ".---"),
            ("\"k\" in Morse code is '-.-', Type the letter \"k\" in Morse code", "-.-"), 
            ("\"l\" in Morse code is '.-..', Type the letter \"k\" in Morse code", ".-.."),
            ("\"m\" in Morse code is '--', Type the letter \"m\" in Morse code", "--"),
            ("\"n\" in Morse code is '-.', Type the letter \"n\" in Morse code", "-."),
            ("\"o\" in Morse code is '---', Type the letter \"o\" in Morse code", "---"),
            ("\"p\" in Morse code is '.--.', Type the letter \"p\" in Morse code", ".--."),
            ("\"q\" in Morse code is '--.-', Type the letter \"q\" in Morse code", "--.-"),
            ("\"r\" in Morse code is '.-.', Type the letter \"r\" in Morse code", ".-."),
            ("\"s\" in Morse code is '...', Type the letter \"s\" in Morse code", "..."),
            ("\"t\" in Morse code is '-', Type the letter \"t\" in Morse code", "-"),
            ("\"u\" in Morse code is '..-', Type the letter \"u\" in Morse code", "..-"),
            ("\"v\" in Morse code is '...-', Type the letter \"v\" in Morse code", "...-"),
            ("\"w\" in Morse code is '.--', Type the letter \"w\" in Morse code", ".--"),
            ("\"x\" in Morse code is '-..-', Type the letter \"x\" in Morse code", "-..-"),
            ("\"y\" in Morse code is '-.--', Type the letter \"y\" in Morse code", "-.--"),
            ("\"z\" in Morse code is '--..', Type the letter \"z\" in Morse code", "--..")
            ]
            self.current_question_index = 0
            self.attempts = 0

            switch_button = tk.Button(self, font=("Helvetica", 14), text="Go to Home", command=lambda: self.go_to_home(), width=20, height=2)
            switch_button.pack(pady=10)

            self.question_label = tk.Label(self, text="", font=("Helvetica", 24))
            self.question_label.pack(pady=10)

            self.answer_label = tk.Label(self, font=("Helvetica", 24), text="Your Answer:")
            self.answer_label.pack(pady=10)

            self.answer_entry = tk.Entry(self, width=30)
            self.answer_entry.pack(pady=10)

            self.result_label = tk.Label(self, font=("Helvetica", 24), text="")
            self.result_label.pack(pady=10)

            check_answer_button = tk.Button(self, font=("Helvetica", 24), text="Check Answer", command=lambda: self.check_answer())
            check_answer_button.pack(pady=5)

            reveal_answer_button = tk.Button(self, font=("Helvetica", 24), text="Reveal Answer", command=lambda: self.reveal_answer())
            reveal_answer_button.pack(pady=5)

            self.next_question_button = tk.Button(self, font=("Helvetica", 24), text="Next Question", command=lambda: self.next_question())
            self.next_question_button.pack(pady=5)

            self.load_question_gui()

    def go_to_home(self):
        self.controller.show_frame("HomePage")

    def go_to_home(self):
        self.controller.show_frame("HomePage")

    def load_question_gui(self):
        self.result_label.config(text="")
        if self.current_question_index < len(self.questions):
            question_text, _ = self.questions[self.current_question_index]
            self.question_label.config(text=question_text)
        else:
            self.question_label.config(text="No more questions!")

    def check_answer(self):
        if self.current_question_index < len(self.questions):
            _, correct_answer = self.questions[self.current_question_index]
            user_answer = self.answer_entry.get().strip()
            self.attempts += 1

            if user_answer == correct_answer:
                self.result_label.config(text="Correct!")
            else:
                self.result_label.config(text=f"Wrong! Attempts: {self.attempts}")

    def reveal_answer(self):
        if self.current_question_index < len(self.questions):
            _, correct_answer = self.questions[self.current_question_index]
            self.result_label.config(text=f"The correct answer is: {correct_answer}")
            self.next_question_button.pack(pady=5)  

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.attempts = 0
            self.load_question_gui()  
            self.result_label.config(text="")  
            self.next_question_button.pack_forget()
        else:
            self.question_label.config(text="No more questions!")

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

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("My App")
        self.geometry("2400x1600")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, ShopPage, CustomizationPage, PracticePage, LearnPage, TranslatorPage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

