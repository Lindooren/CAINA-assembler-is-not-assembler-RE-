#from type_check import *
#from bitwise import *

from .type_check import *
from .bitwise import *

def DirectAddressing (memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, label_addr, line_addr, current_address):
    error_content = ""
    
    # check the type of operand.
    result = OperandTypeCheck(operand)
    if result == "invalid_label_name":
        error = result
        error_content = "Line {}, Address {}.\n\'{}\' is not a valid label.".format(line_addr[current_address], current_address, operand)
    
    else:
        try:

            # search the label in the dictionary
            if result == "label":
                addressL1 = label_addr[operand]

            else:
                addressL1 = int(operand)
            
        except KeyError:
            error = "label_not_found_L1_address"
            error_content = "Line {}, Address {}.\nCannot find level 1 address corresponds to label \'{}\'.".format(line_addr[current_address], current_address, operand)
            
        else:

            # check range of L1 address
            if not (1 <= addressL1 <= len(memory) - 1):
                error = "L1_address_out_of_range"
                error_content = "Line {}, Address {}.\nLevel 1 address \'{}\' is too big or too small.".format(line_addr[current_address], current_address, addressL1)

            else:
                addressL1_location = memory[addressL1]
                
                # selection
                if opcode in ["LDD", "CMP", "ADD", "SUB"]:
                    try:
                        if addressL1_location.type == "data":
                            number = int(addressL1_location.data)

                            if opcode == "LDD":
                                acc = number

                            elif opcode == "CMP":
                                compare = True if acc == number else False

                            elif opcode == "ADD":
                                acc += number

                            elif opcode == "SUB":
                                acc -= number

                        else:
                            error = "invalid_L1_address_content_type"
                            error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nThe required memory lcoation at this level 1 address should be \'data\' but currently the type is \'{}\' ".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, addressL1_location.type)
                    
                    except ValueError:
                        error = "invalid_data_L1_address"
                        error_content = "Line {}, Address {}.\n\Line {}, Level 1 address {}.\nThe data \'{}\' under level 1 address is invalid.".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, memory[addressL1][1])

                elif opcode in ["JMP", "JPE", "JPN", "STO"]:
                    if opcode == "STO":
                        memory[addressL1].type = "data"
                        memory[addressL1].opcode, memory[addressL1].operand = None, None
                        memory[addressL1].data = str(acc)

                    elif opcode == "JMP":
                        pc = addressL1

                    elif opcode == "JPE":
                        pc = addressL1 if compare == True else pc + 1
                        compare = None
                    
                    elif opcode == "JPN":
                        pc = addressL1 if compare == False else pc + 1
                        compare = None

                # Bitwise Direct Addressing Opcodes
                elif opcode in ["AND", "OR", "XOR"]:
                    if addressL1_location.type == "data":
                        number = str(addressL1_location.data)
                        if BinaryNumberCheck(number):

                            # remove the heading B and store it to ACC
                            bin_val = RemoveB(number)
                            acc = BitWiseLogicalOperation(acc, bin_val, opcode)

                        else:
                            error = "invalid_binary_number"
                            error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\n\'{}\' is not a valid binary number".format(line_addr[current_address], current_address,line_addr[addressL1], addressL1, number)
            
                    else:
                        error = "invalid_L1_address_content_type"
                        error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nThe required memory lcoation at this level 1 address should be \'data\' but currently the type is \'{}\'".format(line_addr[current_address], current_address,line_addr[addressL1], addressL1, addressL1_location.type)
                
                if not (opcode in ["JMP", "JPE", "JPN"]):
                    pc = pc + 1
            
                 

    return memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content

#testing
if __name__ == "__main__":
    from memory_space import *

    location_a = memory_space()
    location_b = memory_space(type="instruction", opcode="JMP", operand="shabi")
    location_c = memory_space(type="data", label="shabi", data="10")
    location_d = memory_space()
    location_e = memory_space(type="instruction", opcode="END")
    memory = [location_a, location_b, location_c, location_d, location_e]
    
    pc = 1
    acc = 0
    ix = 0
    compare = None
    error = "no_error"
    end = False
    addressL1 = None
    addressL2 = None
    number = None
    out = None
    opcode = memory[pc].opcode
    operand = memory[pc].operand
    label_addr = {"shabi":2}
    line_addr = {1:1, 2:2, 3:3, 4:4}
    current_address = pc

    print("PC {}\n\
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
error_content {}".format(*DirectAddressing(memory, 
    pc, 
    acc, 
    ix, 
    compare, 
    error, 
    end, 
    addressL1, 
    addressL2, 
    number, 
    out, 
    opcode, 
    operand, 
    label_addr,
    line_addr, 
    current_address)[1:]))