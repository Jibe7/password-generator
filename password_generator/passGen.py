import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

from screeninfo import get_monitors
import string
import secrets

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 400

class PasswordGenerator(customtkinter.CTk):
    """ Class that creates a Python GUI interface using customtkinter. Allow to create passwords with customization on its size and characters. 
    
    """
    def __init__(self):
        super().__init__()
        self.title("Password Generator")


        # Window Sizing
        wind_width = DEFAULT_WIDTH
        wind_height = DEFAULT_HEIGHT
        for m in get_monitors():
            if m.is_primary:
                wind_width = m.width
                wind_height = m.height
        geometry_size = str(wind_width // 2) + 'x' + str(wind_height // 2)
        self.geometry(geometry_size)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 10), weight=0)


        # Password Characters Customization
        self.lowercasesCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use lowercases",
            onvalue = True,
            offvalue = False
        )
        self.lowercasesCheckBox.toggle()
        self.lowercasesCheckBox.grid(row=1, column=0, padx=(0, 40), pady=(0, 20))
        
        self.uppercasesCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use uppercases",
            onvalue = True,
            offvalue = False
        )
        self.uppercasesCheckBox.grid(row=2, column=0, padx=(0, 40), pady=(0, 20))
        
        self.digitsCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use numbers",
            onvalue = True,
            offvalue = False
        )
        self.digitsCheckBox.grid(row=3, column=0, padx=(0, 55), pady=(0, 20))
        
        self.punctuationCheckBox = customtkinter.CTkCheckBox(self,
            text = "Use special characters",
            onvalue = True,
            offvalue = False
        )
        self.punctuationCheckBox.grid(row=4, column=0, padx=(0, 0), pady=(0, 20))

        # Generate Password Button
        self.button = customtkinter.CTkButton(self, 
            text="Generate Password", 
            command=lambda: self.basicPassGen(self.entry.get()),
        )

        self.button.grid(row=5, column=0, padx=0, pady=0)

        # Password Sizing  
        self.entry = customtkinter.CTkEntry(self, 
            placeholder_text="Length of the password",
            width = 150,
        )
        self.entry.grid(row=0, column=0, padx=0, pady=30)
    

        self.password = ""


    def basicPassGen(self, size : int = 15 ) -> None:
        """ This function generates a password and displays it on a CTkTextbox.

        Parameter
        -------------
        size
            The desired size of the password. Defaults to 15.
        """
        if (type(size)==type("s")):
            try:
                size = int(size)
            except:
                size = 15

        alphabet = ""
        if self.lowercasesCheckBox.get():
            alphabet += string.ascii_lowercase
        if self.uppercasesCheckBox.get():
            alphabet += string.ascii_uppercase
        if self.digitsCheckBox.get():
            alphabet += string.digits
        if self.punctuationCheckBox.get():
            alphabet += string.punctuation
        
        if alphabet == "":
            self.password = "Please choose at least one type of characters for the password."
        else:
            self.password = ''.join(secrets.choice(alphabet) for i in range(size))
        
        self.label = customtkinter.CTkTextbox(self, 
            state="normal",
            fg_color="white",
            text_color="blue",
            width=300,
            height=80
        )
        self.label.grid(row=6, column=0, padx=0, pady=60)
        self.label.insert("0.0", self.password)
        # self.label.configure(state="disabled") # enable or disable the right of the user to modify the generated password

app = PasswordGenerator()
app.mainloop()