import math
import argparse


def bin2dec(length, num_str):  # converts binary to decimal
    num = 0
    for index in range(length):
        num = num + (2 ** (length - index - 1)) * int(num_str[index])
    return num


# converts binary to hexadecimal
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


# converts hexadecimal to binary
def hex2bin(length, num_str):
    list(num_str)  # convert num_string to list
    num_str = num_str[2:]  # pop off the 0x
    # dict to convert between the hex char and the binary string
    hex_dict = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110",
                '7': "0111", '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101",
                'E': "1110", 'F': "1111", '\n': ""}
    ans_string = ""
    for letter in num_str:  # runs through the num_string, adding the nibbles to the ans_string
        ans_string = ans_string + hex_dict[letter]
    return ans_string


# converts decimal to binary
def dec2bin(num):
    ans = ""  # empty answer string
    while num > 0:  # while loop to produce the binary string
        temp = num % 2  # find remainder of division by 2
        ans = str(temp) + ans  # add remainder to the beginning of ans
        num = math.floor(num / 2)  # get next number for pass through loop
        #print(ans)
    return ans


# converts decimal to hexadecimal
def dec2hex(num):
    temp = dec2bin(num)  # converts input to binary
    length = len(temp)  # gets length of binary
    return bin2hex(length, temp)  # converts binary to hex and returns


def main():
    parser = argparse.ArgumentParser()  # create argument parser
    parser.add_argument("-ct", "--conversion_type",
                        help="type of conversion to perform")  # adds conversion type argument
    parser.add_argument("-fi", "--file_in_name", help="name of the file to take in")  # adds file in name argument
    parser.add_argument("-fo", "--file_out_name", help="name of the file to produce")  # adds file out name  argument
    args = parser.parse_args()  # parse the arguments
    fin = open(args.file_in_name, 'r')  # creates file in object
    fout = open(args.file_out_name, 'w')  # creates file out object
    num_nums = fin.readline()
    #print(num_nums)
    fout.write(num_nums)

    if args.conversion_type == "bin2hex":  # read in file, process each line using bin2dec, write to output file
        for line in fin:
            temp = line  # temp from line already read by loop
            list(temp)  # convert temp to list
            #print(temp)
            l = int(temp[0])  # get length of number to be converted
            s = temp[2:]  # get number to be converted
            ans = bin2hex(l, s) # convert number to hex
            #print(ans)
            le = len(ans)
            fout.write(str(le) + " " + ans + '\n')  # write to outfile
        return

    if args.conversion_type == "hex2bin":  # read in file, process each line using hex2bin, write to output file
        for line in fin:
            temp = line  # temp from line already read by loop
            list(temp)  # convert temp to list
            # print(temp)
            l = int(temp[0])  # get length of number to be converted
            s = temp[2:]  # get number to be converted
            ans = hex2bin(l, s)  # convert number to binary
            # print(ans)
            le = len(ans)
            fout.write(str(le) + " " + ans + '\n')  # write to outfile
        return

    if args.conversion_type == "dec2bin":  # read in file, process each line using dec2bin, write to output file
        for line in fin:
            temp = int(line)
            ans = dec2bin(temp)  # convert number to binary
            # print(ans)
            le = len(ans)
            fout.write(str(le) + " " + ans + '\n')  # write to outfile
        return

    if args.conversion_type == "dec2hex":  # read in file, process each line using dec2hex, write to output file
        for line in fin:
            temp = int(line)
            ans = dec2hex(temp)  # convert number to hex
            # print(ans)
            le = len(ans)
            fout.write(str(le) + " " + ans + '\n')  # write to outfile
        return

if __name__ == '__main__':
    main()
