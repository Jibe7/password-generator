import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue') # blue, dark-blue, green, 

from screeninfo import get_monitors
import string
import secrets

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 400

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")

        width = DEFAULT_WIDTH
        height = DEFAULT_HEIGHT
        for m in get_monitors():
            if m.is_primary:
                width = m.width
                height = m.height
        geometry_size = str(width // 2) + 'x' + str(height // 2)
        self.geometry(geometry_size)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 10), weight=0)

        self.lowercasesCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use lowercases"
        )
        self.lowercasesCheckBox.grid(row=1, column=0, padx=(0, 40), pady=(0, 20))
        
        self.uppercasesCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use uppercases"
        )
        self.uppercasesCheckBox.grid(row=2, column=0, padx=(0, 40), pady=(0, 20))
        
        self.digitsCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use numbers"
        )
        self.digitsCheckBox.grid(row=3, column=0, padx=(0, 55), pady=(0, 20))
        
        self.punctuationCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use special characters"
        )
        self.punctuationCheckBox.grid(row=4, column=0, padx=(0, 0), pady=(0, 20))


        self.button = customtkinter.CTkButton(self, 
            text="Generate Password", 
            command=lambda: self.basicPassGen(self.entry.get())
        )
        self.button.grid(row=5, column=0, padx=0, pady=0)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Length of the password")
        self.entry.grid(row=0, column=0, padx=0, pady=30)
    
        self.password = ""


        self.useLowerCases = True
        self.useUpperCases = True
        self.useDigits = True
        self.usePunctuation = True

    def checkBoxUpdate(self) -> None:
        pass

    def basicPassGen(self, size : int = 15 ) -> None:
        if (type(size)==type("s")):
            try:
                size = int(size)
            except:
                size = 15

        alphabet = ""
        if self.useLowerCases:
            alphabet += string.ascii_lowercase
        if self.useUpperCases:
            alphabet += string.ascii_uppercase
        if self.useDigits:
            alphabet += string.digits
        if self.usePunctuation:
            alphabet += string.punctuation
        
        self.password = ''.join(secrets.choice(alphabet) for i in range(size))
        
        self.label = customtkinter.CTkTextbox(self, state="normal", fg_color="white", text_color="red", width=200, height=60)
        self.label.grid(row=6, column=0, padx=0, pady=60)
        self.label.insert("0.0", self.password)
        # self.label.configure(state="disabled") # enable or disable the right of the user to modify the generated password

app = App()
app.mainloop()