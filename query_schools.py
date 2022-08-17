import pandas as pd
from school import School

def query_api():
    url = "https://raw.githubusercontent.com/jigsawlabs-student/decision-trees-intro/master/3-practical-ds-4/nyc_hs_sat.csv"
    df = pd.read_csv(url)
    return df.to_dict('records')


def build_instances(records_list, selected_attributes):
    school_instance_list = []

    for record in records_list:

        # use a dictionary comprehension to create a temp script
        temp_dict = {key:value for (key, value) in record.items() if key in selected_attributes}

        # create an instance and add it to the list
        school_instance_list.append(
            School(**temp_dict)
        )

    return school_instance_list

def largest_total_score_school(schools):
    largest_total_score_school = schools[0]

    for school in schools:

        if school.total_score() > largest_total_score_school.total_score():
            largest_total_score_school = school

    return largest_total_score_school

def average_total_score_of(schools):
    number_of_schools = len(schools)
    average_total_score_of_all_schools = 0

    for school in schools:
       average_total_score_of_all_schools = average_total_score_of_all_schools + school.total_score()

    average_total_score_of = average_total_score_of_all_schools / number_of_schools

    return int(average_total_score_of)

def largest_average_student_attendance(schools):
    pass
