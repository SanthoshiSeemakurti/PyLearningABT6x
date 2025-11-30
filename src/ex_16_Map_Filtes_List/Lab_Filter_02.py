test_result = ["pass", "fail", "pass", "pass", "pass", "pass", "pass", "pass", "fail", "pass", "pass"]

result_pass = list(filter(lambda x : x == "pass", test_result))
print(result_pass)

result_fail = list(filter(lambda y: y == "fail", test_result))
print(result_fail)
