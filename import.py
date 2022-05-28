

def importF1(file):
    data = open(file, 'r')
    temp = open('temp.csv', 'w')
    for i in data:
        i.replace('\n', ';')
        temp.write(i)
    data.close()
    temp.close()


def importF2(file):
    data = open(file, 'r')
    temp = open('temp.csv', 'w')
    for i in data:
        i.replace(',', ';')
        temp.write(i)
    data.close()
    temp.close()


def importCSV(file):
    data = open(file, 'r')
    temp = open('temp.csv', 'w')
    for i in data:
        temp.write(i)
    data.close()
    temp.close()
