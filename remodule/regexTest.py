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
pattern_for_numbers = re.compile(r'[0-9]+')
result = pattern_for_numbers.findall(sample_text)
print(result)

#extracting all the 2 digit numbers from sample_text 
pattern_for_two_digit_numbers = re.compile(r'\b[0-9]{2}\b')
result = pattern_for_two_digit_numbers.findall(sample_text)
print(result)

#extracting text only
patter_textonly = re.compile(r'[^0-9]+')
result = patter_textonly.findall(sample_text)
print(result)

#searching for words wich contains more than 2 vowels 
patter_with_two_vowels = re.compile(r'\w[aeiouAEIOU]{2}\w')
result = patter_with_two_vowels.findall(sample_text)
print(result)

#patter to find all the phone numbers in text 
patter_for_phone_numbers = re.compile(r'\d{3}-\d{4}-\d{4}')
result = patter_for_phone_numbers.finditer(sample_text)
for match in result:
    print(match)

#patter to find all the  Indain phone numbers in text 
patter_for_indian_phone_numbers = re.compile(r'(\+91)?(\d{10})')
result = patter_for_indian_phone_numbers.finditer(sample_text)
for match in result:
    print(match)

#closing a file 
sapmle_file.close()
