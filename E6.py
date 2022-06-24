s = str(input("Escribir una frase/palabra: "))
s1 = ''

for lee in reversed(s):
    s1 += lee

if s.lower() == s1.lower():
    print("{} is a palindrome".format(s))
else:
    print("{} is not a palindrome".format(s))

print("\n")

# Opcion 2
if s.lower() == s[::-1].lower(): print("{} is a palindrome".format(s))
else: print("{} is not a palindrome".format(s))