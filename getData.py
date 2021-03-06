import tabula
files = ['2014Spring.pdf', '2014Fall.pdf','2015Spring.pdf','2015Fall.pdf','2016Spring.pdf','2016Fall.pdf','2017Spring.pdf','2017Fall.pdf','2018Spring.pdf','2018Fall.pdf','2019Spring.pdf','2019Fall.pdf','2020Spring.pdf']
special_converted_files = ['2018Fall.csv','2018Spring.csv'] #these files have special formatting for names
converted_files = ['2014Spring.csv', '2014Fall.csv', '2015Spring.csv', '2015Fall.csv', '2016Spring.csv', '2016Fall.csv', '2017Spring.csv', '2017Fall.csv', '2018Spring.csv', '2018Fall.csv', '2019Spring.csv', '2019Fall.csv', '2020Spring.csv']

for i in files: ## Make into csvs
    try:
        tabula.convert_into('GDR Clemson/' + i, 'Processed_CSV/' + i[:-4] + '.csv', output_format='csv', pages="all")
    except Exception as e:
        print(e)

master_String = ""

for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)
    

with open("master.csv", "w") as f:
    f.write(master_String)

