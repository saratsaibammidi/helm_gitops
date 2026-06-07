import subprocess
from datetime import datetime

# Print "Hello, World!" to the terminal.
print("Hello, World!")

# Greet the user with their name
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Display the contents of a text file named "exec_stdout.txt"
try:
	with open("exec_stdout.txt", "r") as file:
		print(file.read())
except FileNotFoundError:
	print("File not found")

# Display the current date and time
current_date_time = datetime.now()
print(current_date_time)
