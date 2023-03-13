#from TypeCheck import *
from .TypeCheck import *

def IndexedAddressing (memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, label_addr, line_addr, CurrentAddress):
    error_content = ""

    # check the type of operand. (L1)(一级地址)
    result = OperandTypeCheck(Operand)
    if result == "invalid_label_name":
        error = result
        error_content = "Line {}, Address {}.\n\'{}\' is not a valid label.".format(line_addr[CurrentAddress], CurrentAddress, Operand)
    
    else:
        try:

            # search the label in the dictionary (L1)
            if result == "label":
                AddressL1 = label_addr[Operand]

            else:
                AddressL1 = int(Operand)
            
        except KeyError:
            error = "label_not_found_L1_address"
            error_content = "Line {}, Address {}.\nCannot find level 1 address corresponds to label \'{}\'.".format(line_addr[CurrentAddress], CurrentAddress, Operand)

        else:
            
            # add index to the base address and get the result
            indexed_addr = AddressL1 + IX

            # check range (indexed)
            if not (1 <= indexed_addr <= len(memory) - 1):
                error = "indexed_address_out_of_range"
                error_content = "Line {}, Address {}.\nIndexed address \'{}\' is too big or too small.".format(line_addr[CurrentAddress], CurrentAddress, indexed_addr)

            else:
                try:
                    Number = int(memory[indexed_addr][1])

                    #selection
                    if Opcode == "LDX":
                        ACC += Number

                    elif Opcode == "STX":
                        memory[indexed_addr][1] = ACC

                    PC = PC + 1

                except ValueError:
                    error = "invalid_data_indexed_address"
                    error_content = "Line {}, Address {}.\n\Line {}, Indexed address {}.\nThe data \'{}\' under indexed address is invalid.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[indexed_addr], indexed_addr, memory[indexed_addr][1])

                except TypeError:   # None represents empty memory location
                    error = "data_not_find_indexed_address"
                    error_content = "Line {}, Address {}.\nCannot find the data under indexed address {}.".format(line_addr[CurrentAddress], CurrentAddress, indexed_addr)
  
    return memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content

#testing
if __name__ == "__main__":
    
    memory = [[None, None], 
    ['Start', 'LDX B'], 
    [None, 'LDM C'], 
    [None, 'LDM 5'], 
    ['B', '9999'], 
    ['C', '10'], 
    [None, None],
    [None, 'GGG']]

    label_addr = {'Start': 1, 'B': 4, 'C': 5}

    PC = 1
    ACC = 9
    IX = 1000
    Compare = False
    error = "no_error"
    end = False
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = None
    Opcode = "LDX"
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
        Operand {}\n".format(*IndexedAddressing(memory, 
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



    