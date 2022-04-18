'''
    In this program I'm trying to learn different methods of re module in python.
    I have dummy text stored in sample.txt file and to read that text from file
    I'm using python open() method .
'''
import re
#Opening a file
sapmle_file = open('./sample.txt','r')

#reading a text from file sample_file
sample_text = sapmle_file.read()

#extracting all the numbers from sample_text 
pattern = re.compile(r'[0-9]+')
result = pattern.findall(sample_text)
print(result)

#extracting all the 2 digit numbers from sample_text 
pattern = re.compile(r'\b[0-9]{2}\b')
result = pattern.findall(sample_text)
print(result)

#closing a file 
sapmle_file.close()
