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
    pass

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
