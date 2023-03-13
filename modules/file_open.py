import tkinter.filedialog
from tkinter import messagebox
import os
from .opcodes import *
#from opcodes import *

def open_file ():

    # memory initialization, [<label or no label>, <instruction|label or value>]
    memory = [[None, None] for i in range(512)] #in this case the line number can be address
    label_addr = {} # label system to pair
    line_addr = {}
    
    fn = tkinter.filedialog.askopenfilename(title = "请打开.txt文件, please open .txt files", filetypes=[("纯文本文件","*.txt")])
    PC = None

    # check presence of file
    if fn == "" or os.path.getsize(fn) == 0:
        return None, None, None, None
    
    # file open and read line
    with open(fn) as f:
        line = f.readline().strip()
        line_counter = 1

        # read line if not empty line
        if len(line) > 0:
            while len(line) > 0:
                addr = line_counter

                # too many line read
                if addr > len(memory) - 1:
                    OutputMessage(value = 5, error_content = len(memory) - 1)
                    return None, None, None, None

                # the line contain address + (content OR opcode + operand), seperate by space
                this_line = line.split(" ")
                if len(this_line) > 3:
                    OutputMessage(value = 1, line_counter = line_counter)
                    return None, None, None, None
                
                if not (this_line[0] in opcodes.Opcodes):

                    # first element of the line may be label address or instruction
                    # deal with label
                    if this_line[0][-1] == ":":
                        temp = list(this_line[0])
                        temp.pop(-1)
                        label = "".join(temp)

                        # deal with 0 length label
                        if len(label) == 0:
                            OutputMessage(value = 2, line_counter = line_counter, error_content = label)
                            return None, None, None, None
                        
                        # deal with label with invalid characters
                        invalid_chars = "0123456789:;<=>?@[\]^`{|}~!#$%^&*()\"\',./"
                        for char in label:
                            if char in invalid_chars:
                                OutputMessage(value = 2, line_counter = line_counter, error_content = label)
                                return None, None, None, None
                        
                        # add label to address system
                        label_addr[label] = addr
                        memory[addr][0] = label
                        this_line.pop(0)

                    # deal with address
                    else:

                        # address should be numbers only
                        numbers = "0123456789"
                        addr = this_line[0]
                        if addr[0] == "-":
                            OutputMessage(value = 3, line_counter = line_counter, error_content = addr)
                            return None, None, None, None

                        for chars in this_line[0]:
                            if not (chars in numbers):
                                OutputMessage(value = 3, line_counter = line_counter, error_content = addr)
                                return None, None, None, None
                            
                        # too big or too small address value
                        addr = int(addr)
                        if not (1 <= addr <= len(memory) - 1):
                            OutputMessage(value = 4, line_counter = line_counter, error_content = addr)
                            return None, None, None, None

                        this_line.pop(0)
                    

                content = " ".join(this_line)
                memory[addr][1] = content
                line_addr[addr] = line_counter  # this maps the lines in program to address locations.

                line = f.readline().strip()
                line_counter += 1
            
            # automatic set PC to head of program
            for i in range(len(memory)):
                if memory[i][0] != None or memory[i][1] != None:
                    PC = i
                    break
                            
            return memory, label_addr, line_addr, PC
            
        else:
            OutputMessage(value = 0, line_counter = line_counter)
            return None, None, None, None

# error output
def OutputMessage (value, line_counter = 1, error_content = None):
    if value == 0:
        messagebox.showerror(title = "Error", message = "Line {}\nEmpty line detected in first line!".format(line_counter))
    elif value == 1:
        messagebox.showerror(title = "Error", message = "Line {}\nThe maximum words or elemet of a line must not exceed 3!".format(line_counter))
    elif value == 2:
        messagebox.showerror(title = "Error", message = "Line {}\n{} is not a valid label.".format(line_counter, error_content))
    elif value == 3:
        messagebox.showerror(title = "Error", message = "Line {}\n{} is not a valid address.".format(line_counter, error_content))
    elif value == 4:
        messagebox.showerror(title = "Error", message = "Line {}\nThe address {} is either too big or too small!\n".format(line_counter, error_content))
    elif value == 5:
        messagebox.showerror(title = "Error", message = "Largest memory address is {}!\nLoading failed!".format(error_content))

# testing        
if __name__ == "__main__":
    memory, label_addr, line_addr, PC = open_file()
    print(memory, label_addr, line_addr, PC)
    

