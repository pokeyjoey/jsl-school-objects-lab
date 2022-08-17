from query_schools import build_instances, query_api, \
largest_total_score_school, average_total_score_of, largest_average_student_attendance

# Ok, so here we'll use our object to answer questions from our api

# 1. First write a function called build_instances that returns a list of
# school instances where each school is filled with relevant data from the api
# below we show the attributes it should contain




school_dicts = query_api()
selected_attrs = ['dbn', 'name', 'boro', 'writing_score', 'math_avg',
        'reading_avg', 'total_students', 'attendance_rate']

def test_build_instances_creates_with_selected_attrs():
    schools = build_instances(school_dicts, selected_attrs)
    first_school = schools[0]
    assert sorted(list(first_school.__dict__.keys())) == sorted(selected_attrs)

# 2. Now that we have a function that creates instances from the data in our api, we
# can answer questions about our schools.

# Write a function that returns the school instance with the largest total_score
# (where total score is the sum of the reading, math, and writing scores)

# Then write a function that returns the average total score of all schools

# Finally, write a function that returns the school who, on average, has the most number of students
# attending on a given day

def test_largest_total_score_returns_school_with_max_score():
    schools = build_instances(school_dicts, selected_attrs)
    assert largest_total_score_school(schools).name == 'STUYVESANT HIGH SCHOOL'

def test_average_total_score_of_schools():
    schools = build_instances(school_dicts, selected_attrs)
    assert average_total_score_of(schools) == 1230

#def test_largest_avg_student_attendance():
#    schools = build_instances(school_dicts)
#    assert largest_average_student_attendance(schools).name == 'BROOKLYN TECHNICAL HIGH SCHOOL'
