fir_str=input()
sec_str=input()
if fir_str.upper() < sec_str.upper():
    print("-1")
elif sec_str.upper() < fir_str.upper():
    print("1")
else:
    print("0")