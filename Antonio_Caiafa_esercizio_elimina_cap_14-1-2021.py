import openpyxl
Excel_programma = openpyxl.load_workbook(filename="Elenco_cap.xlsx")
Excel_file = Excel_programma['Foglio1']
Cap = [Excel_file['A1'].value]
Isola = [Excel_file['D1'].value]
for i in range(1, 3970):
    Cap.append(Excel_file['A' + str(i)].value)
for i in range(1, 47):
    Isola.append(Excel_file['D' + str(i)].value)
Txt_terra = open("Elenco_cap_terra.txt", "w")
for i in range(1, 3970):
    if (Cap[i] in Isola) == False:
        Txt_terra.write(str(Cap[i])+"\n")
Txt_terra.close()