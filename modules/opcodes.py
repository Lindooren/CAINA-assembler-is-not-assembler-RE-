class opcodes ():
    Opcodes = ["LDM", "LDR", "LDD", "LDI", "LDX", "MOV", "STO", "JMP", "CMP", "CMI", "JPE", "JPN", "ADD", "SUB", "INC", "DEC", "OUT", "END", "STX"]
    Immediate_Opcodes = ["LDM", "LDR", "CMP", "ADD", "SUB"]
    Direct_Opcodes = ["LDD", "STO", "JMP", "CMP", "JPE", "JPN", "ADD", "SUB"]
    Indirect_Opcodes = ["LDI", "CMI"]
    Indexed_Opcodes = ["LDX", "STX"]
    Register_Opcodes = ["Mov", "INC", "DEC"]