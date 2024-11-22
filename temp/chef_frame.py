import customtkinter as ctk
import tkinter 
from PIL import Image
from datetime import date
        
class ChefFrame(ctk.CTkFrame):
    def __init__(self,window):
        super().__init__(window, width=960, height=540)
        # self.grid_propagate(0)
        
        # font config
        self.ffont = ('Trip Sans Bold', 40)
        self.ffont1 = ('Trip Sans Medium', 24)
        self.ffont2 = ('Trip Sans Medium', 22)
        self.ffont3 = ('Trip Sans Medium', 16)
        self.status_frame_config()

        #call create_widgets from backend to send order status
        self.create_widgets()

    def create_widgets(self):
        # pending order frame
        self.chef_frame = ctk.CTkFrame(master=self, width=580, height=383, fg_color="#EEC0AA",  corner_radius=0)
        self.chef_frame.place(x = 81, y = 98)
        # pending order label
        title_label = ctk.CTkLabel(master=self.chef_frame, text="PENDING ORDERS", width=280, height=30, font=self.ffont1, text_color="black")
        title_label.place(x = 150, y = 16)
        
        # left side pending orders frame
        self.place_new_orders()
        # prepared orders frame
        self.prepared_orders_frame()
        
        
    def place_new_orders(self):
        # scrollable frame for pending orders
        self.scrollable_orders_frame = ctk.CTkScrollableFrame(master=self.chef_frame, width=560, height=323, fg_color="#EEC0AA",  corner_radius=0)
        self.scrollable_orders_frame.place(x = 0, y =60)
        # item details
        ord_no = [12, 43, 24, 54, 56]
        table_no = [4, 43 , 67, 23, 12]
        ord_item = ["Chicken Sandwich", "Coca Cola", "Drinks", "Burger", "Pasta"]
        item_q = [2, 5, 6, 7, 2]
        rowy = 0
        for i in range (len(ord_no)):
            self.pending_orders(ord_no[i], table_no[i], ord_item[i], item_q[i], rowy)
            rowy += 94
    
    def checked_box(self):
        ord_no = 23
        print(f"pressed order no: {ord_no}")
        
        
    def pending_orders(self, ord_no, table_no, ord_item, item_q, rowy):
        # order details frame
        order_checkbox = ctk.CTkCheckBox(master=self.scrollable_orders_frame, command= self.checked_box, text="")
        order_checkbox.configure(bg_color="#FFF1E2", checkbox_width = 52, checkbox_height = 46, width = 495, height = 73, border_width = 4, hover= False)
        # order_checkbox.place(x = 33, y = rowy + 31)
        order_checkbox.pack()
        
        order_number = ctk.CTkLabel(master=order_checkbox, text=f"ORDER NO: {ord_no}", width=109, height=25, bg_color="#FFF1E2", text_color="black", font=self.ffont3)
        order_number.place(x = 83, y = rowy + 14)
        # order_number.pack()
        
        ordered_item = ctk.CTkLabel(master=order_checkbox, text=f"{ord_item}", width=190, height=19, bg_color="#FFF1E2", text_color="black", font=self.ffont3)
        ordered_item.place(x = 66, y = rowy + 41)
        # ordered_item.pack()
        
        table_number = ctk.CTkLabel(master=order_checkbox, text=f"TABLE NO: {table_no}", width=109, height=24, bg_color="#FFF1E2", text_color="black", font=self.ffont3)
        table_number.place(x = 336, y = rowy + 14)
        # table_number.pack()
        
        item_quantity = ctk.CTkLabel(master=order_checkbox, text=f"Quantity: {item_q}", width=115, height=19, bg_color="#FFF1E2", text_color="black", font=self.ffont3)
        item_quantity.place(x = 331, y = rowy + 41)
        # item_quantity.pack()
        
        
    def prepared_orders_frame(self):
        # completed orders frame
        completed_orders_frame = ctk.CTkFrame(master=self, height=383, width=181, fg_color="#EEC0AA",  corner_radius=0)
        completed_orders_frame.place(x = 700, y= 98)
        
        title_label = ctk.CTkLabel(master=completed_orders_frame,text="COMPLETED \nORDERS", width=121, height=54,font=self.ffont1, text_color="black")
        title_label.place(x = 23, y = 13)
        
        # item frame
        item_frame = ctk.CTkFrame(master=completed_orders_frame, width=146, height=65, fg_color="#FFF1E2")
        item_frame.place(x = 17, y = 82)
        
        
    # main frame configure
    def status_frame_config(self):
        # self.configure(width= 960, height = 540)
        bg_image = Image.open("pics/chef_bg.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

class Window(ctk.CTk):
    def __init__(self, title):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        super().__init__()
        self.geometry("960x540")
        self.title(title)
        self.resizable(False,False)
        ChefFrame(self)
        self.mainloop()

Window("Chef Status")