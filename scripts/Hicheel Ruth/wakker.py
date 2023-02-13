import time

# Define a counter and set to five
seconds = 5

# As long as counter is not zero:
while seconds > 0:
	
    print("tick")
	# Decrement counter
    seconds = seconds -1

	# Sleep for one second
    time.sleep(1)

# Make beep sound
print("peep")
print('\a')