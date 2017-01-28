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
    fin = open(args.file_in_name, 'rb')  # creates file in object with read binary mode
    fout = open(args.file_out_name, 'w')  # creates file out object
    bit_string = ""
    bin_num_nums = ""
    i = 0
    j = 0
    # byte = fin.read(1)  # read in one byte
    while i < 4:  # while there are bytes left in the 4 byte number
        byte = fin.read(1)  # read new byte
        byte = ord(byte)  # convert byte to int
        # print(byte)
        byte = bin(byte)[2:].rjust(8, '0')  # convert int to binary and discard leading 0b
        # print(byte)  # print for debugging
        bin_num_nums = byte + bin_num_nums
        i = i + 1
    # print(bin_num_nums)
    num_nums = bin2dec(len(bin_num_nums), bin_num_nums)
    print(num_nums)
    fout.write(str(num_nums) + '\n')
    while j < (num_nums):
        i = 0
        k = 0
        size = ""
        num = ""
        while i < 4:  # while there are bytes left in the 4 byte number
            byte = fin.read(1)  # read new byte
            byte = ord(byte)  # convert byte to int
            # print(byte)
            byte = bin(byte)[2:].rjust(8, '0')  # convert int to binary and discard leading 0b
            # print(byte)  # print for debugging
            size = byte + size
            i = i + 1
        size = bin2dec(len(size), size)
        while k < size:
            byte = fin.read(1)  # read new byte
            byte = ord(byte)  # convert byte to int
            # print(byte)
            byte = bin(byte)[2:].rjust(8, '0')  # convert int to binary and discard leading 0b
            # print(byte)  # print for debugging
            num = num + byte
            k = k + 1
        num = bin2hex(len(num), num)
        fout.write(str(size) + " " +  num + '\n')

if __name__ == '__main__':
    main()
