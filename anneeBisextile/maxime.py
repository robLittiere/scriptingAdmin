if __name__ == '__main__':

    boolean = True
    print('Entrez une année :')
    yearInput = input()

    if boolean is True:
        if yearInput.isdigit():
            if int(yearInput) % 4 == 0 and int(yearInput) % 100 != 0:
                print("L'année " + str(yearInput) + " est bisextile.")
            elif int(yearInput) % 400 == 0:
                print("L'année " + str(yearInput) + " est bisextile.")
            else:
                print("L'année " + str(yearInput) + " n'est pas bisextile.")
        else:
            boolean = False
