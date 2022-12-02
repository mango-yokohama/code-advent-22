import csv
import sys
import argparse

def processPartOne(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	temptotal = 0
	for line in lines:
		line = line.rstrip('\n')
		line = line.split(' ')
		if line[0] == 'A' and line[1] == 'X':
			temptotal += 1 + 3
		if line[0] == 'B' and line[1] == 'X':
			temptotal += 1 
		if line[0] == 'C' and line[1] == 'X':
			temptotal += 1 + 6

		if line[0] == 'A' and line[1] == 'Y':
			temptotal += 2 + 6
		if line[0] == 'B' and line[1] == 'Y':
			temptotal += 2 + 3
		if line[0] == 'C' and line[1] == 'Y':
			temptotal += 2

		if line[0] == 'A' and line[1] == 'Z':
			temptotal += 3 
		if line[0] == 'B' and line[1] == 'Z':
			temptotal += 3 + 6
		if line[0] == 'C' and line[1] == 'Z':
			temptotal += 3 + 3

	print('Part One Total was: '+str(temptotal))
	fi.close()


def processPartTwo(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	temptotal = 0
	for line in lines:
		line = line.rstrip('\n')
		line = line.split(' ')
		if line[0] == 'A' and line[1] == 'X':
			temptotal += 3
		if line[0] == 'B' and line[1] == 'X':
			temptotal += 1 
		if line[0] == 'C' and line[1] == 'X':
			temptotal += 2

		if line[0] == 'A' and line[1] == 'Y':
			temptotal += 1 + 3
		if line[0] == 'B' and line[1] == 'Y':
			temptotal += 2 + 3
		if line[0] == 'C' and line[1] == 'Y':
			temptotal += 3 + 3

		if line[0] == 'A' and line[1] == 'Z':
			temptotal += 2 + 6
		if line[0] == 'B' and line[1] == 'Z':
			temptotal += 3 + 6
		if line[0] == 'C' and line[1] == 'Z':
			temptotal += 1 + 6

	print('Part Two Total was: '+str(temptotal))
	fi.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Run as an example client')
	parser.add_argument('-i','--input',type=str)
	args = parser.parse_args()
	processPartOne(args.input)
	processPartTwo(args.input)
	print(f'Processing complete.')






