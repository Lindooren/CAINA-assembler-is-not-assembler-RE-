from TypeCheck import *
from Bitwise import *
#from .TypeCheck import *
#from .Bitwise import *

def ImmediateAddressing (memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, line_addr, CurrentAddress):
    error_content = ""

    # remove # in the beginning of operand
    temp = list(Operand)
    temp.pop(0)
    temp2 = "".join(temp)

    # selection
    if Opcode in ["LDM", "LDR", "CMP", "ADD", "SUB"]:

        # correct address/number format?
        if not AddressNumberCheck(temp2):
            error = "invalid_number"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid number".format(line_addr[CurrentAddress], CurrentAddress, temp2)
        
        else:
            Number = int(temp2)
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

    elif Opcode in ["AND", "OR", "XOR"]:
        Number = temp2

        # check if this binary is valid
        BinaryResultCheck = BinaryNumberCheck(Number)
        if BinaryResultCheck:

            # remove the heading B and store it to ACC
            BinVal = RemoveB(Number)
            ACC = BitWiseLogicalOperation(ACC, BinVal, Opcode)

        else:
            error = "invalid_binary_number"
            error_content = "Line {}, Address{}.\n\'{}\' is not a valid binary number".format(line_addr[CurrentAddress], CurrentAddress, Number)

    elif Opcode in ["LSL", "LSR"]:
        if not AddressNumberCheck(temp2):
            error = "invalid_number"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid number".format(line_addr[CurrentAddress], CurrentAddress, temp2)
        
        else:
            NumPlaces = int(temp2)
            
            # bits shifting
            ACC = BitsShifting(ACC, NumPlaces, Opcode)

    PC = PC + 1

    return memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content

#testing
if __name__ == "__main__":
    memory = [[None, 'AND #100']]
    
    PC = 1
    ACC = 8
    IX = 0
    Compare = False
    error = "no_error"
    end = False
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = None
    Opcode = "LSR"
    Operand = "#1"
    line_addr = {1:1}
    CurrentAddress = PC

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
        Operand {}\n\
        error_content {}".format(*ImmediateAddressing(memory, 
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
        Operand, 
        line_addr, 
        CurrentAddress)))