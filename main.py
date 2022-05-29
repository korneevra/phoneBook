import generator as gen
import export as exp
import import_f as imp
import ui

pb = 'temp.csv'  # файл хранения справочника
gen.csvCreate(pb, gen.listGen(5))   # генерируем справочник - случайный набор 5 абонентов
ui.file_print(pb)
while True:
    i = ui.todo()
    if i == '1':
        j = ui.imp_file()
        if j == '1':
            imp.importF1(ui.enter_file_n(), pb)
        elif j == '2':
            imp.importF2(ui.enter_file_n(), pb)
        elif j == '3':
            imp.importCSV(ui.enter_file_n(), pb)
        else:
            ui.error()
            continue
    elif i == '2':
        j = ui.exp_file()
        if j == '1':
            exp.export_f1(ui.enter_file_n(), pb)
        elif j == '2':
            exp.export_f2(ui.enter_file_n(), pb)
        elif j == '3':
            exp.export_csv(ui.enter_file_n(), pb)
        else:
            ui.error()
            continue
    elif i == '3':
        ui.file_print(pb)
    elif i == '4':
        ui.add_subs(pb)
    else:
        ui.error()
        continue
    ui.done()
    if ui.exit_cont() == 'e':
        break

