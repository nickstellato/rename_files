#!/usr/bin/env python

import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r'C:\Users\Berendson\Desktop\secret_message')
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Berendson\Desktop\secret_message")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
def main():
    rename_files()

if __name__ == '__main__':

    main()
