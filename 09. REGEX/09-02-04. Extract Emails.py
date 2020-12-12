# 09-02. REGEX [Exercise]
# 04. Extract Emails

import re

pattern = r'(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@([A-Za-z]+-?[A-Za-z]+)(\.([A-Za-z]+-?[A-Za-z]+))+\b'
string = input()

emails = [email.group() for email in re.finditer(pattern, string)]
print('\n'.join(emails))
