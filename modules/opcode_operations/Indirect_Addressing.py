#from type_check import *
from .type_check import *

def IndirectAddressing (memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, label_addr, line_addr, current_address):
    error_content = ""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # check the type of operand. (L1)(一级地址)
    result = OperandTypeCheck(operand)
    if result == "invalid_label_name":
        error = result
        error_content = "Line {}, Address {}.\n\'{}\' is not a valid label.".format(line_addr[current_address], current_address, operand)
    
    else:
        try:

            # search the label in the dictionary (L1)
            if result == "label":
                addressL1 = label_addr[operand]

            else:
                addressL1 = int(operand)
            
        except KeyError:
            error = "label_not_found_L1_address"
            error_content = "Line {}, Address {}.\nCannot find level 1 address corresponds to label \'{}\'.".format(line_addr[current_address], current_address, operand)

        else:

            # check range (L1)
            if not (1 <= addressL1 <= len(memory) - 1):
                error = "L1_address_out_of_range"
                error_content = "Line {}, Address {}.\nLevel 1 address \'{}\' is too big or too small.".format(line_addr[current_address], current_address, addressL1)

            else:
                # get the content from AddressL1
                addressL1_location = memory[addressL1]
                if addressL1_location.type == "data":

                    # check the type of content (L2)(二级地址)
                    result = OperandTypeCheck(addressL1_location.data)
                    if result == "invalid_label_name":
                        error = result
                        error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\n\'{}\' is not a valid label.".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, addressL1_location.data)

                    else:
                        try:

                            # search the label in the dictionary (L2)
                            if result == "label":
                                addressL2 = label_addr[addressL1_location.data]

                            else:
                                addressL2 = int(addressL1_location.data)

                        except KeyError:
                            error = "label_not_found_L2_address"
                            error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nCannot find level 2 address corresponds to label \'{}\'.".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, addressL1_location.data)

                        else:

                            # check range (L2)
                            if not (1 <= addressL2 <= len(memory) - 1):
                                error = "L2_address_out_of_range"
                                error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nLevel 2 address \'{}\' is too big or too small.".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, addressL2)

                            else:
                                addressL2_location = memory[addressL2]
                                if addressL2_location.type == "data":
                                    try:
                                        if not (opcode in ["STI"]):
                                            number = int(addressL2_location.data) 
                                                
                                        # selection
                                        if opcode == "LDI":
                                            acc = number

                                        elif opcode == "CMI":
                                            compare = True if acc == number else False

                                        elif opcode == "STI":
                                            memory[addressL2].type = "data"
                                            memory[addressL2].opcode, memory[addressL2].operand = None, None
                                            memory[addressL2].data = str(acc)

                                        pc = pc + 1
                                    
                                    except ValueError:
                                        error = "invalid_data_L2_address"
                                        error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nLine {}, Level 2 address {}.\nThe data \'{}\' under level 2 address is invalid.".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, line_addr[addressL2], addressL2, addressL2_location.data)

                                else:
                                    error = "invalid_L2_address_content_type"
                                    error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nLine {}, Level 2 address {}.\nTThe required memory lcoation at this level 1 address should be \'data\' but currently the type is \'{}\'".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, line_addr[addressL2], addressL2, addressL2_location.type)

                else:
                    error = "invalid_L1_address_content_type"
                    error_content = "Line {}, Address {}.\nLine {}, Level 1 address {}.\nThe required memory lcoation at this level 1 address should be \'data\' but currently the type is \'{}\'".format(line_addr[current_address], current_address, line_addr[addressL1], addressL1, addressL1_location.type)

    return memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content

#testing
if __name__ == "__main__":
    from memory_space import *

    location_a = memory_space()
    location_b = memory_space(type="instruction", opcode="STI", operand="2")
    location_c = memory_space(type="data", label="shabi", data="zhizhang")
    location_d = memory_space(type="data", label="zhizhang", data="0")
    location_e = memory_space(type="instruction", opcode="END")
    memory = [location_a, location_b, location_c, location_d, location_e]
    
    pc = 1
    acc = 10
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
    label_addr = {"shabi":2, "zhizhang":3}
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
error_content {}".format(*IndirectAddressing(memory, 
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