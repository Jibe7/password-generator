""" Module containing the password generator application.

Uses customtkinter, screeninfo, string and secrets modules.


"""

import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

from screeninfo import get_monitors
import string
import secrets

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 400

class CharactersCustomization(customtkinter.CTkFrame):
    """ Represents a toggle button on the GUI that controls an option regarding the choice of the characters included in the passwords.
    
    """
    def __init__(self, master : customtkinter.CTk, text : str, characters : str, row : int, column : int, padx : tuple[int, int], pady : tuple[int, int], defaultToggle : bool = False):
        super().__init__(master)
        self.checkBox = customtkinter.CTkCheckBox(self,
            text = text,
            onvalue = True,
            offvalue = False
        )
        self.checkBox.grid(row=row, column=column, padx=padx, pady=pady)
        if defaultToggle:
            self.checkBox.toggle()
            pass
        self.characters = characters

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
        self.lowerCasesCheckBox = CharactersCustomization(self, "Use lowercases", string.ascii_lowercase, row=1, column=0, padx=(0, 40), pady=(0, 20), defaultToggle=True) 
        self.lowerCasesCheckBox.grid(row=1, column=0, padx=(0, 0), pady=(0, 20))

        self.upperCasesCheckBox = CharactersCustomization(self, 
        "Use uppercases",
        string.ascii_uppercase,
        row=2, column=0, padx=(0, 40), pady=(0,20), defaultToggle=False) 
        self.upperCasesCheckBox.grid(row=2, column=0, padx=(0, 0), pady=(0, 20))
        
        self.digitsCheckBox = CharactersCustomization(self,
        "Use numbers",
        string.digits,                                              
        row=3, column=0, padx=(0, 55), pady=(0, 20)) 
        self.digitsCheckBox.grid(row=3, column=0, padx=(0, 0), pady=(0, 20))
        
        self.punctuationCheckBox = CharactersCustomization(self,
        "Use special characters",
        string.punctuation,
        row=4, column=0, padx=(0, 0), pady=(0, 20)) 
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


    def basicPassGen(self, size : int = 15) -> None:
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
        size = abs(size)

        alphabet = ""
        if self.lowerCasesCheckBox.checkBox.get():
            alphabet += string.ascii_lowercase
        if self.upperCasesCheckBox.checkBox.get():
            alphabet += string.ascii_uppercase
        if self.digitsCheckBox.checkBox.get():
            alphabet += string.digits
        if self.punctuationCheckBox.checkBox.get():
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

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()