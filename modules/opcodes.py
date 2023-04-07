# collection/classification of several supported opcodes
class opcodes ():
    opcodes = ["LDM", "LDR", "LDD", "LDI", "LDX", "MOV", "STO", "JMP", "CMP", "CMI", "JPE", "JPN", "ADD", "SUB", "INC", "DEC", "OUT", "END", "STX", "AND", "XOR", "OR", "LSL", "LSR", "STI", "STX"]
    immediate_opcodes = ["LDM", "LDR", "CMP", "ADD", "SUB", "AND", "XOR", "OR", "LSL", "LSR"]
    direct_opcodes = ["LDD", "STO", "JMP", "CMP", "JPE", "JPN", "ADD", "SUB", "AND", "XOR", "OR"]
    indirect_opcodes = ["LDI", "CMI", "STI"]
    indexed_opcodes = ["LDX", "STX"]
    register_opcodes = ["Mov", "INC", "DEC"]