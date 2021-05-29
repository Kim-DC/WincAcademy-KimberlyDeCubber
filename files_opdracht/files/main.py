__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile

def main():
    os.chdir("files")
    clean_cache() 
    
    folder = os.getcwd()
    zip_file = folder + "\data.zip"
    folder_cache = folder + "\cache"
    cache_zip(zip_file, folder_cache)

    list_with_files = cached_files()
    find_password(list_with_files)

def clean_cache():
    folder = os.getcwd()
    folder_cache = folder + "\cache"
    folder_check = os.listdir(folder)
    if 'cache' in folder_check:
        shutil.rmtree(folder_cache) 
    else:
        os.mkdir(folder_cache)

def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)

def cached_files():
    list_files = []
    folder = os.getcwd()
    folder_cache = folder + "\cache"
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_files.append(result)
    return list_files

def find_password(list_files):
    mylines = []
    for zip_file in list_files:
        with open (zip_file, 'rt') as myfile:
            for myline in myfile:
                if 'password' in myline:
                    mylines.append(myline)
                    passphrase = myline.strip(str(['password: '])).rstrip('\n')
                    return(passphrase)

if __name__ == '__main__':
        main()