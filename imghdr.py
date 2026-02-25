# Minimal stub for imghdr module (Python 3.13 compatibility)
# python-telegram-bot v13 isko import karta hai, lekin hamain
# sirf error hatana hai, accurate detection abhi zaroori nahi.

def what(file, h=None):
    """
    Fake implementation of imghdr.what()
    Always return None. Library is mostly using it
    to guess image type, but hamare basic bot ke liye
    ye enough hai.
    """
    return None
