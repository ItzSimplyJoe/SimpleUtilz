def RGB_to_colour(value):
    '''Converts RGB value to a colour string'''
    denaryValue = convert_value_to_denary(value, "rgb")
    colour = Binary_search(denaryValue)
    return colour

def hex_to_colour(value):
    '''Converts hex value to a colour string'''
    denaryValue = convert_value_to_denary(value, "hex")
    colour = Binary_search(denaryValue)
    return colour
    
def RGBA_to_colour(value):
    '''Converts RGBA value to a colour string'''
    denaryValue = convert_value_to_denary(value, "rgba")
    colour = Binary_search(denaryValue)
    return colour

def binary_to_colour(value):
    '''Converts binary value to a colour string'''
    denaryValue = convert_value_to_denary(value, "binary")
    colour = Binary_search(denaryValue)
    return colour

def convert_value_to_denary(value, whatFormat):
    '''Converts a value to denary'''
    if whatFormat == "hex":
        if "#" in value:
            hexWithoutHashTag = value.replace("#","")
        else:
            hexWithoutHashTag = value
        hexWithoutHashTag = hexWithoutHashTag.upper()
        denaryValue = int(hexWithoutHashTag, 16)
    elif whatFormat == "rgb":
        if "(" in value:
            rgbWithoutBrackets = value.replace("(","")
            rgbWithoutBrackets = rgbWithoutBrackets.replace(")","")
        else:
            rgbWithoutBrackets = value
        rgbWithoutBrackets = rgbWithoutBrackets.split(",")
        hexValue = '{:02x}{:02x}{:02x}'.format(int(rgbWithoutBrackets[0]), int(rgbWithoutBrackets[1]), int(rgbWithoutBrackets[2]))
        denaryValue = int(hexValue, 16)
    elif whatFormat == "rgba":
        if "(" in value:
            rgbWithoutBrackets = value.replace("(","")
            rgbWithoutBrackets = rgbWithoutBrackets.replace(")","")
        else:
            rgbWithoutBrackets = value
        rgbWithoutBrackets = rgbWithoutBrackets.split(",")
        hexValue = '{:02x}{:02x}{:02x}{:02x}'.format(int(rgbWithoutBrackets[0]), int(rgbWithoutBrackets[1]), int(rgbWithoutBrackets[2]), int(rgbWithoutBrackets[3]))
        denaryValue = int(hexValue, 16)
    elif whatFormat == "binary":
        if "0b" in value:
            binaryWithout0b = value.replace("0b","")
        else:
            binaryWithout0b = value
        denaryValue = int(binaryWithout0b, 2)
    else:
        print("Not a valid format")
        
    return denaryValue    
    
def Binary_search(value):
    '''Binary search to find the colour in the dataset'''
    with open("simpleColours.csv", "r") as file:
        lines = file.readlines()
    
    low = 0
    high = len(lines) - 1

    while low <= high:
        mid = (low + high) // 2
        line = lines[mid].split(',')[0]

        if int(line) == int(value):
            return lines[mid].split(',')[1]
        elif int(line) < int(value):
            low = mid + 1
        else:
            high = mid - 1
    
    upperValue = lines[mid + 1].split(',')[0]
    lowerValue = lines[mid - 1].split(',')[0]
    if (int(upperValue) - int(mid)) > (int(mid) - int(lowerValue)):
        return lines[mid].split(',')[1]
    else:
        return lines[mid+2].split(',')[1]    