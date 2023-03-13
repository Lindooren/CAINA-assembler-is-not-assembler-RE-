from .opcode_operations.Immediate_Addressing import *
from .opcode_operations.Direct_Addressing import *
from .opcode_operations.Indirect_Addressing import *
from .opcode_operations.Indexed_Addressing import *
from .opcode_operations.Registers import *
from .opcodes import *

# main thread for analyse and run
def AnalysisAndRun (memory, PC, ACC, IX, Compare, label_addr, line_addr, CurrentAddress):

    # initialize all variables
    end = False
    Mode = ""
    AddressL1 = None
    AddressL2 = None
    Number = None
    Out = ""
    Opcode = ""
    Operand = ""
    error = "no_error"
    label = ""
    error_content = ""
    
    label = memory[PC][0]
    Instruction = memory[PC][1]

    if memory[PC] == [None, None]:
        error = "empty_memory_space"
        error_content = "Address {}.\nCurrent memory space is empty, cannot read instruction or data.".format(CurrentAddress)
        
       
    else:
        label = memory[PC][0]
        Instruction = memory[PC][1].split(" ")
        Opcode = Instruction[0]

        # check presence
        if not (Opcode in opcodes.Opcodes):
            # Invalid Opcode
            error = "invalid_opcode"
            error_content = "Line {}, Address {}.\n\'{}\' is not a valid opcode.".format(line_addr[CurrentAddress], CurrentAddress, Opcode)

        else:

#---------------------------------------------------------------------------------------------------------------------------
            # OUT and END are opcodes with no operands, if operands exist then invalid
            if Opcode == "OUT" or Opcode == "END":
                if len(Instruction) > 1:
                    error = "END/OUT_error"
                    error_content = "Line {}, Address {}.\n\'END\'&\'OUT\' opcodes do not need opcodes but opcodes find.".format(line_addr[CurrentAddress], CurrentAddress)
                
                # Deal with opcode out or end
                else:
                    if Opcode == "OUT":
                        Out = ACC

                    else:
                        end = True

                PC += 1

#---------------------------------------------------------------------------------------------------------------------------
            # Other opcodes
            else:
                # these opcodes require only one opcode
                if len(Instruction) <= 1:
                    error = "no_operand"
                    error_content = "Line {}, Address {}.\nOperand not found.".format(line_addr[CurrentAddress], CurrentAddress)

                else:
                    Operand = Instruction[1]

                    # immediate addressing "LDM", "LDR", "CMP", "ADD", "SUB"
                    if Opcode in opcodes.Immediate_Opcodes and Operand[0] == "#":
                        Mode = "Immediate Addressing"

                        memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content = ImmediateAddressing(memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, line_addr, CurrentAddress)

                    # Direct addressing "LDD", "STO", "JMP", "CMP", "JPE", "JPN", "ADD", "SUB"
                    elif Opcode in opcodes.Direct_Opcodes:
                        Mode = "Direct Addressing"

                        memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content = DirectAddressing(memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, label_addr, line_addr, CurrentAddress)
                    
                    # Indirect addressing "LDI", "CMI"
                    elif Opcode in opcodes.Indirect_Opcodes:
                        Mode = "Indirect Addressing"

                        memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content = IndirectAddressing(memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, label_addr, line_addr, CurrentAddress)

                    # Indexed addressing "LDX"
                    elif Opcode in opcodes.Indexed_Opcodes:
                        Mode = "Indexed Addressing"

                        memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content = IndexedAddressing(memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, label_addr, line_addr, CurrentAddress)

                    #registers
                    elif Opcode in opcodes.Register_Opcodes:
                        Mode = "Register opertation"

                        memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, error_content = Registers(memory, PC, ACC, IX, Compare, error, end, AddressL1, AddressL2, Number, Out, Opcode, Operand, line_addr, CurrentAddress)
                    
                    else:
                        error = "invalid_use_opcode_operand"
                        error_content = "Line {}, Address {}.\nIncorrect usage of combinations of opcodes and operands.\ne.g. Immediate opcodes \'LDM\' should come with operand #<number> but \'#\' is not included.".format(line_addr[CurrentAddress], CurrentAddress)

    return memory, PC, ACC, IX, Compare, error, end, Mode, AddressL1, AddressL2, Number, Out, Opcode, Operand, label, error_content

# testing
if __name__ == "__main__":
    from .file_open import *

    """
    memory = [[None, None], 
    ['start', 'LDD A'], 
    [None, 'INC ACC'], 
    [None, 'STO A'], 
    [None, 'CMP #90'], 
    [None, 'JPN start'], 
    [None, 'LDM #66'],
    [None, 'OUT'],
    [None, 'END'], 
    ['A', '66']]

    label_addr = {'start': 1, 'A': 9}
    """

    memory, label_addr, PC = open_file()

    print(memory, label_addr, PC)

    if memory != None:
        ACC = 0
        IX = 0
        Compare = None
        error = "no_error"
        end = False

        while end == False and error == "no_error":
            memory, PC, ACC, IX, Compare, error, end, Mode, AddressL1, AddressL2, Number, Out, Opcode, Operand, label = AnalysisAndRun(memory, PC, ACC, IX, Compare, label_addr)
            print("PC {}\n\
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
        label {}".format(PC, 
    ACC, 
    IX, 
    Compare, 
    error, 
    end, 
    Mode, 
    AddressL1, 
    AddressL2, 
    Number, 
    Out, 
    Opcode, 
    Operand, 
    label))
