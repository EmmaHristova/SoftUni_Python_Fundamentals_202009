# 09-01. REGEX [Lab]
# 02. Match Phone Number

import re

pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'
string = input()

phone_numbers = re.finditer(pattern, string)
phone_numbers = [phone_number.group() for phone_number in phone_numbers]
print(', '.join(phone_numbers))
