#from type_check import *
#from bitwise import *

from .type_check import *
from .bitwise import *

def ImmediateAddressing (memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, line_addr, current_address):
    error_content = ""

    # remove # in the beginning of operand
    temp = list(operand)
    temp.pop(0)
    temp2 = "".join(temp)

    # selection
    if opcode in ["LDM", "LDR", "CMP", "ADD", "SUB"]:

        # correct address/number format?
        if not AddressNumberCheck(temp2):
            error = "invalid_number"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid number".format(line_addr[current_address], current_address, temp2)
        
        else:
            number = int(temp2)
            if opcode == "LDM":
                acc = number

            elif opcode == "LDR":
                ix = number

            elif opcode == "CMP":
                compare = True if acc == number else False

            elif opcode == "ADD":
                acc = acc + number

            elif opcode == "SUB":
                acc = acc - number

    elif opcode in ["AND", "OR", "XOR"]:
        number = temp2

        # check if this binary is valid
        if BinaryNumberCheck(number):

            # remove the heading B and store it to ACC
            bin_val = RemoveB(number)
            acc = BitWiseLogicalOperation(acc, bin_val, opcode)

        else:
            error = "invalid_binary_number"
            error_content = "Line {}, Address{}.\n\'{}\' is not a valid binary number".format(line_addr[current_address], current_address, number)

    elif opcode in ["LSL", "LSR"]:
        if not AddressNumberCheck(temp2):
            error = "invalid_number"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid number".format(line_addr[current_address], current_address, temp2)
        
        else:
            num_places = int(temp2)
            if num_places < 0:
                error = "invalid_number_of_places_of_bit_shifting"
                error_content = "Line {}, Address {}.\n\'{}\' is not a valid number of places of bit shifting number".format(line_addr[current_address], current_address, num_places)
            
            else:
                # bits shifting
                acc = BitsShifting(acc, num_places, opcode)

    pc = pc + 1

    return memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content

# testing
if __name__ == "__main__":
    from memory_space import *

    location_a = memory_space()
    location_b = memory_space(type="instruction", opcode="LSR", operand="#lasdjfklakljsdf")
    location_c = memory_space()
    memory = [location_a, location_b, location_c]
    
    pc = 1
    acc = 8
    ix = 0
    compare = False
    error = "no_error"
    end = False
    addressL1 = None
    addressL2 = None
    number = None
    out = None
    opcode = memory[pc].opcode
    operand = memory[pc].operand
    line_addr = {1:1}
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
error_content {}".format(*ImmediateAddressing(memory, 
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
    line_addr, 
    current_address)[1:]))