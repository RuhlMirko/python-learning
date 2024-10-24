import shutil
""" You can make a zip file with shutil
    the first argument is the name of the file
    the second is the extension of the file (.zip)
    the third is the file folder you want to make a file 
"""
shutil.make_archive("output", "zip", "txt_files")
