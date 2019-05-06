import re


num_data = re.findall("[0-9]","SW214")
print(num_data)

num_str =""

for ns in num_data:
      num_str += ns
print(num_str)


