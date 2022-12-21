import tkinter
from tkinter import *

class Gui:

    def __init__(self, fields) -> None:
        self.root = tkinter.Tk()
        self.field_number = fields
        self.field_size = (self.root.winfo_screenheight()-100)/fields
        self.root.geometry('%dx%d+0+0' % (self.field_size*fields, self.field_size*fields))
        self.canvas = Canvas(self.root, background='black')
        self.canvas.place(width=self.field_size*fields, height=self.field_size*fields)
    
    def start(self, loop, args):
        self.root.after(0, self.run, (loop, args))
        self.root.mainloop()

    # fct_args = (function, function_args)
    def run(self, fct_args):
        self.canvas.delete('all')
        #self.draw_grid()
        self.root.wm_title('TSP')
        fct_args[0](*fct_args[1])
        self.root.after(500, self.run, fct_args)
        
    def draw_grid(self):
        for i in range(self.field_number):
            self.canvas.create_line(self.field_size*i, 0, self.field_size*i, self.field_size*self.field_number, fill="white", width=1)
            self.canvas.create_line(0, self.field_size*i, self.field_size*self.field_number, self.field_size*i, fill="white", width=1)