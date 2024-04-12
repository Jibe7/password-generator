import customtkinter

import string
import secrets

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 10), weight=0)

        self.button = customtkinter.CTkButton(self, text="Generate Password", command=lambda: self.basicPassGen(self.entry.get()))
        self.button.grid(row=1, column=0, padx=0, pady=0)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Length of the password")
        self.entry.grid(row=0, column=0, padx=0, pady=30)
    
        self.password = ""

    def basicPassGen(self, size : int = 15 ) -> None:
        if (type(size)==type("s")):
            try:
                size = int(size)
            except:
                size = 15

        alphabet = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(secrets.choice(alphabet) for i in range(size))
        
        self.label = customtkinter.CTkTextbox(self, state="normal", fg_color="white", text_color="red", width=200, height=60)
        self.label.grid(row=2, column=0, padx=0, pady=60)
        self.label.insert("0.0", self.password)
        self.label.configure(state="disabled")



app = App()
app.mainloop()