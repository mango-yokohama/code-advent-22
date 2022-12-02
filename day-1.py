import csv
import sys
import argparse

def process(in_file, out_file):
	fi = open(in_file,'r')
	lines = list(fi)
	fo = open(out_file,'w')
	csvwriter = csv.writer(fo,delimiter=',')
	temptotal = 0
	elfcounter = 1
	currentmax = 0
	csvwriter.writerow(['Elf','Total_Cals'])
	for line in lines:
		line = line.rstrip('\n')
		
		if line != '':
		
			if int(line) > 0:
				temptotal += int(line)
		else:
			csvwriter.writerow([elfcounter,temptotal])
			elfcounter += 1
			if temptotal > currentmax:
				thirdmax = secondmax
				secondmax = currentmax
				currentmax = temptotal
			elif temptotal > secondmax:
				thirdmax = secondmax
				secondmax = temptotal
			elif temptotal > thirdmax:
				thirdmax = temptotal
			temptotal = 0
	print(f'Highest individual total was: '+str(currentmax))
	print(f'Sum of the top three was: '+str(currentmax+secondmax+thirdmax))
	fo.close()
	fi.close()




if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Run as an example client')
	parser.add_argument('-i','--input',type=str)
	parser.add_argument('-o','--output',type=str, default='')
	args = parser.parse_args()
	process(args.input, args.output)
	print(f'Processing complete.')






