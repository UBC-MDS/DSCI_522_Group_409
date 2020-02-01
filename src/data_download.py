# author: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian 
# date: 2020-01-17

'''This script downloads the data from the input URL. This script takes a filepath
and save the file in the desired folder.

Usage: src/data_download.py --file_url=<file_url> --file_path=<file_path>

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
    """
    Download and unzip the data files from the input link
        
    Parameters:
    ------
    file_url: string
        link of the data source 
    
    file_path: string
        path where the data will be stored
    
    Returns:
    -------
        all the data files from the link
    """

    # extract file from the link

    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
    
    r = requests.get(str(file_url))

    #unzip the zip file
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path = file_path)
    
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
    """
    tests whether the files have been downloaded successfully
        
    Parameters:
    ------
    file_path: string
        path where the data will be stored
    
    Returns:
    -------
        a success.txt will be generated if the files are downloaded successfully
    """
    assert check_file(file_path), "Training file is not generated"

if __name__ == "__main__":
    main(opt["--file_url"], opt["--file_path"])

test_error(opt["--file_path"])
    
