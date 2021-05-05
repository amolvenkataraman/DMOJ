codes = {
    "MG": "midget girls",
    "MB": "midget boys",
    "JG": "junior girls",
    "JB": "junior boys",
    "SG": "senior girls",
    "SB": "senior boys",
}

code = input()
try:
    print(codes[code])
except:
    print("invalid code")