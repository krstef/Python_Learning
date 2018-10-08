import glob2

filenames = glob2.glob("*.txt")
# open mergeText file where the program will merge all txt files
with open("mergeText.txt", "w") as mergeFile:
# read each file from txtFiles
	for filename in filenames: 
		with open(filename, "r") as f:
			mergeFile.write(f.read() + "\n")
'''
after f.read() the file will be closed - because of with
for printing values you shoud write another with :) 
			print(f.read())
'''
