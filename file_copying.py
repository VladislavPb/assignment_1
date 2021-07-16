import shutil
import os
import xml.etree.ElementTree as ET

tree = ET.parse(input())
root = tree.getroot()


for i in root:
    #checking if system is using shashes or backslashes as delimiters
    if '/' in i.attrib['source_path']: 
        delimiter = '/'
    elif '\\' in i.attrib['source_path']:
        delimiter = '\\'
    else:
        delimiter = '/'

    initial = i.attrib['source_path'] +  delimiter + i.attrib['file_name']  #name of initial argument of copying command
    final = i.attrib['destination_path']                                    #name of second argument
    
    if os.path.isfile(initial) is False:
        print(f'File {initial} does not exist')

    elif os.path.isdir(final) is False:
        print(f'Directory {final} does not exist')

    else:
        shutil.copy(initial, final)
        print(f'File {initial} has been succesfully copied to {final}')
