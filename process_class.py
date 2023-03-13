from modules.file_open import *
from modules.analysis_and_run import *

# process class (like a PCB)
class process ():
    def __init__(self) -> None:
        self.memory = None            # NO
        self.PC = None                # YES
        self.ACC = None               # YES
        self.IX = None                # YES
        self.Out = ""                 # YES
        self.State = "Waiting"        # YES
        self.Compare = None           # YES
        self.AddressL1 = None         # YES
        self.AddressL2 = None         # YES
        self.Mode = ""                # YES
        self.Number = None            # YES
        self.error = "no_error"       # YES
        self.end = False              # YES
        self.Opcode = ""              # YES
        self.Operand = ""             # YES
        self.CurrentAddress = None    # YES
        self.label_addr = None         # NO
        self.label = ""               # YES
        self.error_content = ""     # NO
        self.line_addr = None
        

        #Waiting: No file input, waiting for file input
        #Running: File exist, start running
        #Halted: process end abnormally
        #Ended: process end normally
    

    # methods
    # FileOpen method
    # return True if successfully load file
    def FileOpen (self):

        # try to read file
        memory, label_addr, line_addr, PC = open_file()

        # file empty?
        if memory != None:

            # change state to running as file loads, set PC correspond to first line
            self.__init__()
            self.ACC = 0
            self.IX = 0
            self.memory, self.label_addr, self.line_addr, self.PC = memory, label_addr, line_addr, PC
            self.State = "Running"
            return True
        
        else:
            return False

    # Stepping method
    def Stepping (self):

        # byreference the parameters through analysis, change the state when necessarry
        self.CurrentAddress = self.PC

        self.memory, self.PC, self.ACC, self.IX, self.Compare, self.error, self.end, self.Mode, self.AddressL1, self.AddressL2, self.Number, self.Out, self.Opcode, self.Operand, self.label, self.error_content = AnalysisAndRun(self.memory, self.PC, self.ACC, self.IX, self.Compare, self.label_addr, self.line_addr, self.CurrentAddress)

        if self.end == True:
            self.State = "Ended"

        elif self.error != "no_error":
            self.State = "Halted"

    # Clearing method (this is optional)
    def Clearing (self):
        self.__init__()

# testing procedure
if __name__ == "__main__":
    myprocess = process()

    # file open
    myprocess.FileOpen()

    # stepping
    if myprocess.memory != None:
        while myprocess.end == False and myprocess.error == "no_error":
            myprocess.Stepping()

            print("PC : {}\n\
        ACC : {}\n\
        IX : {}\n\
        Compare : {}\n\
        error : {}\n\
        end : {}\n\
        Mode {}\n\
        AddressL1 : {}\n\
        AddressL2 : {}\n\
        Number : {}\n\
        Out : {}\n\
        Opcode : {}\n\
        Operand : {}\n\
        label {}\n".format(myprocess.PC, 
        myprocess.ACC, 
        myprocess.IX, 
        myprocess.Compare, 
        myprocess.error, 
        myprocess.end, 
        myprocess.Mode, 
        myprocess.AddressL1, 
        myprocess.AddressL2, 
        myprocess.Number, 
        myprocess.Out, 
        myprocess.Opcode, 
        myprocess.Operand, 
        myprocess.label))

    # clearing
    clear = input("Do you want to clear everything? ")
    if clear.lower() == "y":
        myprocess.Clearing()
        print("Cleared everything!")
    
    print("memory : {}\n\
    PC : {}\n\
    ACC : {}\n\
    IX : {}\n\
    Compare : {}\n\
    error : {}\n\
    end : {}\n\
    Mode {}\n\
    AddressL1 : {}\n\
    AddressL2 : {}\n\
    Number : {}\n\
    Out : {}\n\
    Opcode : {}\n\
    Operand : {}\n\
    label {}\n".format(myprocess.memory, 
    myprocess.PC, 
    myprocess.ACC, 
    myprocess.IX, 
    myprocess.Compare, 
    myprocess.error, 
    myprocess.end, 
    myprocess.Mode, 
    myprocess.AddressL1, 
    myprocess.AddressL2, 
    myprocess.Number, 
    myprocess.Out, 
    myprocess.Opcode, 
    myprocess.Operand, 
    myprocess.label))
