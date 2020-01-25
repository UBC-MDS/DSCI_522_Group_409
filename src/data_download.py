# author: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian 
# date: 2020-01-17

'''This script downloads the data from the input URL. This script takes a filepath
and save the file in the desired folder.

Usage: data_download.py --file_url=<file_url> --file_path=<file_path>

Options:
--file_url=<file_url>  URL that contains the input file
--file_path=<file_path>  Path (excluding filename) to the folder.
'''

import pandas as pd
import numpy as np
from docopt import docopt
import requests, zipfile, io, os
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(file_url, file_path):

    # extract file from the link

    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
    
    r = requests.get(str(file_url))

    #unzip the zip file
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path = file_path)

    #input_file_path = file_path + "/hour.csv"

    #read the data
    

    #rental_input_data_hr = pd.read_csv(input_file_path)

    # split into training and testing

    #X_train, X_test, y_train, y_test = train_test_split(rental_input_data_hr.drop(columns=['cnt']), 
    #                                                rental_input_data_hr[['cnt']], 
    #                                                test_size=0.20, 
    #                                                random_state=100)

    # save the splitted files
    #X_train.to_csv(file_path +  "/train.csv", index=False)
    #X_test.to_csv(file_path +  "/test.csv", index=False)
    #y_train.to_csv(file_path + "/train_target.csv", index=False)
    #y_test.to_csv(file_path  + "/test_target.csv", index=False)

    
def check_file(file_path):
    """
    Writing the text file and print success in the file
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
    
    file1 = open(file_path + "/success.txt","w")#write mode 
    file1.write("Succes Download") 
    file1.close()
    return os.path.isfile(file_path +  "/success.txt")

def test_error(file_path):
    assert check_file(file_path), "Training file is not generated"

test_error(opt["--file_path"])

if __name__ == "__main__":
    main(opt["--file_url"], opt["--file_path"])
