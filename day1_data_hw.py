import csv
from optparse import Values

def load_from_csv(filepath):
    with open(filepath) as file:
        data = csv.DictReader(file)
        return list(data)

engagement_data = load_from_csv('./engagements.csv')
enrollments_data = load_from_csv('./enrollments.csv')
submissions_data = load_from_csv('./submissions.csv')

# Question 1
# What is the average number of days enrolled in the program?

def average_enrollment(dataset):
    days_to_cancel_list = []
    for enrollment in dataset:
        if enrollment['days_to_cancel'] == None:
            continue
        elif enrollment['days_to_cancel']:
            days_to_cancel_list.append(int(enrollment['days_to_cancel']))
    return sum(days_to_cancel_list) // len(days_to_cancel_list)
print(average_enrollment(enrollments_data))
# 43 days of average enrollment

# Question 2 
# Which user account has the highest average amount of minutes per visit? 

def highest_user_average(dataset):
    user_time = {}

    for engagement in dataset: #This takes forever but it works lol
        if engagement['acct'] not in user_time:
            num_of_all_visits = len([current_engagement['total_minutes_visited'] for current_engagement in dataset if current_engagement['acct'] == engagement['acct']])
            user_time[engagement['acct']] = sum([float(current_engagement['total_minutes_visited']) for current_engagement in dataset if current_engagement['acct'] == engagement['acct']]) / num_of_all_visits

    highest_user = max(user_time, key=user_time.get)

    return f"The user with the highest average minutes is User {highest_user} with an average of {user_time[highest_user]} minutes per visit"
print(highest_user_average(engagement_data))
# User 701 has the highest average amount of minutes per visit at an average of 229.23 minutes

# Question 3
# Which user has the most amount of passed grades

def most_passed(dataset):
    passed_grades = {}

    for grade in dataset:
        if grade['account_key'] not in passed_grades:
            passed_grades[grade['account_key']] = 0
        elif grade['account_key'] in passed_grades and grade['assigned_rating'] == 'PASSED':
            passed_grades[grade['account_key']] += 1

    highest_passes = max(passed_grades, key=passed_grades.get)
    
    return f"The student with the most passes is {highest_passes} with {passed_grades[highest_passes]} passing grades"

print(most_passed(submissions_data))