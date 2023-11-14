import random
import string
length=int(input("Enter the length of password:"))
capital_letter=string.ascii_uppercase
small_letter=string.ascii_lowercase
digit=string.digits
symbols=string.punctuation
combine=capital_letter+small_letter+digit+symbols
x=random.sample(combine,length) 
password="".join(x)
print(password)
