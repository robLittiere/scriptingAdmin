if __name__ == '__main__':
    string = "ABCD"

    # Convert string to list
    def toList(paramList):
        charList = []

        for char in paramList:
            charList.append(char)

        return charList

    # Convert each element of list in to ascii 7 bits integer
    def toAscii(paramList):
        ordList = []

        for char in paramList:
            ordList.append(ord(char))

        return ordList

    # Convert each ascii integer to binary
    def toBin(paramList):
        binList = []
        for char in paramList:
            binList.append(bin(char))

        return binList

    # Convert binary to octet
    def toOct(paramList):
        octList = []
        for char in paramList:
            octList.append("0" + char)

        return octList

    # Convert oct to one string
    def octToString(paramList):
        octString = ""
        for char in paramList:
            octString += char

        return octString


    # Convert list to string, each element is a 6 characters binary number


# Last one has to be six characters also, so add 0s to complete it

# Convert each binary number to decimal

# Convert each decimal number to base 64 table

# Convert list to string

# Complete String to create useable base64 string

print(octToString(toOct(toBin(toAscii(toList(string))))))
