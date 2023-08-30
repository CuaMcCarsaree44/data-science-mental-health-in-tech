import pandas as pd

dataset = pd.read_csv('data/survey.csv');

# Get to know the data
def print_dataset_variances(): 
    data = ""
    print("Generating MD table for you")
    for e in dataset.columns:
        set_e_type = dataset[e].dtypes
        print("Feature ", e , " have this datatype: ", set_e_type)
        print("Variance data of ", e, " is: ")
        print(dataset[e].unique())

        data = data + ("| `" + str(e) + "` | " 
                 + " |" 
                 + " `" + str(set_e_type) + "` | " 
                 + str(dataset[e].unique()) + " |\n")
        print("")
    
    file = open("data/md-support.txt", "x")
    file.write(data)
    file.close()
    print ("MD Generation done")

