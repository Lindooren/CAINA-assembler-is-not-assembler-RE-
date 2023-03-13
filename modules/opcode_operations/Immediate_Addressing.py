# from TypeCheck import *
from .TypeCheck import *

def ImmediateAddressing (memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, line_addr, CurrentAddress):
    error_content = ""

    # first char of operand is "#"
    # remove # in the beginning of operand
    temp = list(Operand)
    temp.pop(0)
    temp2 = "".join(temp)

    # correct address/number format?
    if not AddressNumberCheck(temp2):
        error = "invalid_number"
        error_content = "Line {}, Address {}.\n\'{}\' is not an invalid number".format(line_addr[CurrentAddress], CurrentAddress, temp2)

    else:
        Number = int(temp2)

        # selection
        if Opcode == "LDM":
            ACC = Number

        elif Opcode == "LDR":
            IX = Number

        elif Opcode == "CMP":
            Compare = True if ACC == Number else False

        elif Opcode == "ADD":
            ACC = ACC + Number

        elif Opcode == "SUB":
            ACC = ACC - Number

        PC = PC + 1

    return memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content

#testing
if __name__ == "__main__":
    
    memory = [[None, 'LDI '], 
            [None, 'LDI '], 
            [None, 'LDI #3'], 
            [None, 'LDI #3'], 
            [None, 'LDI #3'], 
            [None, 'LDI #3']]
    
    PC = 1
    ACC = 5
    IX = 0
    Compare = False
    error = "no_error"
    end = False
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = None
    Opcode = "SUB"
    Operand = "#6"

    print("memory {}\n\
        PC {}\n\
        ACC {}\n\
        IX {}\n\
        Compare {}\n\
        error {}\n\
        end {}\n\
        AddressL1 {}\n\
        AddressL2 {}\n\
        Number {}\n\
        Out {}\n\
        Opcode {}\n\
        Operand {}\n".format(*ImmediateAddressing(memory, 
        PC, 
        ACC, 
        IX, 
        Compare, 
        error, 
        end, 
        AddressL1, 
        AddressL2, 
        Number, 
        Out, 
        Opcode, 
        Operand)))