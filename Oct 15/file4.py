import xlsxwriter

x = xlsxwriter.Workbook('Arvind.xlsx')


worksheet = x.add_worksheet()

worksheet.write('A1','Arvind')
worksheet.write('A2','Akash')
worksheet.write('A3','prakash')
worksheet.write('A4','vikas')
worksheet.write('A5','dinesh')
worksheet.write('A6','suresh')
worksheet.write('A7','mahesh')
worksheet.write('A8','nitesh')
worksheet.write('A9','priyesh')
worksheet.write('A10','nilesh')
worksheet.write('A11','viseesh')
worksheet.write('A12','madhuresh')
worksheet.write('A13','pratesh')


x.close()

