#filename: wk02b1_argparse.py
import argparse

parser = argparse.ArgumentParser(description='A script with argparse')    #creates the parser object
parser.add_argument('--input', help='An example input argument')
args = parser.parse_args()            #this will prints a message and throws an exception
print(args.input)   
                        