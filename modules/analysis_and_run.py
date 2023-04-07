from .opcode_operations.immediate_addressing import *
from .opcode_operations.direct_addressing import *
from .opcode_operations.indirect_addressing import *
from .opcode_operations.indexed_addressing import *
from .opcode_operations.registers import *
from .opcodes import *

#from opcode_operations.immediate_addressing import *
#from opcode_operations.direct_addressing import *
#from opcode_operations.indirect_addressing import *
#from opcode_operations.indexed_addressing import *
#from opcode_operations.registers import *
#from opcodes import *

# main thread for analyse and run
def AnalysisAndRun (memory, pc, acc, ix, compare, label_addr, line_addr, current_address):

    # initialize all variables
    end = False
    mode = ""
    addressL1 = None
    addressL2 = None
    number = None
    out = ""
    opcode = ""
    operand = ""
    error = "no_error"
    label = ""
    error_content = ""

    if 1 <= current_address <= 511:
        this_memory_location = memory[current_address]

        # if current memory space is empty (None type)
        if memory[current_address].type == None:
            error = "empty_memory_space"
            error_content = "Address {}.\nCurrent memory space is empty, cannot read instruction or data.".format(current_address)
            
        # if current memory space is an instruction
        elif memory[current_address].type == "instruction":
            opcode = this_memory_location.opcode
            operand = this_memory_location.operand

            # check the validity of opcode
            if not (opcode in opcodes.opcodes):
                # Invalid Opcode
                error = "invalid_opcode"
                error_content = "Line {}, Address {}.\n\'{}\' is not a valid opcode.".format(line_addr[current_address], current_address, opcode)

            else:

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # OUT and END are opcodes with no operands, if operands exist then invalid
                if opcode == "OUT" or opcode == "END":
                    if operand != None:
                        error = "END/OUT_error"
                        error_content = "Line {}, Address {}.\n\'END\'&\'OUT\' opcodes do not need opcodes but opcodes find.".format(line_addr[current_address], current_address)
                    
                    # Deal with opcode out or end
                    else:
                        if opcode == "OUT":
                            out = acc

                        else:
                            end = True

                    pc += 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # Other opcodes
                else:
                    # these opcodes require only one opcode
                    if opcode == None:
                        error = "no_operand"
                        error_content = "Line {}, Address {}.\nOperand not found.".format(line_addr[current_address], current_address)

                    else:

                        # immediate addressing
                        if opcode in opcodes.immediate_opcodes and operand[0] == "#":
                            mode = "Immediate Addressing"

                            memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content = ImmediateAddressing(memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, line_addr, current_address)

                        # Direct addressing
                        elif opcode in opcodes.direct_opcodes:
                            mode = "Direct Addressing"

                            memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content = DirectAddressing(memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, label_addr, line_addr, current_address)
                        
                        # Indirect addressing
                        elif opcode in opcodes.indirect_opcodes:
                            mode = "Indirect Addressing"

                            memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content = IndirectAddressing(memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, label_addr, line_addr, current_address)

                        # Indexed addressing
                        elif opcode in opcodes.indexed_opcodes:
                            mode = "Indexed Addressing"

                            memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content = IndexedAddressing(memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, label_addr, line_addr, current_address)

                        # Registers
                        elif opcode in opcodes.register_opcodes:
                            mode = "Register opertation"

                            memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, error_content = Registers(memory, pc, acc, ix, compare, error, end, addressL1, addressL2, number, out, opcode, operand, line_addr, current_address)
                        
                        # opcode and operand can't be matched
                        else:
                            error = "invalid_use_opcode_operand"
                            error_content = "Line {}, Address {}.\nIncorrect usage of combinations of opcodes and operands.\ne.g. Immediate opcodes \'LDM\' should come with operand #<number> but \'#\' is not included.".format(line_addr[current_address], current_address)

    else:

        # case where the current address or the next PC is pointed to non exist in the memory.
        error = "address_out_of_range"
        error_content = "Line {} Current address \'{}\' is too big or too small.".format(line_addr[current_address], current_address)
    return memory, pc, acc, ix, compare, error, end, mode, addressL1, addressL2, number, out, opcode, operand, label, error_content

# testing
if __name__ == "__main__":
    #from .file_open import *
    import time
    from file_open import *

    memory, label_addr, line_addr, pc = OpenFile()

    print(memory, label_addr, line_addr, pc)

    if memory != None:
        acc = 0
        ix = 0
        compare = None
        error = "no_error"
        error_content = ""
        end = False

        while end == False and error == "no_error":
            current_address = pc
            memory, pc, acc, ix, compare, error, end, mode, addressL1, addressL2, number, out, opcode, operand, label, error_content = AnalysisAndRun(memory, pc, acc, ix, compare, label_addr, line_addr, current_address)
            print("CurrentAddress {}\n\
PC {}\n\
ACC {}\n\
IX {}\n\
Compare {}\n\
error {}\n\
end {}\n\
Mode {}\n\
AddressL1 {}\n\
AddressL2 {}\n\
Number {}\n\
Out {}\n\
Opcode {}\n\
Operand {}\n\
label {}\n\
Error_Content {}".format(current_address,
            pc, 
            acc, 
            ix, 
            compare, 
            error, 
            end, 
            mode, 
            addressL1, 
            addressL2, 
            number, 
            out, 
            opcode, 
            operand, 
            label,
            error_content))
            time.sleep(0.5)
    
    end_state = "NO ERROR" if error == "no_error" else error + " ERROR"
    print("The process ends with {}, please continue".format(end_state))
