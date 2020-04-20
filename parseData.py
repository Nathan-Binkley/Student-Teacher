
special_converted_files = ['2018Fall.csv','2018Spring.csv'] #these files have special formatting for names (ie ' "Smith, John William" ' is normal and in these it's simply 'Smith John William' without commas or quotes )
#TBH, this is the easier way to parse but whatevs
converted_files = ['2013Fall.csv', '2014Spring.csv', '2014Fall.csv', '2015Spring.csv', '2015Fall.csv', '2016Spring.csv', '2016Fall.csv', '2017Spring.csv', '2017Fall.csv', '2018Spring.csv', '2018Fall.csv', '2019Spring.csv', '2019Fall.csv', '2020Spring.csv']

fileLines = []

with open("Processed_CSV/2013Fall.csv", "r") as f:
    line = f.readline()
    while(line):
        fileLines.append(line)
        line = f.readline()
    print("End of file. Length of fileLines = " + str(len(fileLines)))

testData = [0,1,2]
print(fileLines[0])


for i in fileLines[:-1]:
    testData = i.split(",")
    course = testData[0]
    number = testData[1]
    section = testData[2]
    course_title = testData[4]
    A = testData[5]
    B = testData[6]
    C = testData[7]
    D = testData[8]
    F = testData[9]
    P = testData[10]
    F_P = testData[11]
    W = testData[12]
    temp1 = testData[12:]

print(testData)
print("Course: " + str(course))
print("Number: " + str(number))
print("Prof: " + "".join(temp1))
