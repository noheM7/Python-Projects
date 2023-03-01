import tkinter as tk
from tkinter import *
import tkinter.filedialog 


class ParentWindow(Frame):
    def __init__(self, master):
         
            
            Frame.__init__(self)
            self.master.title("File Transfer")
            self.sourceDir_btn=Button(text="Select source", width=20, command=self.sourceDir)
            self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))
            self.source_dir= Entry(width=75)
            self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30, 0))

            self.destDir_btn=Button(text="Select destination", width=20, command=self.destDir)
            self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))
            self.destination_dir= Entry(width=75)
            self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15, 10))
    def sourceDir(self):
            selectSourceDir= tkinter.filedialog.askdirectory()
            self.source_dir.delete(0,END)
            self.source_dir.insert(0,selectSourceDir)
    def destDir(self):
            selectDestDir=tkinter.filedialog.askdirectory()
            self.destination_dir.delete(0,END)
            self.destination_dir.insert(0, selectDestDir)


if __name__== "__main__":
    root=tk.Tk()
    App= ParentWindow(root)
    root.mainloop()