import customtkinter as ctk

root = ctk.CTk()
root.title('Tasks')

entry = ctk.CTkEntry(root)
entry.pack(expand=True, fill='x')

tasks_frame = ctk.CTkFrame(root)
tasks_frame.pack(expand=True, fill='both')

tasks = []
for task in tasks:
    _frame = ctk.CTkFrame(tasks_frame)
    _frame.pack()
    
    _check = ctk.CTkCheckBox(_frame, )

root.mainloop()
