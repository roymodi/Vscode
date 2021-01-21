import xlsxwriter as df

w=df.Workbook('C:\\Users\\bidyut\\Vscode\\a.xlsx')
w1=w.add_worksheet('my')
w2=w.add_worksheet('my1')

w1.write('A1','Name')
w1.write('B1','roll no')
w1.write('C1','Address')

b=['ram','raj','ajay']
c=[10,12,5]
d=['as4','jdh','dsds']
'''
w1.write('A2',b[0])
w1.write('A3',b[1])
w1.write('A4',b[2])
w1.write('B2',c[0])
w1.write('B3',c[1])
'''

for i in range(1,len(b)+1): # for loop for data writing
    w1.write(i,0,b[i-1])
    w1.write(i,1,c[i-1])
    w1.write(i,2,d[i-1])

w1.write_formula('B6','=sum(B2:B4)')# add sum


w.close()