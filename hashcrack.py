import hashlib,urllib, time

def bruteHash():
    hash = raw_input("Enter hash. \n>")
    pw_stream = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read()).split()
    count = 0
    start = time.time()
    for pw in pw_stream:
        if (hashlib.sha1(pw).hexdigest() == hash):
            end = time.time()
            print("Password is ", str(pw), "Tries: ", count, "Time: ", str(end-start))
            quit()
        elif (hashlib.sha1(pw).hexdigest() != hash):
            count += 1

def saltHash():
    hash = raw_input("Enter hash.\n> ")
    salt = raw_input("Enter salt.\n> ")
    pw_stream = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read()).split()
    count = 0
    concat = ""
    start = time.time()
    for pw in pw_stream:
        if (hashlib.sha1(pw).hexdigest() == salt):
            concat = str(pw)
    for pw in pw_stream:
        if (hashlib.sha1(pw+concat).hexdigest() == hash):
            end = time.time()
            print("Password is ", str(pw), "Tries: ", count, "Time: ", str(end-start))
            quit()
        elif (hashlib.sha1(pw+concat).hexdigest() != hash):
            count += 1
    for pw in pw_stream:
        if (hashlib.sha1(concat+pw).hexdigest() == hash):
            end = time.time()
            print("Password is ", str(pw), "Tries: ", count, "Time: ", str(end-start))
            quit()
        elif (hashlib.sha1(pw+concat).hexdigest() != hash):
            count += 1

def main():
    checkHash = raw_input("Options\n-------------------\n(1) Hash w/o salt\n(2) Hash w/ salt\n> ")
    if checkHash == '1':
        bruteHash()
    elif checkHash == '2':
        saltHash()
    else:
        print("Enter a valid choice.")
        main()

main()