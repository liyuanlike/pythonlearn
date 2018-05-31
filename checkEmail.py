import re

def is_valid_email(addr):
    if re.match(r'[0-9a-zA-Z\.]+@[a-zA-Z]+.com', addr):
        return True
    else:
        return False
