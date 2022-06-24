import string, random as rnd

def password_generator(n):
    while True:
        letters = string.ascii_letters
        numbers = string.digits
        if n % 3 != 0:
            m = round(n / 3)
        else:
            m = n / 3
        pw = ''.join(rnd.choice(letters + numbers) for i in range (n))
        pw = ''.join(rnd.sample(pw, n))
        a = [0, 0, 0]
        for let in pw:
            if let in string.ascii_uppercase:
                a[0] += 1
            elif let in string.ascii_lowercase:
                a[1] += 1
            elif let in numbers:
                a[2] += 1
        if a[1] >= a[0] >= 1 and 0 < a[2] <= m:
            break
    return pw


if __name__ == "__main__":
    while True:
        c = True
        try:
            n = int(input("Choose password lenght: "))
        except ValueError:
            print("That is not an int.")
            n = 3
            c = False
        if n >= 3 and c == True:
            break
        elif c == True:
            print("Password must be longer than 2 characters.")
    print(str(password_generator(n)))

