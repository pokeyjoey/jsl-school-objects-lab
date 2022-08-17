from school import School


# 1. Defining a School class

# First we need to write a class that accepts the
# initialization attributes outlined in the `school_attributes` dictionary below

school_attributes = {'dbn': '01M292',
 'name': 'HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES',
 'reading_avg': 355.0,
 'math_avg': 404.0,
 'writing_score': 363.0,
 'boro': 'M',
 'total_students': 171,
 'attendance_rate': 0.87}

def test_that_school_initialized_with_dbn_name_and_boro():
    school = School(**school_attributes)
    sorted_attributes = sorted(['dbn', 'name', 'boro', 'reading_avg', 'math_avg', 'writing_score', 'total_students', 'attendance_rate'])
    assert sorted(list(school.__dict__.keys())) == sorted(['dbn', 'name', 'boro', 'reading_avg', 'math_avg', 'writing_score', 'total_students', 'attendance_rate'])


# Then also define a class attribute, as every instance has the same city

def test_that_school_has_class_attribute_of_city():
    assert School.city == 'New York City'

# Next we'll write some methods that can perform calculations of a school
# Write a total_score() that returns the sum of the math, writing, and reading averages for a school 
# And write an avg_student_attendance that calculates the average number of students that attend a school on a day
# And write a method that returns the largest score of the writing, reading, and math scores

def test_total_score_returns_total_of_scores():
    school = School(**school_attributes)
    assert school.total_score() == float(355 + 404 + 363)

def test_avg_student_attendance_returns_avg_attendance():
    school = School(**school_attributes)
    assert school.avg_student_attendance() == 171*.87

def test_max_score_returns_max_of_scores():
    school = School(**school_attributes)
    assert school.max_score() == 404.0
