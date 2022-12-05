
import sys
import argparse


stack1 = 'MFCWTDLB'
stack2 = 'LBN'
stack3 = 'VLTHCJ'
stack4 = 'WJPS'
stack5 = 'RLTFCSZ'
stack6 = 'ZNHBGDW'
stack7 = 'NCGVPSMF' 
stack8 = 'ZCVFJRQW'
stack9 = 'HLMPR'
stacks = [stack1,stack2,stack3, stack4, stack5, stack6, stack7, stack8,stack9]
def process(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	counter = 0
	print(stacks)
	for line in lines:
		line = line.rstrip('\n')
		line = line.split(' ')
		
		amount = int(line[1])
		source = int(line[3])-1
		dest = int(line[5])-1

		sourcestack = stacks[source]
		tempremoved = sourcestack[:amount]
		tempremaining = sourcestack[amount:]
		stacks[source] = tempremaining

		deststack = stacks[dest]
		deststack = tempremoved[::-1]+deststack
		stacks[dest] = deststack
	print(f'Answer for part 1: ')
	result = ''
	for stack in stacks:
		result += stack[0]
	print(result)


	fi.close()

def processtwo(in_file):
	fi = open(in_file,'r')
	lines = list(fi)
	stacks = [stack1,stack2,stack3, stack4, stack5, stack6, stack7, stack8,stack9]
	for line in lines:
		line = line.rstrip('\n')
		line = line.split(' ')
		
		amount = int(line[1])
		source = int(line[3])-1
		dest = int(line[5])-1

		sourcestack = stacks[source]
		tempremoved = sourcestack[:amount]
		tempremaining = sourcestack[amount:]
		stacks[source] = tempremaining

		deststack = stacks[dest]
		deststack = tempremoved+deststack
		stacks[dest] = deststack
	print(f'Answer for part 2: ')
	result = ''
	for stack in stacks:
		result += stack[0]
	print(result)




	fi.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Run as an example client')

	# run command: python3 day-5.py -i day5_data.txt
	parser.add_argument('-i','--input',type=str)
	args = parser.parse_args()
	process(args.input)
	processtwo(args.input)
	print(f'Processing complete.')
