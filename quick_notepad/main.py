import customtkinter as ctk
import datetime
import os

if not os.path.isdir('docs'):
    os.mkdir('docs')

filename = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}_entry_#{len(os.listdir("docs"))}.txt'

root = ctk.CTk()
root.geometry('800x600')

label = ctk.CTkLabel(root, text=filename)
label.pack()

text_area = ctk.CTkTextbox(root)
text_area.pack(expand=True, fill='both')

def save():
    with open(filename, 'w') as f:
        f.write(text_area.get())

save_btn = ctk.CTkButton(root, text="Salvar", command=save)
save_btn.pack()

root.mainloop()
