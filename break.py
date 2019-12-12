# find png file scrpt
# by Zhou Enna (1002869)


import sys
import argparse
import string
import subprocess as sub


def shift(a):
    return (a-key)%256


def modify(filein,fileout):
    new_bytes = bytearray()

    # PROTIP: pythonic way
    #open binary file
    with open(filein, mode="rb") as fin_b:
        text_b = bytearray(fin_b.read())
        #print(text_b)
        for byte in text_b:
            new_byte = shift(byte)
            new_bytes.append(new_byte)

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

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    for key in range(256):
        modify(filein,fileout)
        check = sub.check_output(["File",fileout]).decode("utf-8")
        if("PNG" in check):
            print(check)
            break
    print(key)



    # all done
