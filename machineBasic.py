import time
import sys

def machineWrite(text, velocity = 0.01):
	"""
	Simulates the behavior of a typewriter to offer more realism in the output flow

	Args:
		text: what the machine is going to write.
		velocity: (default 0.01): speed with which you write the text.

	"""
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush() 
		time.sleep(velocity)
	print() 
	


