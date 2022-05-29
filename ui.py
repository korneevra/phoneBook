

def todo():
    return input('Choose action: \n (1) - import from file \n (2) - export to file \n (3) - print phone book \n :> ')


def imp_file():
    return input('Choose file format: \n (1) - format1 (txt) \n (2) - format2 (txt) \n (3) - CSV \n :> ')


def exp_file():
    return input('Choose file format: \n (1) - format1 (txt) \n (2) - format2 (txt) \n (3) - CSV \n :> ')


def error():
    print('Wrong number!!!')


def enter_file_n():
    return input('Enter file name: ')


def done():
    print('Operation done! \n\n')


def exit_cont():
    return input('Continue or exit (enter/e): ')


def file_print(file):
    with open(file, 'r') as data:
        for i in data:
            t = i.replace(';', '\t\t').replace('\n', '')
            print(t)


