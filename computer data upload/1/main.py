import random

true = True
false = False
debug = false

in_str = ""
out_str = ""

charstring = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?"
keyList = []


# above is 94 chars long

# assumption is that key transfer is 100% secure


def getCharIndex(character):
    for i in range(len(charstring)):
        if character == charstring[i]:
            return i
    print("somethings wrong with getCharIndex()")


def shuffleCharIndex():
    pass


def encrypt(string_in):
    out = []
    for i in range(len(string_in)):
        randByte = random.getrandbits(8)
        keyList.append(randByte)
        to_ret = getCharIndex(string_in[i]) ^ randByte
        out.append(to_ret)
    return out


def decrypt(string_in):
    out = ""
    for i in range(len(string_in)):
        key = keyList[i]
        toDecrypt = string_in[i]
        toRet = toDecrypt ^ key
        out = out + str(charstring[toRet])
    return out


def report(string):
    to_encrypt = str(string)
    encrypted = encrypt(to_encrypt)
    decrypted = decrypt(encrypted)

    print("start txt: " + str(to_encrypt))
    print("encrypted: " + str(encrypted))
    print("keys list: " + str(keyList))
    print("decrypted: " + str(decrypted))


while true:
    keyList = []
    report(input("input to be encrypted:\n"))
