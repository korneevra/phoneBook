

def importF1(file, pb):
    data = open(file, 'r')
    temp = open(pb, 'w')
    for i in data:
        if i != '\n':
            ss = i.replace('\n', ';')
            temp.write(ss)
        else:
            temp.write(i)
    data.close()
    temp.close()


def importF2(file, pb):
    data = open(file, 'r')
    temp = open(pb, 'w')
    for i in data:
        ss = i.replace(',', ';')
        temp.write(ss)
    data.close()
    temp.close()


def importCSV(file, pb):
    data = open(file, 'r')
    temp = open(pb, 'w')
    for i in data:
        temp.write(i)
    data.close()
    temp.close()
