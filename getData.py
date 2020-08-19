import tabula
files = ['2014Fall.pdf','2015Spring.pdf','2015Fall.pdf','2016Spring.pdf','2016Fall.pdf','2017Spring.pdf','2017Fall.pdf','2018Spring.pdf','2018Fall.pdf','2019Spring.pdf','2019Fall.pdf']
special_converted_files = ['2018Fall.csv'] #these files have special formatting for names 
converted_files = ['2014Fall.csv', '2015Spring.csv', '2015Fall.csv', '2016Spring.csv', '2016Fall.csv', '2017Spring.csv', '2017Fall.csv', '2018Spring.csv', '2018Fall.csv', '2019Spring.csv', '2019Fall.csv']

# for i in files: ## Make into csvs
#     try:
#         tabula.convert_into('GDR Clemson/' + i, 'Processed_CSV/' + i[:-4] + '.csv', output_format='csv', pages="all")
#     except Exception as e:
#         print(e)



master_String = ""

for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)

with open("master-2014.csv", "w") as f:
    f.write(master_String)
print("FIRST ROUND: ")
print(converted_files)
converted_files.pop(0)
converted_files.pop(0)
print(converted_files)


master_String = ''
for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)
with open('master-2015.csv', 'w') as f:
    f.write(master_String)

print("SECOND ROUND: ")
print(converted_files)
converted_files.pop(0)
converted_files.pop(0)
print(converted_files)

master_String = ''
for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)
with open('master-2016.csv', 'w') as f:
    f.write(master_String)

print("THIRD ROUND: ")
print(converted_files)
converted_files.pop(0)
converted_files.pop(0)
print(converted_files)

master_String = ''
for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)
with open('master-2017.csv', 'w') as f:
    f.write(master_String)

print("FOURTH ROUND: ")
print(converted_files)
converted_files.pop(0)
converted_files.pop(0)
print(converted_files)

master_String = ''
for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)
with open('master-2018.csv', 'w') as f:
    f.write(master_String)

print("FIFTH ROUND: ")
print(converted_files)
converted_files.pop(0)
converted_files.pop(0)
print(converted_files)

master_String = ''
for i in converted_files:
    try:
        with open('Processed_CSV/' + i, "r") as f:
            master_String += f.read()
    except Exception as e:
        print(e)
with open('master-2019.csv', 'w') as f:
    f.write(master_String)

print("SIXTH ROUND: ")
print(converted_files)
converted_files.pop(0)
# converted_files.pop(0) #-- Uncomment when SP2020 GDR comes out
print(converted_files)

