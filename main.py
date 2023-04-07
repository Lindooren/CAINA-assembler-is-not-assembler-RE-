import tkinter as tk
from tkinter import messagebox
import os
from process_class import *

class app (tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # main window setup
        self.directory = os.path.abspath(".")
        self.resizable(False, False)
        self.config(background="grey")
        self.title("CAINA is not assembler V2.3.0")
        icon = tk.PhotoImage(file = os.path.join(self.directory, 'resources\\huaji.png'))
        self.iconphoto(False, icon)

        self.geometry("+50+50")


        self.GUI_process = process()

        # parts setup
        self.file_open_btn = tk.Button(master = self, text = "Load program", command = self.GUIFileOpen, width = 20, height = 1, bd = 4, font = ("System", 15, 'bold'))
        self.stepping_btn = tk.Button(master = self, text = "Step", command = self.GUIStepping, width = 20, height = 1, bd = 4, font = ("System", 15, 'bold'))
        self.clearing_btn = tk.Button(master = self, text = "Clear", command = self.GUIClearing, width = 20, height = 1, bd = 4, font = ("System", 15, 'bold'))
        self.GUI_text = tk.Text(master = self, fg = "white", bg = "black", width = 40, height = 19, font = ("System", 12, 'bold'))
        self.GUI_text.insert("0.0", chars = self.GetInfoMessage())
        self.error_console = tk.Text(master = self, fg = "white", bg = "black", width = 60, height = 8, font = ("System", 10, 'bold'))
        self.error_console.insert("0.0", chars = self.ErrorLogger())

        # grid
        self.file_open_btn.grid(row = 2, column = 0, pady = 10, padx = 10)
        self.stepping_btn.grid(row = 2, column = 1, pady = 10, padx = 10)
        self.clearing_btn.grid(row = 2, column = 2, pady = 10, padx = 10)
        self.GUI_text.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        self.error_console.grid(row = 1, column = 0, columnspan = 3, pady = 10)

        # color_change
        self.GUI_text.tag_add("State", "6.8", "6.39")
        self.GUI_text.tag_add("Error", "8.8", "8.39")
        self.GUI_text.tag_add("ProcessEnded", "9.15", "9.39")

        self.GUI_text.tag_config("State", foreground = "blue")
        self.GUI_text.tag_config("ProcessEnded", foreground = "red")
        self.GUI_text.tag_config("Error", foreground = "green")
        self.error_console.configure(background = "blue")

    # File Open
    def GUIFileOpen (self):
        result = self.GUI_process.FileOpen()
        self.UpdateInfoMessage() 
        if result:
            messagebox.showinfo(title = "Info", message = "Successfully loaded the program!")

    # Stepping
    def GUIStepping (self):
        if self.GUI_process.state == "Ended":
            messagebox.showwarning(title = "Warning", message = "Process ended normally!\nPlease load another program!")

        elif self.GUI_process.state == "Halted":
            messagebox.showerror(title = "Error", message = "Process ended abnormally!\nPlease check your program or load another program!\nThe error is shown in the error console.")

        elif self.GUI_process.state == "Waiting":
            messagebox.showwarning(title = "Warning", message = "You have not loaded the program yet.\nPlease load a program!")

        else:
            self.GUI_process.Stepping()
            self.UpdateInfoMessage()

    # Clearing
    def GUIClearing (self):
        result = messagebox.askyesno(title = "Clearing?", message = "Do you want to clear everything?")
        if result:
            self.GUI_process.Clearing()
            self.UpdateInfoMessage()

    # Update Info Message
    def UpdateInfoMessage (self):
        self.GUI_text.delete("0.0", tk.END)
        self.GUI_text.insert("0.0", chars = self.GetInfoMessage())
        self.error_console.delete("0.0", tk.END)
        self.error_console.insert("0.0", chars = self.ErrorLogger())
        self.GUI_text.update()
        self.error_console.update()
        self.ColourUpdate()

    # Colour Update
    def ColourUpdate (self):
        state_colour, process_end_colour, error_colour = "", "", ""

        # state colour
        if self.GUI_process.state == "Waiting":
            state_colour = "blue"
            self.error_console.configure(background = "blue", foreground = "white")
        
        elif self.GUI_process.state == "Running":
            state_colour = "green"
            self.error_console.configure(background = "green", foreground = "white")

        elif self.GUI_process.state == "Ended":
            state_colour = "yellow"
            self.error_console.configure(background = "yellow", foreground = "black")

        else:
            state_colour = "red"
            self.error_console.configure(background = "red", foreground = "white")

        # process_end_colour
        if self.GUI_process.end == True:
            process_end_colour = "green"

        else:
            process_end_colour = "red"

        # error_colour
        if self.GUI_process.error == "no_error":
            error_colour = "green"

        else:
            error_colour = "red"
        
        self.GUI_text.tag_remove("State", "6.8", "6.39")
        self.GUI_text.tag_add("Error", "8.8", "8.39")
        self.GUI_text.tag_add("ProcessEnded", "9.15", "9.39")

        self.GUI_text.tag_add("State", "6.8", "6.39")
        self.GUI_text.tag_add("Error", "8.8", "8.39")
        self.GUI_text.tag_add("ProcessEnded", "9.15", "9.39")

        self.GUI_text.tag_configure("State", foreground =   state_colour)
        self.GUI_text.tag_configure("ProcessEnded", foreground = process_end_colour)
        self.GUI_text.tag_configure("Error", foreground = error_colour)
        
    # Get Info Message
    def GetInfoMessage (self):
        message = "--------------------------------------------------------------------------------\n\
PC : {}\n\
ACC : {}\n\
IX : {}\n\
Out : {}\n\
State : {}\n\
Mode : {}\n\
Error : {}\n\
ProcessEnded : {}\n\
--------------------------------------------------------------------------------\n\
CurrentAddress : {}\n\
Label : {}\n\
Opcode : {}\n\
Operand : {}\n\
Compare : {}\n\
AddressL1 : {}\n\
AddressL2 : {}\n\
Number : {}\n\
--------------------------------------------------------------------------------\n\
".format(self.GUI_process.pc,
self.GUI_process.acc,
self.GUI_process.ix,
self.GUI_process.out,
self.GUI_process.state,
self.GUI_process.mode,
self.GUI_process.error,
self.GUI_process.end,
self.GUI_process.current_address,
self.GUI_process.label,
self.GUI_process.opcode,
self.GUI_process.operand,
self.GUI_process.compare,
self.GUI_process.addressL1,
self.GUI_process.addressL2,
self.GUI_process.number
)

        return message

    # Error Logger
    def ErrorLogger (self):
        err_message = "Error Console Logger:\n"
        if self.GUI_process.error != "no_error":
            err_message = err_message + "{}\n{}".format(self.GUI_process.error, self.GUI_process.error_content)

        return err_message

# main running
if __name__ == "__main__":
    my_app = app()
    my_app.mainloop()