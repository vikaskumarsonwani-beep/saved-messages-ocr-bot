# Minimal stub for pkg_resources (Python 3.12+ + python-telegram-bot v13)
# Library sirf version read karne ke liye use karti hai,
# isliye dummy implementation kaafi hai.

class Distribution:
    def __init__(self, version="0.0.0"):
        self.version = version


def get_distribution(name):
    # Hamesha ek dummy distribution return kar dete hain
    # jiska version 13.15 hai (jo hum requirements me use kar rahe hain)
    return Distribution("13.15")
