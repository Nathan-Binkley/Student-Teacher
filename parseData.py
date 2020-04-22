import json

special_converted_files = ['2018Fall.csv','2018Spring.csv'] #these files have special formatting for names (ie ' "Smith, John William" ' is normal and in these it's simply 'Smith John William' without commas or quotes )
#TBH, this is the easier way to parse but whatevs
converted_files = ['2013Fall.csv', '2014Spring.csv', '2014Fall.csv', '2015Spring.csv', '2015Fall.csv', '2016Spring.csv', '2016Fall.csv', '2017Spring.csv', '2017Fall.csv', '2018Spring.csv', '2018Fall.csv', '2019Spring.csv', '2019Fall.csv', '2020Spring.csv']

fileLines = []
master_list = {}
testData = [0,1,2]



def process_Search(query: str) -> str: #Primary search function and processing for a query. A query is generally defined by 
                                   #"Course-Number" of which it pulls the data from the DB.
    
    query = query.upper()
    data_list = master_list[query]

    A = []
    B = []
    C = []
    D = []
    F = []
    W = []
    P = []
    NP = []

    
    for i in data_list:
        A.append(i['A'])
        B.append(i['B'])
        C.append(i['C'])
        D.append(i['D'])
        F.append(i['F'])
        W.append(i['W'])

    gradesList = (A,B,C,D,F,W,P,NP)
    
    for letterGrade in gradesList:
        for i in range(len(letterGrade)):
        
            letterGrade[i] = int(letterGrade[i][:-1])

    
    AvgA = sum(A)//len(A)
    AvgB = sum(B)//len(B)
    AvgC = sum(C)//len(C)
    AvgD = sum(D)//len(D)
    AvgF = sum(F)//len(F)
    AvgWithdraw = sum(W)//len(W)

    

    return "Average; A: " + str(AvgA) + "% B: " + str(AvgB) + "% C: " + str(AvgC) + "% D: " + str(AvgD) + "% F: " + str(AvgF) + "% W: " + str(AvgWithdraw) + "%" 

def getInitials(Name):
    initials = ""
    Name = Name.split()
    Name = Name[1:] + [Name[0]]
    for i in Name:
        initials += i[0]
    return initials

def initialize():
    with open("Processed_CSV/2019Fall.csv", "r") as f:
        line = f.readline()
        while(line):
            fileLines.append(line)
            line = f.readline()
        #print("End of file. Length of fileLines = " + str(len(fileLines)))

        for i in fileLines:
            
            testData = i.split(",")
            
            course = testData[0]
            number = testData[1]
            section = testData[2]
            course_title = testData[3]
            A_Grade = testData[4]
            B_Grade = testData[5]
            C_Grade = testData[6]
            D_Grade = testData[7]
            F_Grade = testData[8]
            P_Grade = testData[9]
            F_P_Grade = testData[10]
            Withdraw = testData[11]
            if fileLines[-1] == "H":
                Name = "".join(testData[12:-1])
                Honors = testData[-1]
            else:
                Name = "".join(testData[12:])
            Name = Name.strip()

            data = {
                "name":course_title,
                "A":A_Grade,
                "B":B_Grade,
                "C":C_Grade,
                "D":D_Grade,
                "F":F_Grade,
                "W":Withdraw,
                "Professor": Name,
                "Prof Initials": getInitials(Name[1:-1])
            }
            if course+"-"+number in master_list:
                master_list[course+"-"+number].append(data)
            else:
                master_list[course+"-"+number] = []
                master_list[course+"-"+number].append(data)
            
    with open("master.json","w+") as f:
        json.dump(master_list, f, indent=4)

initialize()
query = input("What do you want to search (Course-Number)\n")
print("In Fall 2019, there was an average of " + process_Search(query) + " grade rates for " + query)

