

def export_csv(f_name, pb):
    data = open(f_name, 'w')
    pb = (open(pb, 'r'))
    for i in pb:
        data.write(i)
    data.close()
    pb.close()


def export_f1(f_name, pb):
    data = open(f_name, 'w')
    pb = (open(pb, 'r'))
    for i in pb:
        data.write(i.replace(';', '\n') + '\n')
    data.close()
    pb.close()


def export_f2(f_name, pb):
    data = open(f_name, 'w')
    pb = (open(pb, 'r'))
    for i in pb:
        data.write(i.replace(';', ','))
    data.close()
    pb.close()
