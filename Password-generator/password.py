import random
import string

def passwordGenerate(name, age, length=12):
    
    char = string.ascii_letters + string.digits + string.punctuation
    additional_chars = ''.join(random.choices(name + str(age), k=length-len(name)-len(str(age))))
    password = name + str(age) + additional_chars
    password = ''.join(random.sample(password, len(password))) 
    return password


name = input("Enter your name: ")
age = input("Enter your age: ")


password = passwordGenerate(name, age)
print("YourPassword:", password)
