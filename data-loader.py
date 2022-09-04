#from traceback import print_list
import numpy as np
#import pandas as pd
from zipfile import ZipFile
import socket
import os
import random
import shutil
import math
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
# Main function

def main():
    unzip()
    equal_dataset()
    make_dir()
    split_files() 

#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#Unziping files

def unzip():
    #download the datasets <https://www.kaggle.com/datasets/ujjwalchowdhury/yoga-pose-classification>
    if not os.path.exists("YogaPoses"):
        #with ZipFile('C://Users//SBautis2//Downloads//archive.zip', 'r') as zipObj:
        with ZipFile('archive.zip', 'r') as zipObj:
    ### Extract all the contents of zip file in different directory
            zipObj.extractall()
            print('File is unzipped in current directory\n\n')
    else:
        print('File is unzipped in current directory\n\n')

#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#Making the data set equal

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
            print (f"The files in {folder} is {data}\n\n")
            pass
    
    rename_data(main_folder)
    



#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#Renaming the data set in their persfective class
def rename_data(main_folder):
    
     
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
        print("The files are already rename\n\n")

#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#Making directory for train and test
def make_dir():
    try:
        #Making dataset dir

        #parent_directory = "C:\\Users\\SBautis2\\Downloads\\OJT\\YOGA_POSE CLASSIFIER" # Main Directory
        parent_directory = "C:\\Users\\bauti\\Desktop\\YOGA-POSE CLASSIFIER" # Main Directory
        directory = "Datasets"
        data_folder = os.path.join(parent_directory,directory)
        os.mkdir(data_folder)

        training_folder = "train_files"
        testing_folder = "test_files"
            
        #Making train and test folder in dataset dir

        train_folder = os.path.join(directory , training_folder)
        test_folder = os.path.join(directory , testing_folder )
        os.mkdir(train_folder)
        os.mkdir(test_folder)

        #Making Classification folders in train and test dir

        train_dir =(f"{directory}\{training_folder}")
        test_dir = (f"{directory}\{testing_folder}")


        main_folder = "YogaPoses"
        class_list = os.listdir(main_folder)
        for i in class_list:
            os.makedirs(os.path.join(train_dir,i))
            os.makedirs(os.path.join(test_dir,i))





    except:
        print ("All directory are made")


#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#spliting data set train and test
def split_files():
    
    
    #dst dir
    training_folder = "Datasets//train_files"
    testing_folder = "Datasets//test_files"

    train_values = math.floor((len(os.listdir("YogaPoses//Downdog"))*len(os.listdir("YogaPoses"))*0.8)/5)
    
                

    def split_data (train_values,training_folder,testing_folder):

        main_folder = "YogaPoses"
 
        for i in os.listdir(main_folder):
            copy_dir = f"{main_folder}//{i}"
            list_data = os.listdir(copy_dir)
            dest_dir = f"{training_folder}//{i}//{i}"
            dest_dir_test = f"{testing_folder}//{i}//{i}"
            np.random.shuffle(list_data)
            #print (list_data)
            #print (copy_dir)
            #print (f"{copy_dir},,,,,,{dest_dir}")
        
            
            for k in range (train_values):
                copy_img = list_data.pop(0)
                #print (f"{copy_dir}//{copy_img},,,,,,{dest_dir}.jpg")
                src = f"{copy_dir}//{copy_img}"
                #print (src)
                dst = f"{dest_dir}_{k}.jpg"
                #print (dst)
                shutil.copyfile(src , dst)
                
                
            for j in range (len(list_data)):
                copy_img = list_data.pop(0)
                #print (copy_img)
                src = f"{copy_dir}//{copy_img}" 
                #print (src)
                dst = f"{dest_dir_test}_{j}.jpg"
                #print (dst)
                shutil.copyfile(src , dst)
            
           



                

    check_dir_train = os.listdir(training_folder)
    for i in check_dir_train:
        ins_file_dir = f"{training_folder}//{i}"
        #print(len(os.listdir(ins_file_dir)))
        if (len(os.listdir(ins_file_dir))) < train_values :
            split_data(train_values,training_folder,testing_folder)
            print ("it run the function")
        else :
            print (f"{ins_file_dir} has {(len(os.listdir(ins_file_dir)))}/{train_values} files")
    
    one_folder = "YogaPoses//Downdog"
    #print (len(os.listdir(one_folder)))
    
    check_dir_test = os.listdir(testing_folder)
    for j in check_dir_test:
        ins_file_dir = f"{testing_folder}//{j}"
        #print(len(os.listdir(ins_file_dir)))
        if (len(os.listdir(ins_file_dir))) < len(os.listdir(one_folder)) - train_values :
            split_data(train_values,training_folder,testing_folder)
            print ("it run the function")
        else :
            print (f"{ins_file_dir} has {(len(os.listdir(ins_file_dir)))}/{len(os.listdir(one_folder)) - train_values} files")


#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------
    

 



    






main()

