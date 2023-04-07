#from type_check import *

from .type_check import *

def IndexedAddressing (memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, label_addr, line_addr, current_address):
    error_content = ""

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
            error_content = "Line {}, Address {}.\nCannot find level 1 address(base address) corresponds to label \'{}\'.".format(line_addr[current_address], current_address, operand)

        else:
            
            # add index to the base address and get the result
            indexed_addr = addressL1 + ix

            # check range (indexed)
            if not (1 <= indexed_addr <= len(memory) - 1):
                error = "indexed_address_out_of_range"
                error_content = "Line {}, Address {}.\nIndexed address \'{}\' is too big or too small.".format(line_addr[current_address], current_address, indexed_addr)

            else:
                indexed_address_location = memory[indexed_addr]

                if opcode in ["LDX"]:
                    if indexed_address_location.type == "data":
                        try:
                            number = int(indexed_address_location.data)

                            #selection
                            if opcode == "LDX":
                                acc = number

                        except ValueError:
                            error = "invalid_data_indexed_address"
                            error_content = "Line {}, Address {}.\n\Line {}, Indexed address {}.\nThe data \'{}\' under indexed address is invalid.".format(line_addr[current_address], current_address, line_addr[indexed_addr], indexed_addr, indexed_address_location.data)
                    
                    else:
                        error = "invalid_indexed_address_content_type"
                        error_content = "Line {}, Address {}.\nLine {}, Indexed address {}.\nThe required memory lcoation at this indexed address should be \'data\' but currently the type is \'{}\'".format(line_addr[current_address], current_address,line_addr[indexed_addr], indexed_addr, indexed_address_location.type)
                
                elif opcode in ["STX"]:
                    if opcode == "STX":
                        memory[indexed_addr].type = "data"
                        memory[indexed_addr].opcode, memory[indexed_addr].operand = None, None
                        memory[indexed_addr].data = str(acc)

                pc = pc + 1

    return memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content

#testing
if __name__ == "__main__":
    
    from memory_space import *

    location_a = memory_space()
    location_b = memory_space(type="instruction", label="jiba", opcode="LDX", operand="shabi")
    location_c = memory_space(type="data", label="shabi", data="sdfgh")
    location_d = memory_space()
    location_e = memory_space()
    memory = [location_a, location_b, location_c, location_d, location_e]
    
    pc = 1
    acc = 1
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
    label_addr = {"jiba":1, "shabi":2}
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
Error Content {}".format(*IndexedAddressing(memory, 
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

    