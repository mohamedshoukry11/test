import pandas as pd

def create_student_dataframe(data=None):
    
student_data_dict= [
    {'student': 'tarek', 'grade': 85, 'pass/fail': 'Pass'},
    {'student': 'hany', 'grade': 60, 'pass/fail': 'Fail'},
    {'student': 'mohamed', 'grade': 92, 'pass/fail': 'Pass'},
    {'student': 'sami', 'grade': 55, 'pass/fail': 'Fail'},
    {'student': 'riham', 'grade': 78, 'pass/fail': 'Pass'}
]

students_df = create_student_dataframe(student_data_dict)

if students_df is None: 
    print("DataFrame creation failed. Exiting.")
else:
    print("Original DataFrame:\n", students_df)

    
    if 1 < len(students_df):
        student_at_index_1 = students_df.loc[1] 
        print("\nStudent at index 1:\n", student_at_index_1)
    else:
        print("\nIndex 1 does not exist in the DataFrame.")

    passed_students = students_df[students_df['pass/fail'] == 'Pass']
    print("\nStudents who passed:\n", passed_students)

   
    passed_students_concise = students_df.loc[students_df['pass/fail'] == 'Pass']
    print("\nStudents who passed (concise):\n", passed_students_concise)



    if not passed_students.empty:  
        passing_grades = passed_students['grade']
        print("\nGrades of passing students:\n", passing_grades)

        first_passing_student = passed_students.iloc[0] 
        print("\nFirst passing student:\n", first_passing_student)

        first_passing_student_name = passed_students.iloc[0]['student']
        print("\nFirst passing student's name:\n", first_passing_student_name)