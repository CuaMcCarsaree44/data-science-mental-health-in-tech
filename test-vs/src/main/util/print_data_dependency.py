import pandas as pd

dataset = pd.read_csv('data/survey.csv');

# print_dataset_variances
# This function used to help me on generating data variances within every features.
# There are 2 main steps within this function:
# 1. Loop every column within dataset, and then process it into MD table
# 2. Write the MD script to the txt file
#
# @params (string) file_md_output
#   This parameter act as the output file of the MD.
#
# Notes: MD means Markdown
def print_dataset_variances(file_md_output = "data/md-support.txt"): 
    data = ""
    
    print("Generating MD table for you")
    
    # Callback step number-1
    # For every column within dataset, do:
    # 1. Set the datatype of the column as `set_e_type`
    # 2. Generate the MD script for the feature name, datatype, and every unique value within dataset
    for e in dataset.columns:
        # Callback step number-1
        set_e_type = dataset[e].dtypes
        print("Processing ", e)

        data = data + ("| `" + str(e) + "` | "  # Callback step number-2a (feature name)
                 + " |" 
                 + " `" + str(set_e_type) + "` | " # Callback step number-2b (datatype)
                 + str(dataset[e].unique()) + " |\n") # Callback step number-2c (unique value)
   
    # Callback step number-2
    try:
        file = open(file_md_output, "x")
    except:
        # In case the file is already exist, do read instead.
        file = open(file_md_output, "r")
    file.write(data)
    file.close()
    
    print ("MD Generation done")