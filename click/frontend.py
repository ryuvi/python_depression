import tkinter as tk
import tkinter.ttk as ttk
import pyautogui as ag

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        width, height = 800, 600
        self.geometry(f'{width}x{height}')
        
        mouseinfoframe = ttk.Frame(self)
        mouseinfoframe.pack(side=tk.TOP)
        mouseinfolabel = tk.Label(mouseinfoframe, text="Mouse Info")
        mouseinfolabel.pack()
        mouseinfobutton = tk.Button(mouseinfoframe, text="Start", command=self.mouse_info)
        mouseinfobutton.pack()

        # tabControl = ttk.Notebook(self)
        full_frame = ttk.Frame(master=self)
        full_frame.pack()

        tabs = {
            "Egg, Inc.": EggInc(master=full_frame),
            "Trash Tycoon": TrashTycoon(master=full_frame),
            "Cells To Singularity": Cells(master=full_frame)
        }

        for tab in tabs:
            # tabControl.add(tabs[tab], text=tab)
            tabs[tab].pack()

        # tabControl.pack(expand=1, fill='both')

    def run(self):
        self.mainloop()

    def mouse_info(self):
        ag.mouseInfo()


class EggInc(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TrashTycoon(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        info_frame = ttk.Frame(self)
        info_frame.pack()
        
        self.checkvar = tk.BooleanVar(value=True)
        checkbox_info = tk.Checkbutton(info_frame, text="X, Y Information", variable=self.checkvar, onvalue=True, offvalue=False)
        checkbox_info.pack()
        
        self.entryvalue = tk.StringVar()
        entry_info = tk.Entry(info_frame, textvariable=self.entryvalue)
        entry_info.pack()
        
        self.flagstartstop = tk.BooleanVar(value=True)
        btframe = ttk.Frame(self)
        btframe.pack(side=tk.BOTTOM)
        start = tk.Button(self, text="Start", command=self.start_click)
        start.pack(side=tk.LEFT)
        stop = tk.Button(self, text="Stop", command=self.stop_click)
        stop.pack(side=tk.RIGHT)
        
    def start_click(self):
        if self.checkvar:
            self.flagstartstop.set(True)
            x, y = [a.strip() for a in self.entryvalue.get().split(',')]
            ag.moveTo(x, y)
            while self.flagstartstop.get():
                ag.click()
                
    def stop_click(self):
        self.flagstartstop.set(False)


class Cells(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

if __name__ == '__main__':
    mp = MainPage()
    mp.run()