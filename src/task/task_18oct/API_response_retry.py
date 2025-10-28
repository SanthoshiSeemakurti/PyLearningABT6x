"""
An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 times, print a failure message.

Hint: Use a while loop with a counter.


Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200

✅ Test Passed
"""

count =1    # initialization
while count <= 3 :      # condition
    response =int(input("Enter API response code: "))
    print(f"Attempt {count}: Response {response}")
    if response == 200:
        break
    count += 1      # update


if response == 200:
    print("✅ Test Passed")
else:
    print("❌ Test Failed")