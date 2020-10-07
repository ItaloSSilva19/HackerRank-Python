def minion_game(string):
    vowel = 'AEIOU'
    kevin = 0
    stuart = 0
    length_string = len(string)
    for i in range(length_string):
        if string[i] in vowel:
            kevin += length_string
        else:
            stuart += length_string
        length_string -= 1
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Stuart", stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)
