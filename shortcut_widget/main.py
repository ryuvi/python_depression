import customtkinter as tk
import configparser as cp


shortcuts = {}
config = cp.ConfigParser()
config.read('src/shortcuts.ini')

shortcuts.update({a: {b: config.get(a, b) for b in config.options(a)} for a in config.sections()})

root = tk.CTk()

for section in shortcuts.keys():
    tk.CTkLabel(root, text=section).pack()
    cur_ss = tk.CTkFrame(root)
    cur_ss.pack()
    ss = shortcuts[section]
    left_opt = tk.CTkFrame(cur_ss)
    left_opt.pack(side=tk.LEFT, expand=True, fill='both', padx=10, pady=10)
    right_opt = tk.CTkFrame(cur_ss)
    right_opt.pack(side=tk.RIGHT, expand=True, fill='both', padx=10, pady=10)
    for option in ss:
        tk.CTkLabel(left_opt, text=option).pack(padx=10)
        tk.CTkLabel(right_opt, text=ss[option]).pack(padx=10)

root.mainloop()
