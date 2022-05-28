

def export_csv(f_name, book):
    data = open(f'{f_name}.csv', 'a')
    for i in book:
        data.write(i + '\n')
    data.close()


def export_f1(f_name):
    data = open(f'{f_name}.txt', 'w')
    pb = (open('pb.csv', 'r'))
    for i in pb:
        data.write(i.replace(';', '\n') + '\n')
    data.close()
    pb.close()


def export_f2(f_name):
    data = open(f'{f_name}.txt', 'w')
    pb = (open('pb.csv', 'r'))
    for i in pb:
        data.write(i.replace(';', ','))
    data.close()
    pb.close()
