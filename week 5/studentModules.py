# Stores a student name and a list of their courses 
# Then prints out this data 

# Author: Katie O'Brien 

student = {'name': 'Mary', 'modules':
            [{"coursename": "Programming", "grade" : 45 },
            {"coursename" : "History" , "grade" : 99}]
            }

print ("Student: {}" .format(student['name']))
for module in student ["modules"]:
    print ("\t {} \t: {}" .format(module['coursename'], module["grade"]))