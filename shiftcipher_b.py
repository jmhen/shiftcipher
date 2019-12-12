# binary shiftcipher script
# by Zhou Enna (1002869)



import sys
import argparse
import string

def shift(a,e):
    if(e == "e" or e == "E"):
        return (a+key)%256
    elif(e == "d" or e == "D"):
        return (a-key)%256
    else:
        raise Exception("invalid mode!")
    return "e"


def modify(filein,fileout,mode):
    new_bytes = bytearray()

    # PROTIP: pythonic way
    #open binary file
    with open(filein, mode="rb") as fin_b:
        text_b = bytearray(fin_b.read())
        #print(text_b)
        for byte in text_b:
            new_byte = shift(byte,mode)
            new_bytes.append(new_byte)

        print("finish shifting!")
        fout_b = open(fileout, mode='wb')      # write mode
        fout_b.write(new_bytes)
        fin_b.close()
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
    if(int(args.key)>=0 and int(args.key)<=255):
        key = int(args.key)
    else:
        raise Exception("the key is not in the range")
    if(args.mode!="e" and args.mode !="d" and args.mode !="E" and args.mode !="D"):
        raise Exception("the mode is not valid")
    mode = args.mode

    modify(filein,fileout,mode)

    # all done
