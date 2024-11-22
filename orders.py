import customtkinter as ctk
from pyglet import font
# import to connect to database
# import orders_backend

font.add_file("Documents/Trip_Sans/TripSans-Medium.ttf")
font.add_file("Documents/Trip_Sans/TripSans-Bold.ttf")
ffont = ('Trip Sans Bold', 40)
ffont1 = ('Trip Sans Medium', 20)
ffont2 = ('Trip Sans Medium', 16)

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


# creating cutstom tkinter window
app = ctk.CTk()
app.geometry("960x540")
app.title('Orders')
app.resizable(False, False)

app.lift()
app.attributes('-topmost', True)
app.after_idle(app.attributes, '-topmost', False)


#main orders frame
menu_frame = ctk.CTkFrame(master=app, width=1000, height=600)
menu_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# row and column configure
menu_frame.rowconfigure(0, weight=1)
menu_frame.rowconfigure(1, weight=4)
menu_frame.columnconfigure(0, weight=1)
menu_frame.columnconfigure(1, weight=1)
menu_frame.columnconfigure(2, weight=1)


# menu label on top
title = ctk.CTkLabel(master=menu_frame, text="ORDER", font=ffont)
title.grid(row=0, columnspan = 3, pady=8)
# title.pack(expand=True, pady=10)

# order details frame -left
odrframe = ctk.CTkScrollableFrame(master=menu_frame, width = 520, height=400)
odrframe.grid(row=1, columnspan=2, padx=10,pady = 8, sticky="ne")

# payment details frame -right
payframe = ctk.CTkFrame(master=menu_frame)
payframe.grid(row=1, column=2, padx=10, pady = 8, sticky="nw")

# order category frame
catframe = ctk.CTkFrame(master=odrframe, width=600,
                        fg_color="#333333")
catframe.pack(expand=True, fill="x")

# food details frame inside orderframe
foodordered = ctk.CTkFrame(master=odrframe, width=100, fg_color="#38618c")
foodordered.pack(expand=True, fill="x", pady=6)

# order category labels
fooditem = ctk.CTkLabel(master=catframe,
                        height=50, text="Order Name", font=ffont1)
fquantity = ctk.CTkLabel(master=catframe,
                         text="Quantity", font=ffont1)
fprice = ctk.CTkLabel(master=catframe,
                      text="Price", font=ffont1)
fquantity.pack(side="left", expand=True)
fooditem.pack(side="left", expand=True)
fprice.pack(side="right", expand=True)


# food ordered details
def order(food_item, quantity, price, rowq):
    item = ctk.CTkLabel(master=foodordered, width=190, height=40, text=f"{food_item}", font=ffont2, fg_color="#294868")
    quantity = ctk.CTkLabel(master=foodordered, width=165, text=f"{quantity}", font=ffont2)
    price = ctk.CTkLabel(master=foodordered, width=180, text=f"${price}", font=ffont2)
    # place them
    item.grid(sticky="ew", row=rowq, column=0)
    quantity.grid(sticky="ew", row=rowq, column=1)
    price.grid(sticky="ew", row=rowq, column=2)


# order_info = orders_backend.continue_orders()
# food_items = order_info[0]
# food_quantity = order_info[1]
# food_price = order_info[2]
# tax_charge = order_info[3]
# service_charge = order_info[4]

food_items = ["something", "nothing"]
food_quantity = [2,4]
food_price = [10,10]
tax_charge = 1
service_charge = 1


# declaring sub_total amount as 0
sub_total = 0
for i in range(len(food_items)):
    order(food_items[i], food_quantity[i], food_price[i], i)
    order(food_items[i], food_quantity[i], food_price[i], i)
    sub_total += food_quantity[i] * food_price[i]


# payment details
def payment_details(sub_t, tax, service):
    chargesframe = ctk.CTkFrame(
        master=payframe)
    chargesframe.grid(row=0, sticky="new", padx=15, pady=10)
    
    paycharges = ctk.CTkLabel(
        master=chargesframe, text=f"Sub Total: ${sub_t}\n\nTax Charges: ${tax}\n\nService Charges: ${service}"
                    , font=ffont2, height=125, pady=10, padx=10)
    total_amount = sub_t + tax + service
    payamount = ctk.CTkLabel(
        master=payframe, text=f"Total payable amount: \n${total_amount}", width=245, font=ffont2, height=180)
    paybtn = ctk.CTkButton(master=payframe, text="Pay",
                           width=120, height=60, font=ffont1)
    paycharges.grid(row=0, sticky="n")
    payamount.grid(row=1, sticky="n")
    paybtn.grid(row=2, sticky="ns", pady=14)

    # sub total , tax , service charge
payment_details(sub_total, tax_charge, service_charge)


app.mainloop()
