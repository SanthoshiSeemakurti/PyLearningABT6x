"""
Write a Function to Check API Status

Problem:

Write a function check_status(status_code) that returns:

"PASS" if status_code = 200

"FAIL" if status_code = 400 or 500

"UNKNOWN" otherwise

Example Input & Output:

print(check_status(200))   # PASS

print(check_status(500))   # FAIL

print(check_status(302))   # UNKNOWN

"""


# define /declaring function
def check_status(status_code):
    if status_code == 200:
        return "PASS"
    elif status_code==400:
        return "FAIL"
    else:
        return "UNKNOWN"

# user input
status_code = input(int("Enter a status code: "))

# calling function
check_status(status_code)