import hashlib, urllib, time, sys

def improved_crack():

    p_arr = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read()).split()
    found = False
    if len(sys.argv) == 2:
        dict1 = {}
        for pw in p_arr:
            key = hashlib.sha1(pw).hexdigest()
            dict1[key] = pw
        print("The password is " + dict1[sys.argv[1]])

    if len(sys.argv) == 3:
        dict1 = {}
        for pw in p_arr:
            key = hashlib.sha1(pw).hexdigest()
            dict1[key] = pw
        salt = dict1[sys.argv[2]]

        dict2 = {}
        for pw in p_arr:
            key = hashlib.sha1(salt + pw).hexdigest()
            dict2[key] = pw
        if sys.argv[1] in dict2:
            pwd = dict2[sys.argv[1]]
            print("The password is " + pwd)
            found = True

        if not found:
            dict3 = {}
            for pw in p_arr:
                key = hashlib.sha1(pw + salt).hexdigest()
                dict3[key] = pw
            if sys.argv[1] in dict3:
                print("The password is " + dict3[sys.argv[1]])
                found = True

        if not found:
            print("Password is not in this list. Please try another.")
            quit()


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Please enter a valid number of arguments")
        quit()
    improved_crack()

start = time.time()
main()
print("--- %s seconds ---" %(time.time() - start))