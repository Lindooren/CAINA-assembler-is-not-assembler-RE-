from modules.file_open import *
from modules.analysis_and_run import *

# process class (like a PCB)
class process ():
    def __init__(self) -> None:
        self.memory = None
        self.pc = None
        self.acc = None
        self.ix = None
        self.out = ""
        self.state = "Waiting"
        self.compare = None
        self.addressL1 = None
        self.addressL2 = None
        self.mode = ""
        self.number = None
        self.error = "no_error"
        self.end = False
        self.opcode = ""
        self.operand = ""
        self.current_address = None
        self.label_addr = None
        self.label = ""
        self.error_content = ""
        self.line_addr = None
        
        #Waiting: No file input, waiting for file input
        #Running: File exist, start running
        #Halted: process end abnormally
        #Ended: process end normally
    
    # methods
    # file open method
    # return True if successfully load file
    def FileOpen (self):

        # try to read file
        memory, label_addr, line_addr, pc = OpenFile()

        # file empty?
        if memory != None:

            # change state to running as file loads, set PC correspond to first line
            self.__init__()
            self.acc = 0
            self.ix = 0
            self.memory, self.label_addr, self.line_addr, self.pc = memory, label_addr, line_addr, pc
            self.state = "Running"
            return True
        
        else:
            return False

    # Stepping method
    def Stepping (self):

        # byreference the parameters through analysis, change the state when necessarry
        self.current_address = self.pc

        self.memory, self.pc, self.acc, self.ix, self.compare, self.error, self.end, self.mode, self.addressL1, self.addressL2, self.number, self.out, self.opcode, self.operand, self.label, self.error_content = AnalysisAndRun(self.memory, self.pc, self.acc, self.ix, self.compare, self.label_addr, self.line_addr, self.current_address)

        if self.end == True:
            self.state = "Ended"

        elif self.error != "no_error":
            self.state = "Halted"

    # Clearing method
    def Clearing (self):
        self.__init__()

# testing
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
        label {}\n".format(myprocess.pc, 
        myprocess.acc, 
        myprocess.ix, 
        myprocess.compare, 
        myprocess.error, 
        myprocess.end, 
        myprocess.mode, 
        myprocess.addressL1, 
        myprocess.addressL2, 
        myprocess.number, 
        myprocess.out, 
        myprocess.opcode, 
        myprocess.operand, 
        myprocess.label))

    # clearing
    clear = input("Do you want to clear everything? ")
    if clear.lower() == "y":
        myprocess.Clearing()
        print("Cleared everything!")
    
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
        label {}\n".format(myprocess.pc, 
        myprocess.acc, 
        myprocess.ix, 
        myprocess.compare, 
        myprocess.error, 
        myprocess.end, 
        myprocess.mode, 
        myprocess.addressL1, 
        myprocess.addressL2, 
        myprocess.number, 
        myprocess.out, 
        myprocess.opcode, 
        myprocess.operand, 
        myprocess.label))