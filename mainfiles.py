__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# 1 In main.py, write the following functions:
# clean_cache: takes no arguments and creates an empty
# folder named cache in the current directory.
# If it already exists, it deletes everything in the cache folder.

from glob import glob
import os
import shutil
import zipfile
import pathlib

os.chdir("files")
folder = os.getcwd()
folder_cache = folder + "/cache"
zip_file = folder + "/data.zip"

#1 - Clean Cache
def clean_cache():
    folder_check = os.listdir(folder)
    if 'cache' in folder_check:
        #delete folder
        shutil.rmtree(folder_cache) 
    else:
        #create folder
        os.mkdir(folder_cache)
    return
#clean_cache()
folder_check = os.listdir(folder)
list_files_cache = os.listdir(folder_cache)


#2 - Cache Zip
def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)
    return 
cache_zip(zip_file,folder_cache)

#3 - Returns list of cached files
def cached_files():
    global list_files
    list_files = []
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_files.append(result)
    return list_files

cached_files()

#4 - Finds password in cached files
def find_password(list_files):
    global file_containing_password
    file_containing_password = ""
    mylines = []
    for x in list_files:
        with open(x) as f:
            if 'password' in f.read():
                file_containing_password = x
        with open (x, 'rt') as myfile:
            for myline in myfile:
                if 'password' in myline:
                    mylines.append(myline)
                    passphrase = myline.strip(str(['password: ']))
                    passphrase2 = passphrase.rstrip("\n")
                    print(passphrase2)
                    return(passphrase2)

find_password(list_files)