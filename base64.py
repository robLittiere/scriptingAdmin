if __name__ == '__main__':
    string = "ABCD"

# Convert string to list
    charList = []

    for char in string:
        charList.append(char)

    print(charList)


# Convert each element of list in to ascii 7 bits integer
    ordList = []
    for char in charList:
        ordList.append(ord(char))

    print(ordList)

# Convert each ascii integer to binary

    binList = []
    for char in ordList:
        binList.append(bin(char))

    print(binList)


# Convert binary to octet

    octList = []
    for char in binList:
        octList.append("0" + char)

    print(octList)

# Convert binary to 6

# Convert list to string, each element is a 6 characters binary number
# Last one has to be six characters also, so add 0s to complete it

# Convert each binary number to decimal

# Convert each decimal number to base 64 table

# Convert list to string

# Complete String to create useable base64 string
