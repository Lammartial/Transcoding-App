# Timing Python Scripts

# Import relevant modules
import time
import pytz
from datetime import datetime

# Start of the python script
script_start_time = datetime.now(pytz.timezone('Asia/Saigon'))

# Timing a section of python code
start_time = time.time()
# Do some code


# End time once the code has finished
end_time = time.time()
# Total time
final_time = end_time - start_time
print(f"Execution time is {final_time} seconds")

# Script end time
script_end_time = datetime.now(pytz.timezone('Asia/Saigon'))
print(script_end_time - script_start_time)