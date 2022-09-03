# from importlib.resources import path
# from itertools import count
# from msilib.schema import Directory
from operator import eq
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import sklearn
# import pathlib
# import PIL
from zipfile import ZipFile
import socket
import os
import random

# Main function
def main():
    unzip()
    equal_dataset()
    split_set()



def unzip():
    #download the datasets <https://www.kaggle.com/datasets/ujjwalchowdhury/yoga-pose-classification>
    if not os.path.exists("YogaPoses"):
        #with ZipFile('C://Users//SBautis2//Downloads//archive.zip', 'r') as zipObj:
        with ZipFile('archive.zip', 'r') as zipObj:
    ### Extract all the contents of zip file in different directory
            zipObj.extractall()
            print('File is unzipped in current directory')
    else:
        print('File is unzipped in current directory')





def equal_dataset():
### Making equal data set 

    blank_list = []
    main_folder = "YogaPoses"
    class_folder = os.listdir(main_folder)
    #print (class_folder)
    
    
    #knowing the least data set
    for i in class_folder:
        folder = "YogaPoses/"+i
        open_folder = os.listdir(folder)
        #print(f"{i} has {len(open_folder)} images")
        blank_list.append(len(open_folder))

    #print (blank_list)

    least_val = min(blank_list)
    #print (f"the least value is {least_val}\n\n")

    #determining
    for i in class_folder:
        folder = "YogaPoses/"+i
        files = os.listdir(folder)
        data = len(files)
        if data > least_val :
            list_data = os.listdir(folder)
            delete_files = random.choices(list_data,k=data-least_val)
            #print  (f"Ther are {data} in {folder}")
            #print (f"{data-least_val} need to delete")
            #print (delete_files)

            for j in delete_files:
                data_set = folder+"/"+j
                os.remove(data_set)
            
            #print("\n\n\n")
            

        else:
            #print (f"The files in {folder} is {data}\n\n\n")
            pass
    
    rename_data(main_folder)
    

    

    





def rename_data(main_folder):
    ####Renaming datas
     
    try:
        #Renaming the photos in their specific classification with count
        #main_folder = "YogaPoses"
        class_file = os.listdir(main_folder)
        #print (class_file)
        for i in class_file:
            #print(i)
            class_folder = "YogaPoses/"+ i
            for counter , filename in enumerate(os.listdir(class_folder)):
                dst = f"{i}_{counter}.jpg"
                src = f"{class_folder}/{filename}"
                dst = f"{class_folder}/{dst}"
                os.rename(src,dst)

    except FileExistsError:
        print("The files are already rename")




def split_set():
    try:
        #Making dataset dir

        #parent_directory = "C:\\Users\\SBautis2\\Downloads\\OJT\\YOGA_POSE CLASSIFIER" # Main Directory
        parent_directory = "C:\\Users\\bauti\\Desktop\\YOGA-POSE CLASSIFIER" # Main Directory
        directory = "Datasets"
        data_folder = os.path.join(parent_directory,directory)
        os.mkdir(data_folder)

        training_folder = "train"
        testing_folder = "test"
        
        #Making train and test folder in dataset dir
        train_folder = os.path.join(directory , training_folder)
        test_folder = os.path.join(directory , testing_folder )
        os.mkdir(train_folder)
        os.mkdir(test_folder)
    except:
        print ("All directory are made")




main()

