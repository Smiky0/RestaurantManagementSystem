import customtkinter as ctk
from pyglet import font

class Orders(ctk.CTk):
    def __init__(self,title):
        super().__init__()
        # window specifics
        self.geometry("960x540")
        self.title(title)
        self.resizable(False, False)

        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', False)

        # mainframe in window
        self.mainframe = MainFrame(self)

        # start window 
        self.mainloop()

class MainFrame(ctk.CTkFrame):
    def __init__(self,window):
        super().__init__(window)

        # font config
        self.ffont = ('Trip Sans Bold', 40)
        self.ffont1 = ('Trip Sans Medium', 20)
        self.ffont2 = ('Trip Sans Medium', 16)
        
        # sub total for total order
        self.sub_total = 0
        
        # calling all widgets
        self.widgets()
        # mainframe config
        self.frame_config()

    # all frames inside mainframe and their widgets
    def widgets(self):
        # order title label
        title = ctk.CTkLabel(master=self, text="ORDER", font=self.ffont)
        title.grid(row=0, columnspan = 3, pady=8)

        # left side orders frame
        self.orders_frame()
        # right side payment frame
        self.pay_frame()

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
        fooditem = ctk.CTkLabel(master=catframe, height=50, text="Order Name", font=self.ffont1)
        fquantity = ctk.CTkLabel(master=catframe, text="Quantity", font=self.ffont1)
        fprice = ctk.CTkLabel(master=catframe, text="Price", font=self.ffont1)
        # placing category label
        fooditem.grid(row = 0,column = 0)
        fquantity.grid(row = 0, column =1)
        fprice.grid(row = 0,column = 2)
        
        # order name, quantity, and price frame inside scrollable frame
        self.ordered_items_frame()


    def ordered_items_frame(self):
        # food details frame inside orderframe
        self.foodordered = ctk.CTkFrame(master=self.odrframe, width=100, fg_color="#38618c")
        self.foodordered.grid(row = 0, sticky = "we")
        self.foodordered.columnconfigure(0, weight=1)
        self.foodordered.columnconfigure(1, weight=1)
        self.foodordered.columnconfigure(2, weight=1)
        
        # ordered food details
        food_items = ["something", "nothing"]
        food_quantity = [2,4]
        food_price = [10,10]
        
        # place all ordered food list in order list frame
        for i in range(len(food_items)):
            self.order(food_items[i], food_quantity[i], food_price[i], i)
            self.order(food_items[i], food_quantity[i], food_price[i], i)
            self.sub_total += food_quantity[i] * food_price[i]
        
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
        paycharges = ctk.CTkLabel(master=chargesframe, text=f"Sub Total: ${self.sub_total}\n\nTax Charges: ${tax_charge}\n\nService Charges: ${service_charge}", font=self.ffont2, height=125, pady=10, padx=10)
        total_amount = self.sub_total + tax_charge + service_charge
        payamount = ctk.CTkLabel(master=self.payframe, text=f"Total payable amount: \n${total_amount}", width=245, font=self.ffont2, height=180)
        paybtn = ctk.CTkButton(master=self.payframe, text="Pay", width=120, height=60, font=self.ffont1)
        
        # placing widgets in payment frame
        paycharges.grid(row=0, sticky="n")
        payamount.grid(row=1, sticky="n")
        paybtn.grid(row=2, sticky="ns", pady=14)
        
    # places food items in scrollable frame when called
    def order(self,food_item, quantity, price, rowq):
        item = ctk.CTkLabel(master=self.foodordered, width=210, height=40, text=f"{food_item}", font=self.ffont2, fg_color="#294868")
        quantity = ctk.CTkLabel(master=self.foodordered, width=165, text=f"{quantity}", font=self.ffont2)
        price = ctk.CTkLabel(master=self.foodordered, width=170, text=f"${price}", font=self.ffont2)
        # place them
        item.grid(row=rowq, column=0)
        quantity.grid( row=rowq, column=1)
        price.grid(row=rowq, column=2)


    def frame_config(self):
        self.configure(width=1000, height=600)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        # row and column configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

Orders("Orders")
