import argparse
parser = argparse.ArgumentParser()
parser.add_argument('number', type=int, help="an integer number")
args = parser.parse_args()
result = args.number * 2
print("Result:", result)
