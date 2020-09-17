def binary(n):
    binary_list= []
    result = n
    while result > 0:
        binary_list.append(result%2)
        result = result // 2
    string_bin = "" 
    for number in binary_list:
        string_bin +=str(number)   
    return "".join(string_bin[::-1])

def octal(n):
    octal_list= []
    result = n
    while result > 0:
        octal_list.append(result%8)
        result = result // 8
    string_octal = "" 
    for number in octal_list:
        string_octal +=str(number)   
    return "".join(string_octal[::-1])

def hexadec(n):
    hexadec_list= []
    result = n  

    while result > 0:
        remainder = result%16
        if remainder == 10:
            remainder = "A"
        elif remainder == 11:
            remainder = "B"
        elif remainder == 12:
            remainder = "C"            
        elif remainder == 13:
            remainder = "D" 
        elif remainder == 14:
            remainder = "E"
        elif remainder == 15:
            remainder = "F" 
        hexadec_list.append(remainder)
        result = result // 16

    string_hexadec = "" 
    for number in hexadec_list:
        string_hexadec +=str(number)
    return "".join(string_hexadec[::-1])

def print_formatted(number):
    for i in range(1,number+1):
        width = len(binary(number))
        dec =str(i).rjust(width, ' ')
        oc = octal(i).rjust(width, ' ')
        hx = hexadec(i).rjust(width, ' ')
        bn = binary(i).rjust(width, ' ')
        print(dec, oc, hx, bn)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
