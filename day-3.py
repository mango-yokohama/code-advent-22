
import sys
import argparse
from collections import Counter

def process(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	temptotal = 0
	for line in lines:
		line = line.rstrip('\n')

		firsthalf = line[:len(line)//2]
		secondhalf = line[len(line)//2:]

		commonletter =''.join(set(firsthalf).intersection(secondhalf))
		
		if commonletter.isupper() and commonletter != '':
			temptotal += ord(commonletter) - 38
		if commonletter.islower() and commonletter != '':
			temptotal += ord(commonletter) - 96
	print(f'PART 1: Sum of the priority items values are: '+str(temptotal))

	fi.close()

def processtwo(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	items = []
	temptotal = 0
	for subgroup in [lines[n:n+3] for n in range(0, len(lines), 3)]:
		item1 = subgroup[0].rstrip()
		item2 = subgroup[1].rstrip()
		item3 = subgroup[2].rstrip()
		commonletter = ''.join(set(item1).intersection(set(item2).intersection(item3)))
		if commonletter.isupper() and commonletter != '':
			temptotal += ord(commonletter) - 38
		if commonletter.islower() and commonletter != '':
			temptotal += ord(commonletter) - 96
	print(f'PART 2: Sum of the priority items values are: '+str(temptotal))

	fi.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Run as an example client')

	# run command: python3 day-3.py -i day3_data.txt
	parser.add_argument('-i','--input',type=str)
	args = parser.parse_args()
	process(args.input)
	processtwo(args.input)
	print(f'Processing complete.')






