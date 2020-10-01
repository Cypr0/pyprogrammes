# Caesar cipher improved
text = input("Enter your message: ")
cipher = ''
n=int(input("Enter your number: "))
assert n>=1 and n<=25
for char in text:
    if not char.isalpha():
        cipher+=char
    else:
        code = ord(char) + n
        if code > ord('Z') and char.isupper():
            code = ord('A')-1+(ord(char)+n-ord('Z'))
        if code > ord('z') and char.islower():
            code=ord('a')-1+(ord(char)+n-ord('z'))
        cipher += chr(code)

print(cipher)
