# define a class that represents the memory space in the memory
class memory_space ():
    def __init__(self, type = None, label = None, opcode = None, operand = None, data = None) -> None:
        self.type = type
        self.label = label
        self.opcode = opcode
        self.operand = operand
        self.data = data
    
