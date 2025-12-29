import sys

def process_student_data(argv=None):
    if argv is None:
        argv = sys.argv

    # Check command-line arguments
    if len(argv) == 7:
        script_name = argv[0]
        name = argv[1]
        department = argv[2]
        semester = argv[3]
        m1 = argv[4]
        m2 = argv[5]
        m3 = argv[6]
    else:
        script_name = argv[0]
        name = "Niyati Gogri"
        department = "BCA"
        semester = "3"
        m1 = "98"
        m2 = "96"
        m3 = "89"

    # Calculate total and average
    total_marks = int(m1) + int(m2) + int(m3)
    average_marks = total_marks / 3

    # Grade calculation
    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 80:
        grade = "B"
    elif average_marks >= 70:
        grade = "C"
    elif average_marks >= 60:
        grade = "D"
    else:
        grade = "F"

    return {
        "script_name": script_name,
        "name": name,
        "department": department,
        "semester": semester,
        "marks": (int(m1), int(m2), int(m3)),
        "total": total_marks,
        "average": average_marks,
        "grade": grade
    }


if __name__ == "__main__":
    result = process_student_data()

    print("Script Name:", result["script_name"])
    print("Student Name:", result["name"])
    print("Department:", result["department"])
    print("Semester:", result["semester"])
    print("Marks in 3 Subjects:", *result["marks"])
    print("Total Marks:", result["total"])
    print("Average Marks:", result["average"])
    print("Grade:", result["grade"])
