import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Telefonbuch(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Telefonbuch")
        self.geometry("410x615")
        self.resizable(False, False)  

        self.bg_image = ctk.CTkImage(
            light_image=Image.open("london.jpg"),
            dark_image=Image.open("london.jpg"),
            size=(410, 615)
        )

        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relwidth=1, relheight=1)


        self.entry_name = ctk.CTkEntry(self.bg_label, placeholder_text="Name")
        self.entry_name.place(relx=0.0, rely=0.4, anchor="w")

        self.entry_number = ctk.CTkEntry(self, placeholder_text="Telefonnummer")
        self.entry_number.place(relx=0.0, rely=0.45, anchor="w")

        # Button zum Hinzufügen
        self.button_add = ctk.CTkButton(self, text="Hinzufügen")
        self.button_add.place(relx=0.0, rely=0.5, anchor="w")
