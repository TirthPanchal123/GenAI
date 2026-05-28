str1="      hello world welcome to python programming     "

'''
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.split(","))
print(str1.replace("python","java"))
print(str1.count("o"))
print(str1.find("welcome"))
print(str1.startswith("hello"))
print(str1.endswith("programming"))
print(str1.strip()) # extra white space remove
'''


'''
str2="hello, world! "
print(str2.strip())
'''

'''
str3="python is a great programming language"
print(str3.split(","))
'''

words=["python","is","a","great","programing","language"]
print("".join(words))