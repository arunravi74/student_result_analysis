# student_result_analysis

1. /api/student/
    Methods allowed : GET, POST
      The GET method is used to see all the student details
      The POST method is used to add the student details

2. /api/student/<pk>/marks/add/
    Methods allowed: POST
      The POST method is used to add the marks to a particular student
      
3. /api/student/<pk>/marks/
    Methods allowed: GET
      The GET method is used to get the mark of a particular student
      
4. /api/student/results/
    Methods Allowed: GET
    The GET method show category based results
      1. The total number of students
      2. The number of students in each grade
            The following are the grades
            a. 100 -91 - A
            b. 90 - 81 -B
            c. 80 - 71 -C
            d. 70 - 61 -D
            e. 61 - 55 -E
            f. < 55 - F
      4. Distinction percentage, First class, and pass percentage using the formulas given below
           a. Distinction % = ( number of students in A grade / total number of students ) * 100
           b. First class % = [ (number of students in B grade + number of students in c grade ) / total number of students] * 100
           c. Pass % = [ (total number of students - number of students in F grade ) / total number of students ] * 100 
