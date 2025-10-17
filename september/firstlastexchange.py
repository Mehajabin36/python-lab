print("first and last characters exchanged")
s = input("Enter the string: ")

if len(s) < 2:
    print(s)
else:
    s = s[-1] + s[1:-1] + s[0]
    print("First and last characters exchanged:", s)
