import base64

str_data = ''

def BinaryToDecimal(binary):
    decimal = int(binary, 2)
    return decimal

def main():
    # base 64 to binary
    with open('input.txt', 'r') as f:
        data = f.read()
    bin_data = base64.b64decode(data)
    # binary to ascii
    
    delim = 0 #delimiter  
    hex_data = '' 
    for i in range(0, len(bin_data), 8):
        byte = bin_data[i:i+8]
        decimal = BinaryToDecimal(byte)
        if delim % 2 == 0:
            pass
        else:
            hex_data += chr(decimal) 
        delim += 1

    #dec to ascii
    ascii_data = ''
    i = 0
    while(i < len(hex_data)):
        dec_num = int(hex_data[i] + hex_data[i+1])   # separate 2 digits
        if((dec_num >= 48 and dec_num <= 57) or (dec_num >= 65 and dec_num <= 90) or (dec_num >= 97 and dec_num <= 122)):  # check if it is a readable character    
            ascii_data += chr(dec_num)
            i += 2
        else:
            dec_num = int(hex_data[i] + hex_data[i+1] + hex_data[i+2]) # separate 3 digits
            ascii_data += chr(dec_num)
            i += 3

    #rot13
    rot13_data = ''
    for i in ascii_data:
        if i.isalpha():
            if i.isupper():
                rot13_data += chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
            else:
                rot13_data += chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_data += i

    #flag here
    flag = base64.b64decode(rot13_data)
    print(flag)



if __name__ == '__main__':
    main()