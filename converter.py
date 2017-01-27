import math


def bin2dec(length, num_str):       #converts binary to decimal
    num = 0
    for index in range(length):
        num = num + (2 ** (length - index - 1)) * int(num_str[index])
    return num


# converts binary to hexadecimal
def bin2hex(length, num_string):
    offset = 4 - length % 4             #determine how many 0s needed to make the string length evenly divisible by 4
    if length < 4:
        for i in range(4 - length):         #add 0s
            num_string = "0" + num_string
    else:
        for i in range(offset):             #add 0s
            num_string = "0" + num_string
    num_list = []
    for i in range((math.floor(len(num_string) / 4))):      #convert string into list of 4 bit nibble
        num_list.append(num_string[i * 4] + num_string[i * 4 + 1] + num_string[i * 4 + 2] + num_string[i * 4 + 3])
    #print(num_list)
    for i in range(len(num_list)):      #convert cells to decimal numbers
        num_list[i] = bin2dec(4, num_list[i])
    for i in range(len(num_list)):      #convert decimals to hex representation
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
    for cell in num_list:
        ans_string = ans_string + str(cell)
    return ans_string


# converts hexadecimal to binary
def hex2bin(num_str):
    list(num_str)               #convert num_string to list
    num_str = num_str[2:]       #pop off the 0x
    #dict to convert between the hex char and the binary string
    hex_dict = {'0':"0000", '1':"0001", '2':"0010", '3':"0011", '4':"0100", '5':"0101", '6':"0110",
                '7':"0111", '8':"1000", '9':"1001", 'A':"1010", 'B':"1011", 'C':"1100", 'D':"1101",
                'E':"1110", 'F':"1111"}
    ans_string = ""
    for letter in num_str:
        ans_string = ans_string + hex_dict[letter]
    return ans_string


# converts decimal to binary
def dec2bin(num):
    return


# converts decimal to hexadecimal
def dec2hex(num):
    return


print(hex2bin("0xF"))
