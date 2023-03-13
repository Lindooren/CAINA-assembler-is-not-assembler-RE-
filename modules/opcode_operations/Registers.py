def Registers (memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, line_addr, CurrentAddress):
    error_content = ""
    
    if Opcode == "MOV":
        if Operand == "IX":
            IX = ACC

        else:
            error = "invalid_register"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid register.".format(line_addr[CurrentAddress], CurrentAddress, Operand)

    elif Opcode == "INC":
        if Operand == "ACC":
            ACC += 1

        elif Operand == "IX":
            IX += 1

        else:
            error = "invalid_register"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid register.".format(line_addr[CurrentAddress], CurrentAddress, Operand)

    elif Opcode == "DEC":
        if Operand == "ACC":
            ACC -= 1

        elif Operand == "IX":
            IX -= 1

        else:
            error = "invalid_register"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid register.".format(line_addr[CurrentAddress], CurrentAddress, Operand)

    PC += 1

    return memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content

#testing
if __name__ == "__main__":
    
    memory = [[None, None], 
    ['Start', 'LDM B'], 
    [None, 'LDM C'], 
    [None, 'LDM 5'], 
    ['B', 'C'], 
    ['C', '10'], 
    [None, None],
    [None, 'GGG']]

    line_addr = {'Start': 1, 'B': 4, 'C': 5}

    PC = 1
    ACC = 9
    IX = 1
    Compare = False
    error = "no_error"
    end = False
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = None
    Opcode = "INC"
    Operand = "AC"

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
        Operand {}\n".format(*Registers(memory, 
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