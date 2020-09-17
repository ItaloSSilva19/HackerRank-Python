def binary(n):
    pass

def octal(n):
    pass

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
