import re

s = input()

# print("yes" if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.match(r"([\d])\1\1\1", s.replace("-", "")) else "no")
# if re.match(r"[456]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}", s) and not re.match(r"([\d])\1\1\1", s.replace("-", "")):
#     print("yes")
# else:
#     print("no")




if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
    print("Valid")
else:
    print("Invalid")