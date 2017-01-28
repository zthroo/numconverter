import math
import argparse


def bin2dec(length, num_str):  # converts binary to decimal
    num = 0
    for index in range(length):
        num = num + (2 ** (length - index - 1)) * int(num_str[index])
    return num


def bin2hex(length, num_string):
    offset = 4 - length % 4  # determine how many 0s needed to make the string length evenly divisible by 4
    if length < 4:
        for i in range(4 - length):  # add 0s
            num_string = "0" + num_string
    else:
        for i in range(offset):  # add 0s
            num_string = "0" + num_string
    num_list = []
    for i in range((math.floor(len(num_string) / 4))):  # convert string into list of 4 bit nibble
        num_list.append(num_string[i * 4] + num_string[i * 4 + 1] + num_string[i * 4 + 2] + num_string[i * 4 + 3])
    # print(num_list)
    for i in range(len(num_list)):  # convert cells to decimal numbers
        num_list[i] = bin2dec(4, num_list[i])
    for i in range(len(num_list)):  # convert decimals to hex representation
        if num_list[i] == 10:
            num_list[i] = "A"
        if num_list[i] == 11:
            num_list[i] = "B"
        if num_list[i] == 12:
            num_list[i] = "C"
        if num_list[i] == 13:
            num_list[i] = "D"
        if num_list[i] == 14:
            num_list[i] = "E"
        if num_list[i] == 15:
            num_list[i] = "F"

    ans_string = "0x"
    for cell in num_list:  # runs through num_list, adding the hex characters to the answer string
        ans_string = ans_string + str(cell)
    return ans_string


def main():
    parser = argparse.ArgumentParser()  # create argument parser
    parser.add_argument("-fi", "--file_in_name", help="name of the file to take in")  # adds file in name argument
    parser.add_argument("-fo", "--file_out_name", help="name of the file to produce")  # adds file out name  argument
    args = parser.parse_args()  # parse the arguments
    fout = open(args.file_out_name, 'w')  # creates file out object
    with open(args.file_in_name, 'rb') as fin:  # creates file in object with read binary mode
        byte = fin.read(1)
        while byte:
            byte = ord(byte)
            byte = bin(byte)[2:].rjust(8, '0')
            print (byte)
            byte = fin.read(1)
    #num_nums = bin2dec(4, str(fstring[0:3]))


if __name__ == '__main__':
    main()
