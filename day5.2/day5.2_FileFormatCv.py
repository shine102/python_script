import pandas as pd 
import sys
import json
import yaml
import os
import argparse

# create the parser
parser = argparse.ArgumentParser(description='Convert a CSV file to JSON or YAML and vice versa')
parser.add_argument('-i', '--input', help='Input file', required=True)
parser.add_argument('-o', '--output', help='Output file', required=True)

# parse the arguments
args = parser.parse_args()

# if the input file is a CSV file
if args.input.split('.')[-1] == 'csv':
    input_file = pd.read_csv(args.input)
    # if the output file is a JSON file
    if args.output.split('.')[-1] == 'json':
        input_file.to_json(args.output, orient='records')
    # if the output file is a YAML file
    elif args.output.split('.')[-1] == 'yaml':
        # convert to temporary JSON file
        input_file.to_json('temp.json', orient='records')
        with open('temp.json') as f:
            data = json.load(f) # load the JSON file
        with open(args.output, 'w') as f: 
            yaml.dump(data, f) # dump the YAML file
        os.remove('temp.json') 
    else:
        print("input and output types must be different or must be CSV and JSON or CSV and YAML")
        exit(1)
# if the input file is a JSON file
elif args.input.split('.')[-1] == 'json' and args.output.split('.')[-1] == 'csv':
    # read the JSON file
    input_file = pd.read_json(args.input)
    # to csv
    input_file.to_csv(args.output, index=False)
# if the input file is a YAML file
elif args.input.split('.')[-1] == 'yaml' and args.output.split('.')[-1] == 'csv':
    # to temporary JSON file
    json.dump(yaml.safe_load(open(args.input)), open('temp.json', 'w'))
    input_file = pd.read_json('temp.json')
    # to csv
    input_file.to_csv(args.output, index=False)
    os.remove('temp.json')
else:
    print("input and output types must be different or must be CSV and JSON or CSV and YAML")
    exit(1)

