CHAR_INT_START = 3
SPECIAL_CHARS_SIZE = 5
SPECIAL_CHARS = [' ', '\"', ',', '.', '\'']

def make_upper(input): #Converts all of the English alphabet characters in the input to uppercase
    temp = ""
    for c in input:
        t = ord(c)
        if 'a' <= c and c <= 'z':
            t -= ord('a')
            t += ord('A')
        temp += chr(t)
    return temp

def binpow(c, e, mod): #Calculates c^e (mod mod):
    c %= mod
    res = 1
    while e > 0:
        if e & 1:
            res = res * c % mod
        c = c * c % mod
        e >>= 1
    return res

def encrypt(message, e, n):
    charToInt = get_table()

    encrypted = ""
    for c in message:
        encrypted += chr(charToInt[c])
    temp = ""
    for c in encrypted:
        temp += chr(binpow(ord(c), e, n))
    encrypted = temp
    return encrypted

def get_table():
    charToInt = {}
    charInt = CHAR_INT_START
    c = 'A'
    while c <= 'Z':
        charToInt[c] = charInt
        charInt += 1
        c = chr(ord(c) + 1)
    for i in range(SPECIAL_CHARS_SIZE):
        charToInt[SPECIAL_CHARS[i]] = charInt
        charInt += 1
    return charToInt

def gen(e, n, CIS, message):
    global CHAR_INT_START
    CHAR_INT_START = CIS
    temp = ""
    for c in message:
        if c == '*':
            temp += '\"'
        elif c == '^':
            temp += '\''
        else:
            temp += c
    message = temp

    message = make_upper(message)
    encrypted = encrypt(message, e, n)
    output = str(e) + " " + str(n) + "\n"
    output += str(len(encrypted)) + "\n"
    for i in encrypted:
        output += str(ord(i)) + ' '
    output += "\n"

    return output

