#a custom module to be imported

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email))