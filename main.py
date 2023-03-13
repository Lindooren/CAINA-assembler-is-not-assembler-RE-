import tkinter as tk
from tkinter import messagebox
import os
from process_class import *

class APP (tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # main window setup
        self.directory = os.path.dirname(__file__)
        self.resizable(False, False)
        self.config(background="grey")
        self.title("CAINA is not assembler V2.1.0")
        icon = tk.PhotoImage(file = os.path.join(self.directory, 'resources\\huaji.png'))
        self.iconphoto(False, icon)

        self.geometry("+50+50")


        self.GUIprocess = process()

        # parts setup
        self.fileopenbtn = tk.Button(master = self, text = "Load program", command = self.GUIfileopen, width = 20, height = 1, bd = 4, font = ("黑体", 15, 'bold'))
        self.steppingbtn = tk.Button(master = self, text = "Step", command = self.GUIstepping, width = 20, height = 1, bd = 4, font = ("黑体", 15, 'bold'))
        self.clearingbtn = tk.Button(master = self, text = "Clear", command = self.GUIclearing, width = 20, height = 1, bd = 4, font = ("黑体", 15, 'bold'))
        self.GUItext = tk.Text(master = self, fg = "white", bg = "black", width = 40, height = 19, font = ("黑体", 12, 'bold'))
        self.GUItext.insert("0.0", chars = self.getinfomessage())
        self.ErrorConsole = tk.Text(master = self, fg = "white", bg = "black", width = 80, height = 6, font = ("黑体", 10, 'bold'))
        self.ErrorConsole.insert("0.0", chars = self.errorexplain())

        # grid
        self.fileopenbtn.grid(row = 2, column = 0, pady = 10, padx = 10)
        self.steppingbtn.grid(row = 2, column = 1, pady = 10, padx = 10)
        self.clearingbtn.grid(row = 2, column = 2, pady = 10, padx = 10)
        self.GUItext.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        self.ErrorConsole.grid(row = 1, column = 0, columnspan = 3, pady = 10)

    # file open
    def GUIfileopen (self):
        result = self.GUIprocess.FileOpen()
        self.updateinfomessage() 
        if result:
            messagebox.showinfo(title = "Info", message = "Successfully loaded the program!")

    # stepping
    def GUIstepping (self):
        if self.GUIprocess.State == "Ended":
            messagebox.showwarning(title = "Warning", message = "Process ended normally!\nPlease load another program!")

        elif self.GUIprocess.State == "Halted":
            messagebox.showerror(title = "Error", message = "Process ended abnormally!\nPlease check your program or load another program!\nThe error is shown in the error console.")

        elif self.GUIprocess.State == "Waiting":
            messagebox.showwarning(title = "Warning", message = "You have not loaded the program yet.\nPlease load a program!")

        else:
            self.GUIprocess.Stepping()
            self.updateinfomessage()

    # clearing
    def GUIclearing (self):
        result = messagebox.askyesno(title = "Clearing?", message = "Do you want to clear everything?")
        if result:
            self.GUIprocess.Clearing()
            self.updateinfomessage()

    # update message
    def updateinfomessage (self):
        self.GUItext.delete("0.0", tk.END)
        self.GUItext.insert("0.0", chars = self.getinfomessage())
        self.ErrorConsole.delete("0.0", tk.END)
        self.ErrorConsole.insert("0.0", chars = self.errorexplain())
        self.GUItext.update()
        self.ErrorConsole.update()

    # get infomessage
    def getinfomessage (self):
        message = "----------------------------------------\n\
PC : {}\n\
ACC : {}\n\
IX : {}\n\
Out : {}\n\
State : {}\n\
Mode : {}\n\
Error : {}\n\
ProcessEnded : {}\n\
----------------------------------------\n\
CurrentAddress : {}\n\
Label : {}\n\
Opcode : {}\n\
Operand : {}\n\
Compare : {}\n\
AddressL1 : {}\n\
AddressL2 : {}\n\
Number : {}\n\
----------------------------------------\n\
".format(self.GUIprocess.PC,
self.GUIprocess.ACC,
self.GUIprocess.IX,
self.GUIprocess.Out,
self.GUIprocess.State,
self.GUIprocess.Mode,
self.GUIprocess.error,
self.GUIprocess.end,
self.GUIprocess.CurrentAddress,
self.GUIprocess.label,
self.GUIprocess.Opcode,
self.GUIprocess.Operand,
self.GUIprocess.Compare,
self.GUIprocess.AddressL1,
self.GUIprocess.AddressL2,
self.GUIprocess.Number
)

        return message

    # errorexplain
    def errorexplain (self):
        err_message = ""
        if self.GUIprocess.error != "no_error":
            err_message = "{}\n{}".format(self.GUIprocess.error, self.GUIprocess.error_content)

        return err_message

# main
if __name__ == "__main__":
    MyAPP = APP()
    MyAPP.mainloop()

# really trash
# omg the opload