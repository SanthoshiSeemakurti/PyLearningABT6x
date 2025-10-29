"""
You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request

"""
API_Response = int(input("Enter the API response:").strip())
if API_Response == "200":
    print ("✅ The API response is successful.")
elif API_Response=="404":
    print(" ❌ The requested resource could not be found on the server.")
else:
    print("Other value is entered! Enter valid API response code from your test script!")