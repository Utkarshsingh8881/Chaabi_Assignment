# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

from datetime import datetime

def check_difference(from_date, to_date, difference):
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')
    date_difference = abs((to_datetime - from_datetime).days)
    return date_difference < difference

from_date = input("Enter the 'from' date (yy-mm-dd): ")
to_date = input("Enter the 'to' date (yy-mm-dd): ")
difference = int(input("Enter the difference (in days): "))
result = check_difference(from_date, to_date, difference)
print(result)