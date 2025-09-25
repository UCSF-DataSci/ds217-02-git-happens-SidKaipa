import os
#TODO load_data(filename): Generic loader that checks file extension

def load_data(filename):
    if filename.lower().endswith('.csv'): #converts filename to lowercase and looks for the extension
        return load_csv(filename)
    else:
        return []

#TODO load_csv(filename): Load CSV data (same technique as basic script)

def load_csv(filename):
    ret = []
    file = open(filename, "r")
    lines = file.readlines()

    #for each row
    for line in lines[1:]:
        #get all the values together and add that list to the final list to be returned
        ret.append(line.strip().split(','))
    file.close()
    return ret


def get_grades(students): #gets all the grades of the students into one list
    grades = []
    for l in students:
        grades.append(int(l[2]))
    return grades


#TODO analyze_data(students): Return dictionary with multiple statistics
def analyze_data(students):
    total_students = len(students)

    #average grade
    denom = 0
    numerator = 0
    #for each list, add the grade to the numerator and increment the denominator
    for l in students:
        numerator += int(l[2])
        denom += 1
    avg = numerator/denom


    #max grade
    max = 0
    for l in students:
        if int(l[2]) > max: #checks each grade to see its greater than the current max, if it is, max is updated
            max = int(l[2])

    #min grade
    min = 100
    for l in students:
        if int(l[2]) < min: #checks each grade to see its less than the current min, if it is, min is updated
            min = int(l[2])

    #subject counts
    dict = {}
    subjects = ["math", "science", "trig", "calculus", "chemistry", "biology", "astronomy"]
    for l in students:
        subject = l[3].strip() # for each subject
        dict[subject] = dict.get(subject,0) + 1 #the subject we are on, if it's not found in the dictionary, a key is made and the val is set to 0, else it's incremented
    
    #return this
    ret_dict = {
        "total students" : total_students,
        "average grade" : avg,
        "max grade" : max,
        "min grade" : min,
        "subject counts" : dict

    }
    return ret_dict

    

 




#TODO analyze_grade_distribution(grades): Count grades by letter grade ranges

def analyze_grade_distribution(grades):
    dist = {"A":0,"B":0,"C":0,"D":0,"F":0}
    #checks each grade and increments the count of the grade
    for grade in grades:
        if grade >= 90:
            dist["A"] += 1
        elif grade >= 80:
            dist["B"] += 1
        elif grade >= 70:
            dist["C"] += 1
        elif grade >= 60:
            dist["D"] += 1
        else:
            dist["F"] += 1

    #creates a percentage dictionary and divides the counts by the total
    perc = dist.copy()
    perc["A"] = dist["A"] / len(grades)
    perc["B"] = dist["B"] / len(grades)
    perc["C"] = dist["C"] / len(grades)
    perc["D"] = dist["D"] / len(grades)
    perc["F"] = dist["F"] / len(grades)

    return {"counts": dist,
            "percentages": perc}


#TODO save_results(results, filename): Save detailed report

def generate_report(filename, students, grades):
    return f"""
--- Report ---
Analyze Data: {analyze_data(students)}
Grade Distribution: {analyze_grade_distribution(grades)}
-----------------------------
"""


def save_results(report, filename): 
    dir = os.path.dirname(filename) #gets the directory name of the filename
    if dir: #checks if the directory exists, if not it creates it
        os.makedirs(dir, exist_ok=True)
    file = open(filename, "w") #opens new file, and writes in the report
    file.write(report)
    file.close()

#TODO main()
def main():
    input_file = "../data/students.csv"
    output_file = "../output/analysis_report_2.txt"
    students = load_data(input_file)
    grades = get_grades(students)
    report = generate_report(input_file,students,grades)
    save_results(report,output_file)

if __name__ == '__main__':
    main()
