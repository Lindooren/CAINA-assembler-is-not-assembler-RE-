# from TypeCheck import *
from .TypeCheck import *

def IndirectAddressing (memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, label_addr, line_addr, CurrentAddress):
    error_content = ""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

            # check range (L1)
            if not (1 <= AddressL1 <= len(memory) - 1):
                error = "L1_address_out_of_range"
                error_content = "Line {}, Address {}.\nLevel 1 address \'{}\' is too big or too small.".format(line_addr[CurrentAddress], CurrentAddress, AddressL1)

            else:
                
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # get the content from AddressL1
                content = memory[AddressL1][1]

                # check the type of content (L2)(二级地址)
                result = OperandTypeCheck(content)
                if result == "invalid_label_name":
                    error = result
                    error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\n\'{}\' is not a valid label.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[AddressL1], AddressL1, content)

                else:
                    try:

                        # search the label in the dictionary (L1)
                        if result == "label":
                            AddressL2 = label_addr[content]

                        else:
                            AddressL2 = int(content)

                    except KeyError:
                        error = "label_not_found_L2_address"
                        error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nCannot find level 2 address corresponds to label \'{}\'.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[AddressL1], AddressL1, content)

                    else:

                        # check range (L1)
                        if not (1 <= AddressL2 <= len(memory) - 1):
                            error = "L2_address_out_of_range"
                            error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nLevel 2 address \'{}\' is too big or too small.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[AddressL1], AddressL1, AddressL2)

                        else:
                            try:

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                Number = int(memory[AddressL2][1]) 
                                        
                                # selection
                                if Opcode == "LDI":
                                    ACC = Number

                                elif Opcode == "CMI":
                                    Compare = True if ACC == Number else False

                                PC = PC + 1
                            
                            except ValueError:
                                error = "invalid_data_L2_address"
                                error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nLine {}, Level 2 address {}.\nThe data \'{}\' under level 2 address is invalid.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[AddressL1], AddressL1, line_addr[AddressL2], AddressL2,memory[AddressL2][1])

                            except TypeError:   # None represents empty memory location
                                error = "data_not_find_L2_address"
                                error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nCannot find the data under level 2 address.".format(line_addr[CurrentAddress], CurrentAddress, line_addr[AddressL1], AddressL1, line_addr[AddressL2])

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

    label_addr = {'Start': 1, 'B': 4, 'C': 5}

    PC = 1
    ACC = 10
    IX = 0
    Compare = False
    error = "no_error"
    end = False
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = None
    Opcode = "CMI"
    Operand = "C"

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
        Operand {}\n".format(*IndirectAddressing(memory, 
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

    