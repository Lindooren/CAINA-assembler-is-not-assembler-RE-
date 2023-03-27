# ****** main convertion
def BitWiseLogicalOperation (ACC, number, opcode):
    ACC = BinaryConvertion(ACC)
    ACC, number = LengthAlignment(ACC, number)
    
    ResultBits = ""
    
    # select correct operation according to opcode
    if opcode == "AND":
        for i in range(len(ACC)):
            ResultBits += AND_Operation(ACC[i], number[i])

    elif opcode == "OR":
        for i in range(len(ACC)):
            ResultBits += OR_Operation(ACC[i], number[i])

    elif opcode == "XOR":
        for i in range(len(ACC)):
            ResultBits += XOR_Operation(ACC[i], number[i])

    return DenaryConvertion(ResultBits)

# convert value to binary number
def BinaryConvertion (value):
    Binary = "0" + bin(value).split("b")[1]
    if value < 0:

        # one's complement operation
        BinaryList = list(Binary)
        for i in range(len(BinaryList)):
            if BinaryList[i] == "0":
                BinaryList[i] = "1"

            else:
                BinaryList[i] = "0"

        # two's complement operation
        Carry = 1
        for i in range(-1, -1 - len(BinaryList), -1):
            Result = int(BinaryList[i]) + Carry
            if Result <= 1:
                Carry = 0

            else:
                Result = 0
                Carry = 1
            
            BinaryList[i] = str(Result)
            
        Binary = "".join(BinaryList)

    return Binary

# convert binary string to a denary
def DenaryConvertion (binary_str):
    Denary = 0
    Exponent = 0
    for i in range(-1, -1 - len(binary_str), -1):
        BitVal = int(binary_str[i]) * (2 ** Exponent)

        # treatment for sign bit 1
        if i == (0 - len(binary_str)) and binary_str[i] == "1":
            BitVal = 0 - BitVal

        Exponent += 1
        Denary += BitVal

    return Denary

# make the two values' length into same length
def LengthAlignment (ACC, number):
    if len(ACC) > len(number):
        NumBits = len(ACC) - len(number)
        number = AlignmentAppliance(number, NumBits)

    else:
        NumBits = len(number) - len(ACC)
        ACC = AlignmentAppliance(ACC, NumBits)

    return ACC, number

    
# make the length same.
def AlignmentAppliance (value, num_bits):
    if value[0] == "0":
        value = "0" * num_bits + value

    else:
        value = "1" * num_bits + value

    return value

# AND
def AND_Operation (bit_one, bit_two):
    if bit_one == "1" and bit_two == "1":
        return "1"

    else:
        return "0"

# OR
def OR_Operation (bit_one, bit_two):
    if bit_one == "0" and bit_two == "0":
        return "0"

    else:
        return "1"

# XOR
def XOR_Operation (bit_one, bit_two):
    if bit_one == bit_two:
        return "0"

    else:
        return "1"

# Bits shifting
def BitsShifting (ACC, num_places, opcode):
    BinaryVal = BinaryConvertion(ACC)
    for i in range(num_places):
        if opcode == "LSL":
            BinaryVal = BinaryVal[1:] + "0"

        else:
            BinaryVal = "0" + BinaryVal[::-1][1:][::-1]

    return DenaryConvertion(BinaryVal)


# main
if __name__ == "__main__":
    #print(BitWiseLogicalOperation(4, "0010", "OR"))
    print(BitsShifting(127, 4, "LSR"))