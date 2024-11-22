import customtkinter as ctk
from PIL import Image
from datetime import date
        
class OrderStatusFrame(ctk.CTkFrame):
    def __init__(self,window):
        super().__init__(window, width=960, height=540)
        self.grid_propagate(0)
        
        # font config
        self.ffont = ('Trip Sans Bold', 40)
        self.ffont1 = ('Trip Sans Medium', 20)
        self.ffont2 = ('Trip Sans Medium', 16)
        self.status_frame_config()

        #call create_widgets from backend with the order number
        self.create_widgets()

    def create_widgets(self):
        self.order_number_text = f"ORDER NUMBER: OD25231"
        self.table_number_text = f"TABLE NUMBER: 1"
        date_today = date.today()
        date_today = date_today.strftime("%d/%m/%Y")
        
        ctk.CTkLabel(self, text=self.order_number_text, font=('Trip Sans Medium', 24), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 82, y = 111)
        ctk.CTkLabel(self, text=self.table_number_text, font=('Trip Sans Medium', 24), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 400, y = 111)
        ctk.CTkLabel(self, text=f"DATE: {date_today}", font=('Trip Sans Medium', 24), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 697, y = 111)
    
    # main frame configure
    def status_frame_config(self):
        # self.configure(width= 960, height = 540)
        bg_image = Image.open("Documents/order_status_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

