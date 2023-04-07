import tkinter.filedialog
from tkinter import messagebox
import os

from .opcodes import *
from .memory_space import *
from .opcode_operations.type_check import *

#from opcodes import *
#from memory_space import *
#from opcode_operations.type_check import *

# file open main procedure
def OpenFile ():

    # memory initialization, 
    # each memory space could be replaced by a 'memory_space' object
    # the object could be nothing, or an instruction, or data
    max_size = 512
    memory = [memory_space() for i in range(max_size)] #in this case the line number can be address
    label_addr = {}     # label to memory address pair dictionary
    line_addr = {}      # line(of source code/text) to memory address pair dictionary

    # initialize the line to memory address pair dictionary
    for i in range(1, max_size):
        line_addr[i] = i

    pc = None           # set PC to None
    
    # initialize a dialogue of file opening
    fn = tkinter.filedialog.askopenfilename(title = "请打开.txt文件, please open .txt files", filetypes=[("纯文本文件","*.txt")])

    # check if file is empty
    if fn == "" or os.path.getsize(fn) == 0:
        return None, None, None, None
    
    # file open and read line
    with open(fn) as f:
        line_counter = 1

        # read line
        for line in f:
            line = line.strip()
            addr = line_counter
            type = None
            label = None
            opcode = None
            operand = None
            data = None

            # too many lines, for example >512 lines
            if line_counter > max_size - 1:
                return None, None, None, None

            # seperate by space for this line
            this_line = line.split(" ")
            if len(this_line) > 3:
                return None, None, None, None
            
            # treat special case if this line is 0 length
            if len(this_line) > 0 and this_line[0] != "":
                if not (this_line[0] in opcodes.opcodes):

                    # first element of the line may be label address or instruction
                    # deal with label
                    if this_line[0][-1] == ":":
                        temp = list(this_line[0])
                        temp.pop(-1)
                        label = "".join(temp)
                        
                        # deal with invalid label
                        if not LabelCheck(label):
                            return None, None, None, None
                        
                        # add label to address system
                        label_addr[label] = addr
                        this_line.pop(0)

                    # numeric address
                    else:

                        # address should be numbers only
                        numbers = "0123456789"
                        addr = this_line[0]
                        if addr[0] == "-":
                            return None, None, None, None

                        for chars in this_line[0]:
                            if not (chars in numbers):
                                return None, None, None, None
                            
                        # too big or too small address value
                        addr = int(addr)
                        if not (1 <= addr <= max_size - 1):
                            return None, None, None, None

                        this_line.pop(0)
                
                if this_line[0] in opcodes.opcodes:
                    type = "instruction" 
                    opcode = this_line[0]
                    this_line.pop(0)
                    if len(this_line) > 0:
                        operand = this_line[0]

                else:
                    type = "data"
                    data = this_line[0]
                    this_line.pop(0)
                    if len(this_line) > 0:
                        return None, None, None, None

            # assignment
            memory[addr].type, memory[addr].label, memory[addr].opcode, memory[addr].operand, memory[addr].data = type, label, opcode, operand, data
            line_addr[addr] = line_counter  # maps the line number to memery address
            line_counter += 1
        
        # automatic set PC to head of program
        for i in range(max_size):
            if memory[i].type == "instruction":
                pc = i
                break
                        
        return memory, label_addr, line_addr, pc

"""
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
"""

# testing        
if __name__ == "__main__":
    memory, label_addr, line_addr, pc = OpenFile()
    print(memory, label_addr, line_addr, pc)
    

