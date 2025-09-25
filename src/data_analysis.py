#TODO load_students(filename): Read CSV and return list of student data
import os
def load_students(filename):
    ret = []
    file = open(filename, "r")
    lines = file.readlines()

    #for each row
    for line in lines[1:]:
        #get all the values together and add that list to the final list to be returned
        ret.append(line.strip().split(','))
    file.close()
    return ret


#TODO calculate_average_grade(students): Calculate and return average

def calculate_average_grade(students):
    #if the list is empty return 0
    if len(students) == 0:
        return 0
    denom = 0
    numerator = 0
    #for each list, add the grade to the numerator and increment the denominator
    for l in students:
        numerator += int(l[2])
        denom += 1
    return numerator/denom

#TODO count_math_students(students): Count students in Math

def count_math_students(students):
    total = 0
    #for each list, check to see if the student is in Math, if so increment
    for l in students:
        if l[3] == "Math":
            total += 1
    return total

#TODO generate_report(): Create formatted report string

def generate_report(total_students, avg_grade, num_in_math):
    return f"""
--- Report ---
Total Students Analyzed: {total_students}
Average Grade: {avg_grade:.1f}
Students in Math: {num_in_math}
-----------------------------
"""

#TODO save_report(report, filename): Write report to file

def save_report(report, filename):
    dir = os.path.dirname(filename) #gets the directory name of the filename
    if dir: #checks if the directory exists, if not it creates it
        os.makedirs(dir, exist_ok=True)
    file = open(filename, "w") #opens new file, and writes in the report
    file.write(report)
    file.close()

#TODO main()
def main():
    input_file = "data/students.csv"
    output_file = "output/analysis_report.txt"
    ret = load_students(input_file)
    num_of_students = len(ret)
    avg_grade = calculate_average_grade(ret)
    math_count = count_math_students(ret)
    report = generate_report(num_of_students,avg_grade,math_count)
    save_report(report,output_file)


if __name__ == '__main__':
    main()