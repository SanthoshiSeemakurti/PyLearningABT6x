"""

Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.

"""

import time
wait_time = 0    #initiation

while wait_time < 5:
  page_load = input(f"wait time {wait_time}: Is the Page loaded? (yes/no): ").strip().lower()
  if page_load == "yes":        # condition
      break
  wait_time += 1

if wait_time < 5:
        print ("✅ Page loaded successful")
else:
        print("❌ Page load failed due to timeout!")
