from PIL import Image
from customtkinter import *
from transformers import pipeline
import torch

# gui creation 
root = CTk()                    

# app format
root.geometry("600x650")
set_appearance_mode("dark")

# label format
label = CTkLabel(root, text="Enter Your Text Here:", fg_color="transparent", font = ("Lexend", 27, 'bold'))
label.pack(pady = 15)

# textbox for the summary that the user types in 
text = CTkTextbox(master=root,
                   border_color="#6FC276",
                     border_width=1.5, height = 480, 
                     width = 400, wrap="word", 
                     scrollbar_button_color = "#87CDF6", 
                     corner_radius=25)

text.pack(pady = 15)


# summarize function
def summarize():
    new_window = CTkToplevel(root)
    new_window.minsize(500, 580)
    sum_label = CTkLabel(new_window, text="Here is your summary:", fg_color="transparent", font = ("Lexend", 27, 'bold'))
    sum_label.pack(pady=15)

    user_input=text.get("1.0","end-1c")
    


    # hugging face model
    summary = pipeline("summarization", model="t5-small")
    txt = summary(user_input, max_length=120, min_length=25, do_sample=False)
    final_summary = txt[0]['summary_text']

    summary_box = CTkTextbox(master=new_window, 
                             border_color="#6FC276", 
                             border_width=1.5, 
                             height = 480, width = 400, 
                             wrap="word", 
                             scrollbar_button_color = "#87CDF6", 
                             corner_radius=25)
    
    summary_box.insert("1.0", final_summary)
    summary_box.pack(pady = 15)
    
    new_window.grab_set()


# summary button
button = CTkButton(root,
                    text="Summarize", 
                    font = ("Lexend", 18, 'bold'), 
                    fg_color = "#0082cb", 
                    border_color="#6FC276", 
                    border_width=2, 
                    height=35, 
                    corner_radius=25, 
                    hover_color = "#87CDF6", 
                    command=summarize)

button.pack(pady=15)

# settings image
icon = CTkImage(dark_image=Image.open("gear_icon.png"))

# settings button 
settings = CTkButton(root, 
                     corner_radius=25, 
                     fg_color = "#0082cb", 
                     width=4, 
                     height=40, 
                     border_color="#6FC276", 
                     border_width=2, 
                     image=icon,
                     text="",
                     hover_color = "#87CDF6")

settings.place(relx=0.01, rely=0.96, anchor="sw")


root.mainloop()