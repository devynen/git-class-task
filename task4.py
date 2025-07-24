"""
    You're helping a student at the University of Jos register for courses this semester.
    Their initial course list is: courses = ["MTH 101", "PHY 101", "CHM 101", "CSC 101", "GST 101"]
    
    1. The student realizes they need to add "ENG 101" at the beginning of their course list 
       since English is a prerequisite for other courses.
    2. The Academic Office informs them that "GST 101" has been moved to next semester, 
       so it should be removed from the current list.
    3. The student wants to add "BIO 101" right after "CHM 101" to complete their science requirements.
    4. Find and display the total number of courses the student is now registered for.
    5. The student wants to know what their 3rd course in the list is.
"""

courses = ["MTH 101", "PHY 101", "CHM 101", "CSC 101", "GST 101"]

#to add ENG at the beginning
courses.insert(0,"ENG 101")
print(courses)

#to remove GST
del courses[-1]
print(courses)

#to add bio101 
courses.insert(-1,"BIO 101")
print(courses)

#total number of courses
total_courses=len(courses)
print(f"total number of course is:",total_courses)

#to display third course
third_course = courses[2]
print(f"third course is :",third_course)

