import os
import csv 
import sys
# This is the path where you want to search
path = sys.argv[1]
#'/Users/mohammadnassar/OneDrive - University of New Haven/Ethical_Hacking_Material/THM assignments'

# this is the extension you want to detect
extension = '.csv'

grades={}
emails={}
for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            print (file_name)
            with open(file_name) as csv_file:
                
                csv_reader = csv.reader(csv_file, delimiter=',')
                
                
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        pass
                        line_count+=1
                        # print(f'Column names are {", ".join(row)}')
                    else:
                        if file_name=='TryHackMe  Students.csv':
                            emails[row[1]]=row[0]
                        elif file_name=="my.csv":
                            pass
                        else: 
                            if not row[1] in grades: 
                                grades[row[1]]={}  
                            grades[row[1]][file_name]=row[-1]
for student in grades: 
    print (student)
    # for x in grades[student]: 
    #     print (x, grades[student][x])

for x in emails: 
    print (x, emails[x])
                        
    

# Create header line
students = list (grades.keys())
print (students)
assts = set()
# create a list of assignment
for d in grades.values():
    for asst in d: 
        assts.add(asst)
print(assts)
assts = list (assts)

header_line = ["Student/Assignment"]  + assts
print (header_line)
# Create rows
rows = [header_line]
print (students)
for std in students:
    print(emails[std])
    rows += [ [emails[std]] + [grades[std].get(asst,'-') for asst in assts] ]

for row in rows: 
    print (row)

with open('my.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)
            
