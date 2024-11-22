import customtkinter as ctk
from PIL import Image, ImageTk
from pyglet import font

class OrderStatus(ctk.CTk):
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
        self.mainframe = OrderStatusFrame(self)

        # start window 
        self.mainloop()
        
class OrderStatusFrame(ctk.CTkFrame):
    def __init__(self,window):
        super().__init__(window)
        # font config
        self.ffont = ('Trip Sans Bold', 40)
        self.ffont1 = ('Trip Sans Medium', 20)
        self.ffont2 = ('Trip Sans Medium', 16)
        
        self.call_widgets()
        
    def call_widgets(self):
        bg_image = Image.open("temp\Documents\menu_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)
        
        # order status title at top
        # order status title label
        title = ctk.CTkLabel(master=self, text="ORDER STATUS", font=self.ffont)
        title.grid(row=0, columnspan = 3, pady=8)
        # configure outside frame
        self.status_frame_config()
        # order id and order date details frame
        self.order_details_frame_con()
        # payment status label
        payment_status = "paid"
        payment_status_label = ctk.CTkLabel(master=self, width=173, text=f"Payment Status: {payment_status}", font=self.ffont2 )
        payment_status_label.grid(row = 2,sticky = "w", pady = 2)
        # order status image frame
        self.order_image_frame_con()
        # feedback frame at the bottom
        # call feedback frame after food is ready
        self.feedback_frame_con()

    def order_details_frame_con(self):
        order_details = ctk.CTkFrame(master=self, width=700)
        order_details.grid( row = 1, pady = 10, sticky = "nsew", padx = 10)
        order_details.columnconfigure(0, weight=1)
        order_details.columnconfigure(1, weight=1)
        order_details.columnconfigure(2, weight=1)
        
        order_id = 12312
        date = "19/11/23"
        
        # labels inside order_details frame
        order_id_label = ctk.CTkLabel(master=order_details, width=200, height=40, text=f"Order ID: {order_id}", font=self.ffont1)
        gap = ctk.CTkLabel(master=order_details, width=400, height=40, text=f"")
        date_label = ctk.CTkLabel(master=order_details, width=200, text=f"Date: {date}", font=self.ffont1)
        # place them
        order_id_label.grid(row=0, column=0, sticky="w")
        gap.grid(row=0, column=1, sticky="w")
        date_label.grid(row=0, column=2, sticky="e")
        
    
    def order_image_frame_con(self):
        # order status image frame
        order_status_frame = ctk.CTkFrame(master=self, width=600, height=200)
        # frame configure
        order_status_frame.grid(row = 3, pady = 10, sticky = "nsew")
        order_status_frame.columnconfigure(0, weight=1)
        order_status_frame.columnconfigure(1, weight=1)
        
        # put image in frame
        # 1st image of food preparing
        prepare_image = ctk.CTkImage(Image.open("pics/preparing_food.png"), size=(200, 200))
        prepare_image_label = ctk.CTkLabel(master=order_status_frame, image=prepare_image, text="")  # display image with a CTkLabel
        prepare_image_label.grid(row = 0, column = 0, sticky = "nsw", padx = 80, pady = 50)
        # 2nd image of food being ready
        prepared_iamge = ctk.CTkImage(Image.open("pics/Food_prepared.png"), size=(200, 200))
        prepared_image_label = ctk.CTkLabel(master=order_status_frame, image=prepared_iamge, text="")  # display image with a CTkLabel
        prepared_image_label.grid(row = 0, column = 1, sticky = "nse", padx = 80, pady = 50)
    
    # feedback frame
    def feedback_frame_con(self):
        feedback_frame = ctk.CTkFrame(master=self, width=400, height=200)
        feedback_frame.grid(row = 4)
        
        # feedback label 
        feedback_label = ctk.CTkLabel(master=feedback_frame, text="Give us your feedback: ", font=self.ffont1)
        feedback_label.grid(row = 0,  padx = 10, pady = 6)
    
    # main frame configure
    def status_frame_config(self):
        self.configure(width= 800)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


OrderStatus("Order Status")