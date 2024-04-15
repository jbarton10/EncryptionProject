import os
import sys

def encode(uFile, offset):
    return


def decode(uFile, offset):
    return

def checkFile(uFile):
    print(uFile)
    
    if os.path.isfile(uFile):
        print("looks good")
        True
    else:
        print("Please enter a valid file name, thank you.")
        sys.exit()

def main():
    uInput = input("Would you like to encode or decode today?   ")

    if uInput.lower() == "encode":
        uFile = input("Please enter the file name you would like to encode:  ")
        checkFile(uFile)
        offset = input("Please enter the offset of the file to be encoded:  ")
        encode(uFile, offset)
    elif uInput.lower() == "decode":
        uFile = input("Please enter the file name you would like to deocde:  ")
        checkFile(uFile)
        decode(uFile, offset)
    else:
        print("Please enter encode or decode, thank you!")    

if __name__=="__main__": 
    main() 