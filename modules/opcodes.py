class opcodes ():
    Opcodes = ["LDM", "LDR", "LDD", "LDI", "LDX", "MOV", "STO", "JMP", "CMP", "CMI", "JPE", "JPN", "ADD", "SUB", "INC", "DEC", "OUT", "END", "STX", "AND", "XOR", "OR", "LSL", "LSR", "STI", "STX"]
    Immediate_Opcodes = ["LDM", "LDR", "CMP", "ADD", "SUB", "AND", "XOR", "OR", "LSL", "LSR"]
    Direct_Opcodes = ["LDD", "STO", "JMP", "CMP", "JPE", "JPN", "ADD", "SUB", "AND", "XOR", "OR"]
    Indirect_Opcodes = ["LDI", "CMI", "STI"]
    Indexed_Opcodes = ["LDX", "STX"]
    Register_Opcodes = ["Mov", "INC", "DEC"]