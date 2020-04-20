
import tabula


files = ['2013Fall.pdf','2014Spring.pdf', '2014Fall.pdf','2015Spring.pdf','2015Fall.pdf','2016Spring.pdf','2016Fall.pdf','2017Spring.pdf','2017Fall.pdf','2018Spring.pdf','2018Fall.pdf','2019Spring.pdf','2019Fall.pdf','2020Spring.pdf']

for i in files:
    try:
        tabula.convert_into('GDR Clemson/'+i, i[:-4]+'.csv', output_format='csv', pages="all")
    except Exception as e:
        print(e)

