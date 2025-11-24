cities = ("Berlin", "London", "Paris", "New Delhi")
print(len(cities))
print("New York" in cities)
print("New Delhi"in cities)

t = (12,34,56)
# t.append(17)  # AttributeError: 'tuple' object has no attribute 'append'


ENV_API_URLS = tuple(["abc.com/get", "zee.com/post", "rty.com/put"])
print(ENV_API_URLS)

colours= ("red", "green", "blue")
for c in colours:
    print(c)

name = "Mira"*3
print(name)

num= (1,2,) *3
print(num )

nums = (1,2,2,3,2,4)
print(len(nums))
print(nums.count(2))
print(nums.index(3))
my_list = [1,2,3,4,5]
my_tuple= tuple(my_list)
print(my_tuple)

back_to_list = list(my_tuple)
print(back_to_list)
print(max(back_to_list))
print(back_to_list[0:3])
print(back_to_list[-1])
print(back_to_list[-2])

