import customtkinter as ctk
from PIL import Image

import orders_backend

class OrderFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window, width=960, height=540)

        bg_image = Image.open("Documents\orders_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)

        # sub total for total order
        self.sub_total = 0
        
        # left side orders frame
        self.orders_frame()
        
        # right side payment frame
        # self.pay_frame()
        
        # mainframe config
        self.frame_config()
        
    # left order frame 
    def orders_frame(self):
        # main order frame
        order_mainframe = ctk.CTkFrame(master=self,width= 520, height=400)
        order_mainframe.grid(row=1, columnspan=2, padx=10,pady = 8, sticky="ne")
        
        # order details frame inside order mainframe
        self.odrframe = ctk.CTkScrollableFrame(master=order_mainframe, width= 520, height=335)
        self.odrframe.grid(row=1, padx=10,pady = 8, sticky="ne")

        # order category frame
        catframe = ctk.CTkFrame(master=order_mainframe, width=600, fg_color="#333333")
        catframe.grid(row = 0, sticky = "we")
        catframe.columnconfigure(0, weight=1)
        catframe.columnconfigure(1, weight=1)
        catframe.columnconfigure(2, weight=1)
        
        # order category labels
        fooditem = ctk.CTkLabel(master=catframe, height=50, text="Order Name", font=('Trip Sans Bold', 20))
        fquantity = ctk.CTkLabel(master=catframe, text="Quantity", font=('Trip Sans Bold', 20))
        fprice = ctk.CTkLabel(master=catframe, text="Price", font=('Trip Sans Bold', 20))
        # placing category label
        fooditem.grid(row = 0,column = 0)
        fquantity.grid(row = 0, column =1)
        fprice.grid(row = 0,column = 2)
        
        # order name, quantity, and price frame inside scrollable frame
        # self.ordered_items_frame()


    def ordered_items_frame(self, ordered_items):
        # food details frame inside orderframe
        self.foodordered = ctk.CTkFrame(master=self.odrframe, width=100, fg_color="#38618c")
        self.foodordered.grid(row = 0, sticky = "we")
        self.foodordered.columnconfigure(0, weight=1)
        self.foodordered.columnconfigure(1, weight=1)
        self.foodordered.columnconfigure(2, weight=1)


        food_item_list = []
        food_quantity_list = []
        food_price_list = []
        
        # ordered food details
        ordered_items_list = list(ordered_items.items())
        for i in ordered_items_list:
            name, price = orders_backend.fetch_name_price(str(i[0]))
            food_item_list.append(name)
            food_quantity_list.append(int(i[1]))
            food_price_list.append(int(price))

        print(food_item_list, food_quantity_list, food_price_list)
        # food_item_list = ["something", "nothing"]
        # food_quantity_list = [2,4]
        # food_price_list = [10,10,10]
        
        # place all ordered food list in order list frame
        sub_total = 0
        for i in range(len(food_item_list)):
            self.order(food_item_list[i], food_quantity_list[i], food_price_list[i], i)
            sub_total += food_quantity_list[i] * food_price_list[i]

        self.sub_total = sub_total
        self.pay_frame()
        
    def order(self,food_item, quantity, price, rowq):
        item = ctk.CTkLabel(master=self.foodordered, width=210, height=40, text=f"{food_item}", font=('Trip Sans Bold', 16), fg_color="#294868")
        quantity = ctk.CTkLabel(master=self.foodordered, width=165, text=f"{quantity}", font=('Trip Sans Bold', 16))
        price = ctk.CTkLabel(master=self.foodordered, width=170, text=f"${price}", font=('Trip Sans Bold', 16))
        # place them
        item.grid(row=rowq, column=0)
        quantity.grid( row=rowq, column=1)
        price.grid(row=rowq, column=2)
        
    # right side payment frame 
    def pay_frame(self):
        # payment details frame -right
        self.payframe = ctk.CTkFrame(master=self)
        self.payframe.grid(row=1, column=2, padx=10, pady = 8, sticky="nw")
        
        # fixed tax and service charge
        tax_charge = 1
        service_charge = 1
        
        # all charges frame
        chargesframe = ctk.CTkFrame(master=self.payframe)
        chargesframe.grid(row=0, sticky="new", padx=15, pady=10)
        
        # payment charges, total amount and button here
        paycharges = ctk.CTkLabel(master=chargesframe, text=f"Sub Total: ${self.sub_total}\n\nTax Charges: ${tax_charge}\n\nService Charges: ${service_charge}", font=('Trip Sans Bold', 16), height=125, pady=10, padx=10)
        total_amount = self.sub_total + tax_charge + service_charge
        payamount = ctk.CTkLabel(master=self.payframe, text=f"Total payable amount: \n${total_amount}", width=245, font=('Trip Sans Bold', 16), height=180)
        paybtn = ctk.CTkButton(master=self.payframe, text="Pay", width=120, height=60, font=('Trip Sans Bold', 20))
        
        # placing widgets in payment frame
        paycharges.grid(row=0, sticky="n")
        payamount.grid(row=1, sticky="n")
        paybtn.grid(row=2, sticky="ns", pady=14)
        
    # places food items in scrollable frame when called


    def frame_config(self):
        self.configure(width=960, height=540)
        self.grid_propagate(0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        # row and column configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)