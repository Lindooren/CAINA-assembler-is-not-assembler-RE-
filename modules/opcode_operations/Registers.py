def Registers (memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, line_addr, current_address):
    error_content = ""
    
    if opcode == "MOV":
        if operand == "IX":
            ix = acc

        else:
            error = "invalid_register"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid register for opcode \'{}\'.".format(line_addr[current_address], current_address, operand, opcode)

    elif opcode == "INC":
        if operand == "ACC":
            acc += 1

        elif operand == "IX":
            ix += 1

        else:
            error = "invalid_register"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid register for opcode \'{}\'.".format(line_addr[current_address], current_address, operand, opcode)

    elif opcode == "DEC":
        if operand == "ACC":
            acc -= 1

        elif operand == "IX":
            ix -= 1

        else:
            error = "invalid_register"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid register for opcode \'{}\'.".format(line_addr[current_address], current_address, operand, opcode)

    pc += 1

    return memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content

#testing
if __name__ == "__main__":
    from memory_space import *

    location_a = memory_space()
    location_b = memory_space(type="instruction", opcode="MOV", operand="ACC")
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
Error Content {}".format(*Registers(memory, 
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