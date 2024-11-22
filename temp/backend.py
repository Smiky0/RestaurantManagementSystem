import customtkinter as ctk

import login, login_backend
import menu
import orders
import order_status
# import orders, orders_backend

class Window(ctk.CTk):
    def __init__(self, title):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        super().__init__()
        self.geometry("960x540")
        self.title(title)
        self.resizable(False,False)
        # self.wm_attributes("-transparentcolor", "grey")

        self.wholeloginframe = login.Login_Frame(self)
        
        # self.loginframe = login.Loginframe(self)
        self.wholeloginframe.loginframe.login_button.bind("<Button-1>", self.go_to_menu)
        self.wholeloginframe.place_forget()

        self.menuframe = menu.Menuframe(self)
        self.menuframe.order_button.bind("<Button-1>", self.go_to_orders)
        self.menuframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        # self.menuframe.place_forget()

        self.orderframe = orders.OrderFrame(self)
        self.orderframe.place_forget()
        self.mainloop()

    def go_to_menu(self, event):
        username = self.wholeloginframe.loginframe.username_entry.get() #00B2FF
        password = self.wholeloginframe.loginframe.password_entry.get()
        status = login_backend.openMenu(username, password)
        if status == 0:
            self.wholeloginframe.loginframe.login_status_text.configure(text="Wrong username", text_color="red")
            self.wholeloginframe.loginframe.login_status_text.place(x = 244, y = 204)
        elif status == -1:
            self.wholeloginframe.loginframe.login_status_text.configure(text="Wrong password", text_color="red")
            self.wholeloginframe.loginframe.login_status_text.place(x = 248, y = 295)
        else:
            # login_window.withdraw()
            # self.wholeloginframe.loginframe.login_status_text.configure(text="Done", text_color="white")
            self.place_frame_menu_login()
            

    def go_to_orders(self, event):
        item_objects_stored = self.menuframe.menu_scrollable_frame.item_objects_stored
        items_quantity = [int(item_objects_stored[i].get()) for i in range(len(item_objects_stored))]
        item_menu_ids = self.menuframe.menu_scrollable_frame.items_data[0]
        items_quantity = dict(zip(item_menu_ids, items_quantity))
        self.ordered_items = {key:value for key, value in items_quantity.items() if value!=0}
        # print(self.ordered_items)
        if self.ordered_items:
            self.place_frame_order_menu()
        else:
            print("No items")

    def go_to_order_status(self):
        pass
        
    def place_frame_menu_login(self):
        self.wholeloginframe.place_forget()
        self.menuframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def place_frame_order_menu(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.menuframe.place_forget()
        self.orderframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.orderframe.ordered_items_frame(self.ordered_items)

Window("Restaurant Management System")