import generator as gen
import export as exp

lst = gen.listGen(10)
exp.export_csv('pb', lst)
exp.export_f1('format1')
exp.export_f2('format2')

