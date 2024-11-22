import customtkinter as ctk
from pyglet import font
# from login_backend import *

#Font setup
reg_font = ('Trip Sans Medium', 40)
entry_font = ('Trip Sans Medium', 20)

#Mode setup
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  #creating cutstom tkinter window
app.geometry("960x540")
app.title('Register')
app.resizable(False,False)
app.lift()
app.attributes('-topmost',True)
app.after_idle(app.attributes,'-topmost',False)


# def register_button_function():
#     email_id = email_id.get()
#     name = name_entry.get()
#     password = password_entry.get()
#     status = openMenu(email_id, password)
#     if status == 0:
#         reg_text.configure(text="Wrong username")
#     elif status == -1:
#         reg_text.configure(text="Wrong password")
#     else:
#         reg_text.configure(text="Done", text_color="white")
        
#         #Configure going to menu here



#Login Frame
reg_frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=15)
reg_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
reg_frame.pack_propagate(0)

reg_text = ctk.CTkLabel(master=reg_frame, text="Register",font=reg_font)
# reg_text.pack(padx=30, pady=(40,20), anchor="w")
reg_text.pack(padx=30, pady=(40,20))

#Frame Widgets
email_entry=ctk.CTkEntry(master=reg_frame, width=220, placeholder_text='Email ID', font=entry_font)
email_entry.pack(padx=30, pady=5)

name_entry=ctk.CTkEntry(master=reg_frame, width=220, placeholder_text='Name', font=entry_font)
name_entry.pack(padx=30, pady=5)

password_entry=ctk.CTkEntry(master=reg_frame, width=220, placeholder_text='Password', font=entry_font, show="*")
password_entry.pack(padx=30, pady=5)

reg_button = ctk.CTkButton(master=reg_frame, width=220, text="Register", font=entry_font,  corner_radius=6) #command=register_button_function,
reg_button.pack(padx=30, pady=5)

reg_text = ctk.CTkLabel(master=reg_frame, text="", font=entry_font, text_color="red")
reg_text.pack(padx=30, pady=5)

app.mainloop()