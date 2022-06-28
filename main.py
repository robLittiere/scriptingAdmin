if __name__ == "__main__":

    base_64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


    def add_zero_to_create_octal(param_list):
        """
        Add zero to the start of each elements, if needed, to form a complete binary number
        :param param_list: the given list of elements
        :return: param_list: the same list with updated elements
        """
        for binaryElement in param_list:
            while len(binaryElement) < 8:
                binaryElement.insert(0, "0")
        return param_list


    def add_nth_zero_to_number(last_binary, desired_length):
        """
        Add zeros to a binary number to give it a desired length
        :param last_binary: The last binary number of a list
        :param desired_length: An integer that represents the nth length we want to aim for
        :return:
        """
        if len(last_binary) < desired_length:
            last_binary += "0"
            return add_nth_zero_to_number(last_binary, desired_length)
        else:
            return last_binary


    def convert_list_to_binary_list(param_list):
        """
        Convert each element of a list to its equivalent ascii list
        :param param_list: The input value list
        :return:
        """
        new_list = []
        for caracter in param_list:
            # Convert each ascii integer to binary
            binary = bin(ord(caracter)).replace("b", "")
            new_list.append(binary)  # ord() returns ascii number and bin() returns binary
        return new_list


    def convert_octal_to_binary_of_six_list(octal_list):
        """
        Convert an octal list to a string. Add seperation every 6 caracters to make it a binary of six
        :param octal_list:
        :return: binary_of_six_list: A list of binary numbers
        """
        # Convert octal to string
        octalString = ''.join(octal_list)
        # Convert it back to list. Add separation every 6 caracters
        binary_of_six_list = []
        i = 0
        while i < len(octalString):
            number = octalString[i:i + 6]
            binary_of_six_list.append(number)
            i += 6

        return binary_of_six_list


    def convert_binary_to_decimal(binary_list):
        """
        Convert a given binary list into a decimal list
        :param binary_list: List containing binary numbers
        :return: decimal_list: List containing decimal numbers
        """
        decimal_list = []
        for binary_number in binary_list:
            decimal_list.append(int(binary_number, 2))
        return decimal_list


    def convert_decimal_list_to_base_64_list(decimal_list):
        """
        Convert a given decimal list elements to base64 equivalent elements
        :param decimal_list: List containing decimal numbers
        :return: base_64_list: List containing converted base64 elements
        """
        base_64_letter_list = []
        for decimal in decimal_list:
            base64_letter = base_64_table[int(decimal)]
            base_64_letter_list.append(base64_letter)
        return base_64_letter_list


    def create_base_64_decimals_to_string(base_64_list):
        '''
        Takes a list of base 64 characters, stringify it and makes sure its at least 8 characetrs long
        :param base_64_list: A List of base64 elements
        :return: base_64_string: A final base 64 String
        '''
        base_64_string = ''.join(base_64_letter_list)
        # Complete String to create useable base64 string
        while len(base_64_string) < 8:
            base_64_string += "="
        return base_64_string


    inputValue = "ABCD"
    # Convert string to list
    list = list(inputValue)

    # Convert each element of list in to ascii 7 bits integer and then to its binary
    binary_list = convert_list_to_binary_list(list)

    # Convert binary to octal
    octal_list = add_zero_to_create_octal(binary_list)

    # Convert it back to list. Add separation every 6 caracters
    binary_of_six_list = convert_octal_to_binary_of_six_list(octal_list)

    # Last one has to be six characters also, so add 0s to complete it
    binary_of_six_list[-1] = add_nth_zero_to_number(binary_of_six_list[-1], 6)

    # Convert each binary number to decimal then to base64 letters
    decimal_list = convert_binary_to_decimal(binary_of_six_list)

    # Convert each decimal number to base 64 table
    base_64_letter_list = convert_decimal_list_to_base_64_list(decimal_list)

    base_64_string = create_base_64_decimals_to_string(base_64_letter_list)
    print(base_64_string)
