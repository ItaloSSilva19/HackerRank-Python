
def print_rangoli(n):
    import string
    alphabet = string.ascii_lowercase
    rangoli = []
    
    #Create half of the rangoli alphabet
    for i in range(n-1,-1,-1):
        if i == n-1:
            sequence = alphabet[i]
        else:
            sequence = alphabet[n-1:i:-1] + alphabet[i] + alphabet[i+1:n]
        rangoli.append(sequence)

            
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
