'''
DO NOT REMOVE THIS COMMENT
STUDENT ID: 46864512
STUDENT NAME: Suresh Ghatani
[]: add an 'x' inside the square brackets to declare that 
you haven't seen any other person's code
and you haven't shared your code with, or shown your code to, anyone
'''
with open('grades_file.csv', 'r') as f:
	records = {}
	lines = f.readlines()[2:] # skip first two lines
	for line in lines:
		tokens = [int(item.strip()) for item in line.strip().split(',')]
		records[tokens[0]] = tokens[1] # add to dictionary
	print(records)