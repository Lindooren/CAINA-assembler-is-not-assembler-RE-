#from TypeCheck import *
from .TypeCheck import *

def DirectAddressing (memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, label_addr, line_addr, CurrentAddress):
    error_content = ""
    
    # check the type of operand.
    result = OperandTypeCheck(Operand)
    if result == "invalid_label_name":
        error = result
        error_content = "Line {}, Address {}.\n\'{}\' is not a valid label.".format(line_addr[CurrentAddress], CurrentAddress, Operand)
    
    else:
        try:

            # search the label in the dictionary
            if result == "label":
                AddressL1 = label_addr[Operand]

            else:
                AddressL1 = int(Operand)
            
        except KeyError:
            error = "label_not_found_L1_address"
            error_content = "Line {}, Address {}.\nCannot find level 1 address corresponds to label \'{}\'.".format(line_addr[CurrentAddress], CurrentAddress, Operand)
            
        else:

            # check range
            if not (1 <= AddressL1 <= len(memory) - 1):
                error = "L1_address_out_of_range"
                error_content = "Line {}, Address {}.\nLevel 1 address \'{}\' is too big or too small.".format(line_addr[CurrentAddress], CurrentAddress, AddressL1)

            else:
            
                # selection
                try:
                    if not(Opcode in ["JMP", "JPE", "JPN", "STO"]):
                        Number = int(memory[AddressL1][1]) 

                    if Opcode == "LDD":
                        ACC = Number

                    elif Opcode == "STO":
                        memory[AddressL1][1] = str(ACC)

                    elif Opcode == "JMP":
                        PC = AddressL1

                    elif Opcode == "CMP":
                        Compare = True if ACC == Number else False

                    elif Opcode == "JPE":
                        PC = AddressL1 if (Compare and Compare != None) else PC + 1
                        Compare = None
                    
                    elif Opcode == "JPN":
                        PC = AddressL1 if not (Compare and Compare != None) else PC + 1
                        Compare = None

                    elif Opcode == "ADD":
                        ACC += Number

                    elif Opcode == "SUB":
                        ACC -= Number

                    if not Opcode in ["JMP", "JPE", "JPN"]:
                        PC = PC + 1

                except ValueError:
                    error = "invalid_data_L1_address"
                    error_content = "Line {}, Address {}.\n\Line {}, Level 1 address {}.\nThe data \'{}\' under level 1 address is invalid.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[AddressL1], AddressL1, memory[AddressL1][1])

                except TypeError:   # None represents empty memory location
                    error = "data_not_find_L1_address"
                    error_content = "Line {}, Address {}.\nCannot find the data under level 1 address \'{}\'.".format(line_addr[CurrentAddress], CurrentAddress, AddressL1)

    return memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content

#testing
if __name__ == "__main__":
    
    memory = [[None, None], 
    ['Start', 'LDD B'], 
    [None, 'LDM C'], 
    [None, 'LDM 5'], 
    ['B', '1000000000000000000'], 
    ['C', '5'], 
    [None, None],
    [None, 'GGG']]

    label_addr = {'Start': 1, 'B': 4, 'C': 5}

    PC = 1
    ACC = 6
    IX = 0
    Compare = False
    error = "no_error"
    end = False
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = None
    Opcode = "LDD"
    Operand = "B"
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
        Operand {}\n".format(*DirectAddressing(memory, 
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
        label_addr)))