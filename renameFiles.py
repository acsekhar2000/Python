import glob
import os

directory_path = "/home/myubuntu/pyprojects/Data/Securities/"
# Use glob to find all files with a specific extension
file_list = glob.glob(os.path.join(directory_path, "*.csv"))

# Print the list of file names
for file_path in file_list:
    #print(file_path)
    #print(file_path[50:52])
    if file_path[50:52].isnumeric():
        newname=file_path[0:42] + file_path[50:52] + "export.csv"
        print(newname)
        os.rename(file_path, newname)
