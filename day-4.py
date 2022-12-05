
import sys
import argparse
from collections import Counter

def process(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	temptotal = 0
	for line in lines:
		line = line.rstrip('\n')
		line = line.split(',')

		firsthalf = line[0].split('-')
		secondhalf = line[1].split('-')

		firsthalflower = int(firsthalf[0])
		firsthalfupper = int(firsthalf[1])

		secondhalflower = int(secondhalf[0])
		secondhalfupper = int(secondhalf[1])

		if firsthalflower <= secondhalflower and firsthalfupper >= secondhalfupper:
			temptotal += 1
		elif firsthalflower >= secondhalflower and firsthalfupper <= secondhalfupper:
			temptotal += 1
	print(f'PART 1: Sum of the priority items values are: '+str(temptotal))


	fi.close()

def processtwo(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	temptotal = 0
	for line in lines:
		line = line.rstrip('\n')
		line = line.split(',')

		firsthalf = line[0].split('-')
		secondhalf = line[1].split('-')

		firsthalflower = int(firsthalf[0])
		firsthalfupper = int(firsthalf[1])

		secondhalflower = int(secondhalf[0])
		secondhalfupper = int(secondhalf[1])

		if (firsthalfupper >= secondhalflower) and (secondhalfupper >= firsthalflower):
			temptotal += 1
	print(f'PART 2: Sum of the priority items values are: '+str(temptotal))

	fi.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Run as an example client')

	# run command: python3 day-4.py -i day4_data.txt
	parser.add_argument('-i','--input',type=str)
	args = parser.parse_args()
	process(args.input)
	processtwo(args.input)
	print(f'Processing complete.')






