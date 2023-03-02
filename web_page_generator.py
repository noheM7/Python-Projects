import tkinter as tk 
from tkinter import *
import webbrowser 





# buttons and self function
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        self.btn= Button(self.master, text= "Default HTML Page", width= 30,height=2, command=self.defaultHTML)
        self.btn.grid(row=4, column= 3)
        self.custom_lbl = tk.Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.custom_lbl.grid(row=3, column=0)
        self.custom_btn = Button(self.master, text="Submit Custom text",width=30, height= 2, command=self.customHTML)
        self.custom_btn.grid(row=4 , column= 4)
        self.custom_text = tk.Entry(self.master, text = '', width=75)
        self.custom_text.grid(row=3 , column= 3)

    #the default function
    def defaultHTML(self):
        htmlText= "Stay tuned for our amazing summer sale!!"
        htmlFile= open("index.html", "w")
        htmlContent= "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #create on text function
    def customHTML(self):
        customText = (self.custom_text.get())
        customFile = open("index.html", "w")
        customContent = "<html>\n<body>\n<h1>" + customText + "</html>\n</body>\n</h1>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("index.html")
#execute
if __name__ == "__main__":
    root= tk.Tk()
    App= ParentWindow(root)
    root.mainloop()