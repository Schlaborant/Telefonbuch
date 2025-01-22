import customtkinter as ctk
from PIL import Image, ImageTk

#ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Phone_book(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Phone book")
        self.geometry("410x615")
        self.resizable(False, False)  

        self.bg_image = ctk.CTkImage(light_image=Image.open("images/london.jpg"),
                                     dark_image=Image.open("images/london.jpg"),
                                     size=(410, 615)
        )
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relwidth=1, relheight=1)

        self.add_image=Image.open("images/add_button.png")
        self.add_image=ctk.CTkImage(light_image=self.add_image,
                                    dark_image=self.add_image,
                                    size=(50, 50))
        self.add_button = ctk.CTkButton(self, image=self.add_image, text="", 
                                        command=self.add_contact,
                                        width=50, height=50,
                                        fg_color="white", hover_color="white",
                                        corner_radius=0)
        self.add_button.place(relx=0.1, rely=0.4, anchor="w")


        self.edit_image = Image.open("images/edit_button.png")
        self.edit_image = ctk.CTkImage(light_image=self.edit_image,
                                       dark_image=self.edit_image,
                                       size=(50, 50))
        self.edit_button = ctk.CTkButton(self, image=self.edit_image, text="",
                                         command=self.edit_contact,
                                         width=50, height=50,
                                         fg_color="white", hover_color="white",
                                         corner_radius=0)
        self.edit_button.place(relx=0.1, rely=0.6, anchor="w")


        self.search_image = Image.open("images/search_button.png")
        self.search_image = ctk.CTkImage(light_image=self.search_image,
                                         dark_image=self.search_image,
                                         size=(50, 50))
        self.search_button = ctk.CTkButton(self, image=self.search_image, text="",
                                           command=self.search_contact,
                                           width=50, height=50,
                                           fg_color="white", hover_color="white",
                                           corner_radius=0)
        self.search_button.place(relx=0.9, rely=0.4, anchor="e")


        self.delete_image = Image.open("images/delete_button.png")
        self.delete_image = ctk.CTkImage(light_image=self.delete_image,
                                         dark_image=self.delete_image,
                                         size=(50, 50))
        self.delete_button = ctk.CTkButton(self, image=self.delete_image, text="",
                           command=self.delete_contact,
                           width=50, height=50,
                           fg_color="white", hover_color="white",
                           corner_radius=0)
        self.delete_button.place(relx=0.9, rely=0.6, anchor="e")

    def add_contact(self):
        pass

    def edit_contact(self):
        pass

    def search_contact(self):
        pass
    
    def delete_contact(self):
        pass