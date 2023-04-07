def OperandTypeCheck (input_content):  

    #return "address" if content is "made of numbers only"
    #return "label" if content is "made of valid combination of characters"
    #otherwise returns the error
    if not AddressNumberCheck(input_content):
        if not LabelCheck(input_content):
            return "invalid_label_name"
        
        else:
            return "label"

    return "address"

# check if correct label, if False then invalid
def LabelCheck (label):

    # del with label with invalid characters
    invalid_chars = "0123456789:;<=>?@[\]^`{|}~!#$%^&*()\"\',./-"
    for char in label:
        if char in invalid_chars:
            return False

    return True

# check if valid address/number, if False then invalid
def AddressNumberCheck (address):
    
    if address[0] == "-":
        temp = list(address)
        temp.pop(0)
        address = "".join(temp)
    # address should be numbers only
    numbers = "0123456789"
    for chars in address:
        if not (chars in numbers):
            return False

    return True

# check a binary digit if it is valid.
def BinaryNumberCheck (number):
    if number[0] == "B" or number[0] == "b":
        number = RemoveB(number)
        if len(number) > 0:
            ValidNumbers = "01"
            for bit in number:
                if not (bit in ValidNumbers):
                    return False
        
        else:
            return False

        return True
    else:
        return False

# remove the beginning B letter
def RemoveB (binary):
    temp = list(binary)
    temp.pop(0)
    return "".join(temp)


# check if label in the list_to_address dictionary.

#main
if __name__ == "__main__":
    """import os
    print(os.path.dirname(__file__))
    #print(OperandTypeCheck("1999999"))"""
    
    """a = {"sb":666}
    try:
        print(a["jb"])
    except KeyError:
        print("SB")"""
    print(BinaryNumberCheck("B101056789"))
