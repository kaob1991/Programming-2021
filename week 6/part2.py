# Program to allow a user to create new students and to view students 

# Will be using functions to break this up into smaller bits and to make it more managable

# Author: Katie O'Brien 

def displayMenu ():
    print ('What would you like to do?: ')
    print ('\t (a) Add new student')
    print ('\t (v) View students')
    print ('\t (q) Quit')
    choice = input("Please enter one letter (a/v/q):").strip() #removes leading and trailing whitespace
    return choice

def doAdd (students):
    currentStudent = {}
    currentStudent ["name"]= input('Please enter name : ')
    currentStudent ['modules'] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input('\t Please enter a module name (blank to quit): ').strip()

    while moduleName != '':
        module = {}
        module ["name"] = moduleName
        module ['grade'] = int(input('\t\t Please enter grade: '))
        modules.append (module)
        moduleName = input('\t Please enter a module name (blank to quit): ').strip ()

    return modules 

def  displayModules (modules):
    print ('\tName    \tGrade')
    for module in modules: 
        print ('\t{}  \t{}'.format (module ['name'], module ['grade']))

def doView (students):
    for currentStudent in students:
        print (currentStudent['name'])
        displayModules(currentStudent ['modules'])



students = []

choice = displayMenu()

while (choice != 'q'):

    if choice == ('a'):
        doAdd(students)
    elif choice == ('v'):
        doView(students)
    elif choice != ('q'):
        print('Please enter either a, v or q')
    choice = displayMenu()

