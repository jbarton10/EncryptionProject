import os
import sys
import string

def encode(uFile, offset):

    f = open(uFile, "r")
    encF = open("encryptedFile.txt", "w")
    alph = list(string.ascii_lowercase)

    for line in f:
        for letter in line:
            letter.lower()
            if letter not in alph:
                encF.write(letter)
            elif letter in alph:
                letterPos = alph.index(letter)
                letterPos +=  offset
                encLetter = alph[letterPos % len(alph)]
                #encLetter = alph[letterPos]
                encF.write(encLetter)
    
    f.close()
    encF.close()


def decode(uFile, offset):
    f = open(uFile, "r")
    decF = open("decryptedFile.txt", "w")
    alph = list(string.ascii_lowercase)
    
    for line in f:
        for letter in line:
            letter.lower()
            if letter not in alph:
                decF.write(letter)
            elif letter in alph:
                letterPos = alph.index(letter)
                letterPos -=  offset
                encLetter = alph[letterPos % len(alph)]
                #encLetter = alph[letterPos]
                decF.write(encLetter)
                

def checkFile(uFile):
    print(uFile)
    
    if os.path.isfile(uFile):
        print("looks good\n")
        True
    else:
        print("Please enter a valid file name, thank you.")
        sys.exit()

def main():
    print(string.ascii_letters)
    uInput = input("Would you like to encode or decode today?   ")

    if uInput.lower() == "encode":
        uFile = input("Please enter the file name you would like to encode:  ")
        checkFile(uFile)
        offset = int(input("Please enter the offset of the file to be encoded:  "))
        if type(offset) == int:
            encode(uFile, offset)
        else:
            print("Offset must be an integer\n")



    elif uInput.lower() == "decode":
        uFile = input("Please enter the file name you would like to decode:  ")
        checkFile(uFile)
        offset = int(input("Please enter the original offset of the file to be decoded:  "))
        if type(offset) == int:
            decode(uFile, offset)
        else:
            print("Offset must be an integer\n")


    else:
        print("Please enter encode or decode, thank you!")    

if __name__=="__main__": 
    main() 