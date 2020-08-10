import json
import os

special_converted_files = ['2018Fall.csv','2018Spring.csv'] #these files have special formatting for names (ie ' "Smith, John William" ' is normal and in these it's simply 'Smith John William' without commas or quotes )
#TBH, this is the easier way to parse but whatevs
converted_files = ['2013Fall.csv', '2014Spring.csv', '2014Fall.csv', '2015Spring.csv', '2015Fall.csv', '2016Spring.csv', '2016Fall.csv', '2017Spring.csv', '2017Fall.csv', '2019Spring.csv', '2019Fall.csv', '2020Spring.csv']

fileLines = []
master_list = {}
master_prof_list = {}



def process_Search(orig_query: str) -> str: #Primary search function and processing for a query. A query is generally defined by 
                                   #"Course-Number" of which it pulls the data from the DB.
    query = orig_query.upper()
    
    items = query.split("-")
    master_String = ''

    # if("ALL" in items):
    #     print("ALL IN QUERY")
    #     print("HERE COMES THE SUN")
    #     if items[0] == "ALL" and items[1] == "ALL":
    #         print("ALLALL")
    #         for i in master_list:
    #             master_String += process_Search(i)
    #     elif items[0] == "ALL":
    #         for i in master_list:
    #             if items[1] in i:
    #                 master_String += process_Search(i)
    #     elif items[1] == "ALL":
    #         for i in master_list:
    #             if items[0] in i:
    #                 master_String += process_Search(i)
    #     else:
    #         print("Misunderstood")
    #         return "HELP"
    #     return master_String

    # else:
    if query in master_list:
        data_list = master_list[query]
    else:
        raise NotADirectoryError
    name = data_list[-1]['name'] # Get the most recent course name on file. If we did the beginning, it'd throw the incorrect name because Clemson is big dumb.
    # print(data_list)
    A = []
    B = []
    C = []
    D = []
    F = []
    W = []
    P = []
    NP = []
    

    professorGrades = {}

    
    for i in data_list:
        A.append(i['A'])
        B.append(i['B'])
        C.append(i['C'])
        D.append(i['D'])
        F.append(i['F'])
        W.append(i['W'])

        
        searchableName = getFirstLast(i['Professor'])

        professorGrades[searchableName] = []
        

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

    courseString = "Average; A: " + str(AvgA) + "% B: " + str(AvgB) + "% C: " + str(AvgC) + "% D: " + str(AvgD) + "% F: " + str(AvgF) + "% W: " + str(AvgWithdraw) + "% from " + str(len(data_list)) + " class(es) for " + orig_query + ": " + name
    

    bestProfName = "" #Professor name to go in professor string
    bestProfAB = 0
    bestProfLenCount = 0

    worstProfName = ""
    worstProfFW = 0
    worstProfLenCount = 0

    data = []

    for i in professorGrades:
        
        try:
            professorGrades[i].extend(process_profQuery(i))
            data = professorGrades[i]
        except Exception as e:
            print(e)
        
        if data[0] > bestProfAB:
            bestProfName = i
            bestProfAB = data[0]
            bestProfLenCount = data[-1]
        if data[1] > worstProfFW:
            worstProfName = i
            worstProfFW = data[1]
            worstProfLenCount = data[-1]
    
    profString = "The statistically best professor is " + bestProfName + " with an A+B Avg of " + str(bestProfAB) + "% in " + str(bestProfLenCount) + " classes\n\nThe statistically worst professor is " + worstProfName + " with an F+W Avg of " + str(worstProfFW) + "% out of " + str(worstProfLenCount) + " class(es)" #Final professor string

    return courseString + "\n\n" + profString + "\n\n"



def getInitials(Name):
    initials = ""
    Name = Name.split()
    Name = Name[1:] + [Name[0]] #Rotates it
    for i in Name:
        initials += i[0]
    return initials

def initialize():
    global master_list, master_prof_list

    if os.path.isfile('./master.json'): #SKIP PARSE DATA WHEN NOT NECESSARY
        print("FOUND COURSE FILE")
        with open('master.json', 'r') as f:
            master_list = json.load(f)
        # print(master_list)
        if os.path.isfile('./master_prof.json'):
            print("FOUND PROF FILE")
            with open('master_prof.json', 'r') as f:
                master_prof_list = json.load(f)
        else:
            print("PROF FILE NOT FOUND")
    else:
    
        with open("master.csv", "r") as f:
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

                if Name[0] == '"':
                    Name = Name[1:-1]

                FL = getFirstLast(Name)


                data = {
                    "name":course_title,
                    "A":A_Grade,
                    "B":B_Grade,
                    "C":C_Grade,
                    "D":D_Grade,
                    "F":F_Grade,
                    "W":Withdraw,
                    "Professor": Name,
                    "Prof Initials": getInitials(Name)
                }

                if course+"-"+number in master_list:
                    master_list[course+"-"+number].append(data)
                else:
                    master_list[course+"-"+number] = []
                    master_list[course+"-"+number].append(data)

                if FL in master_prof_list:
                    master_prof_list[FL].append(data)
                else:
                    master_prof_list[FL] = []
                    master_prof_list[FL].append(data)
                
        with open("master.json","w+") as f: #Unformatted data, useful for space
            json.dump(master_list, f)
        with open("master_prof.json", "w+") as f:
            json.dump(master_prof_list, f)
          

def getFirstLast(Name):
    FML = Name.split()
    First = FML[1]
    Last = FML[0]
    return First + " " + Last



def process_profQuery(Name):
    data_list = master_prof_list[Name]
    
    A = []
    B = []
    F = []
    W = []
    P = []
    NP = []    

    C = []
    D = [] # Incase you want these 

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

    return  [(AvgA + AvgB), (AvgF+AvgWithdraw), (len(data_list))]




def toCamelCase(Name):
    items = Name.split()
    for i in range(len(items)):
        items[i] = items[i][0].upper() + items[i][1:].lower()
    return " ".join(items)

def getAllCourses():
    temp = []
    for i in master_list:
        if i[:-5] not in temp:
            temp.append(i[:-5])
        else:
            pass
    with open("CourseList.txt", "w") as f:
        for i in range(len(temp)):
            f.write(temp[i]+"\n")

def go(course):
    initialize()
    getAllCourses()
    searchCourse(course)

def searchCourse(query):
    # query = input("What course do you want to search? (Format: <Course>-<number> ie CPSC-3720)\n")
    try:
        
        print("\n--------------------------------------------------------")
        print("Since Spring 2014, there was an average of " + process_Search(query))
        print("DISCLAIMER:")
        print("Not every professor listed will be at Clemson, this is a tool built for better information but not complete information")
        print("Take it at your own discression")
        print("\nIn addition, this system works on the Grade Distribution Releases located at https://www.clemson.edu/institutional-effectiveness/oir/data-reports/\n")
        print("As a result, the limitations according to the GDR are as follows:")
        print('*Course Sections that meet the following conditions are not included: Undergraduate classes with less than 10 students or Graduate classes with less than 5 students. In addition, if a section has all but 1 student making a common grade (example: All but one student makes a "B" in a class), the section is excluded.*')
        print('\n----------------------------------------------------------------------------')
    except NotADirectoryError as e:
        print("Class not found, are you sure you used the correct format? (Ex: cpsc-2120)")
    except Exception as e:
        
        print("Something went wrong somewhere, idk bout that")
        print(e)

go('cpsc-2120')