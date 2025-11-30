# converting  milliseconds to seconds

response_time =[1200, 3400, 6000]

def mil_sec(x):
    return x/1000

response_time_in_Sec= list(map(mil_sec, response_time))
print((response_time_in_Sec))


# with lambda expression:
response_time_in_s = list(map(lambda x: x/1000, response_time))
print(response_time_in_s)