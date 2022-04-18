'''
    In this program I'm trying to learn different methods of re module in python.
    I have dummy text stored in sample.txt file and to read that text from file
    I'm using python open() method .
'''
#Opening a file
sapmle_file = open('./sample.txt','r')

#reading a text from file sample_file
sample_text = sapmle_file.read()

#closing a file 
sapmle_file.close()
