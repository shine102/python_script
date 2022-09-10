import os
import sys
import pandas as pd
import json, yaml

def main():
    path = sys.argv[1]
    # check if not exists path
    if not os.path.exists(path):
        print("Path does not exist")
        sys.exit(1)
    # check if not a directory
    if not os.path.isdir(path):
        print("Path is not a directory")
        sys.exit(1)
    # check if directory is empty
    if os.listdir(path) == []:
        print("Directory is empty")
        sys.exit(1)
    # loop all files in directory
    for file in os.listdir(path):
        if file.endswith(".csv"):
            print("converting .csv file")
            df = pd.read_csv(path + "/" + file)
            df.to_json(path + "/" + file[:-4] + ".json", orient="records")
        elif file.endswith(".json"):
            print("converting .json file")
            df = pd.read_json(path + "/" + file)
            df.to_csv(path + "/" + file[:-5] + ".csv", index=False)
        elif file.endswith(".yaml"):
            print("converting .yaml file")
            # to temporary JSON file
            json.dump(yaml.safe_load(open(path + "/" + file)), open("temp.json", "w"))
            # read the JSON file
            json_file = pd.read_json("temp.json")
            # to csv
            json_file.to_csv(path + "/" + file[:-5] + ".csv", index=False)
            os.remove("temp.json")

if __name__ == "__main__":
    main()