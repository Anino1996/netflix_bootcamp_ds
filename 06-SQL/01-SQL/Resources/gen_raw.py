import pandas as pd
import os

files=filter(lambda x: x[-3:] == 'csv' and "checkpoints" not in x, os.listdir())
# files=['departments.csv']
file_prefix="raw"

def main():


	for file_name in files:
		df= pd.read_csv(file_name)
		row_data=str(tuple(tuple(val) for val in df.values))

		with open(f'{file_prefix}_{file_name[:-4]}.txt', 'w') as infile:
			infile.write(row_data)

if __name__=='__main__':
	main()

