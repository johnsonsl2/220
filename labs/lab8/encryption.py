"""
Name: Sara Johnson
lab8.py

Problem:Inputing files and coding out files to demonstrate work for the instructor

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""


def encode(message, key):
    out = ""
    for ch in message:
        pre_ord = (ord(ch))
        final_ord = pre_ord + key
        final_ch = (chr(final_ord))
        out = out + final_ch
    return out
# Add your encryption methods here