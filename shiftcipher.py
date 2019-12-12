# printable character shiftcipher script
# by Zhou Enna (1002869)


import sys
import argparse
import string

def shift(a,e):

    length = len(string.printable)
    e_new_pos= string.printable.index(a)+key
    d_new_pos = string.printable.index(a)-key
    if(a == " "):
        return " "
    if(e == "e" or e == "E"):
            sub = string.printable[e_new_pos%length]
    elif(e == "d" or e == "D"):
            sub = string.printable[d_new_pos%length]
    return sub


def modify(filein,fileout,mode):
    newtext = ""

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        text = fin.read()
        for character in text:
            new_char = shift(character,mode)
            newtext = newtext + new_char

        print("finish shifting!")
        fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
        fout.write(newtext)
        fin.close()
        # file will be closed automatically when interpreter reaches end of the block


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='number to shift')
    parser.add_argument('-m', dest='mode', help='e or d mode')
    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    if(int(args.key)>=1 and int(args.key)<len(string.printable)-1):
        key = int(args.key)
    else:
        raise Exception("the key is not in the range")
    if(args.mode!="e" and args.mode !="d" and args.mode !="E" and args.mode !="D"):
        raise Exception("the mode is not valid")
    mode = args.mode

    modify(filein,fileout,mode)

    # all done
