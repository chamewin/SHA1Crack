# James Nguyen
# CSC 4980/6980 Blockchains & Applications
# Assignment 2
# February 25, 2019
#
# Purpose:
# This program attempts to brute force SHA1 hashes by hashing each password and comparing it with the hash passed as
# the 1st argument (sys.argv[1]). This program also has the option to crack salted hashes if the salt is known by first
# finding the plaintext of the salt using a brute force method and concatenating the salt plaintext to each password
# in the password list at the front of the password then at the end.


import hashlib, sys, time, urllib


def brute_hash():

    # Variables

    count = 0  # This variable keeps track of the number of comparisons the program makes before finding the password.

    concat = ""  # This variable stores the plaintext of the salt hash.

    found = False  # This variable is used when checking to see if the password has been found yet.

    # This is an array of passwords obtained by separating a list of passwords using newline as the delimiter.

    pw_stream = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-'
                                   'Credentials/10-million-password-list-top-1000000.txt').read()).split()

    # If there are 2 arguments passed, the hash is not salted and the following code will run. This code will hash each
    # password in the password list and compare the hash with the hash passed as the 1st argument (sys.argv[1]).

    if len(sys.argv) == 2:
        for pw in pw_stream:
            if hashlib.sha1(pw).hexdigest() == sys.argv[1]:
                print("Password is " + str(pw) + ". Tries: " + str(count))
                found = True
            elif hashlib.sha1(pw).hexdigest() != sys.argv[1]:
                count += 1

    # If there are 3 arguments passed, it means the hash is salted and the user provided a salt (in hash form). This
    # code will hash each password in the password list and compare the hash with the salt hash passed as the 2nd
    # argument (sys.argv[2]). If a match is found, store the salt plaintext in concat variable.

    if len(sys.argv) == 3:
        for pw in pw_stream:
            if hashlib.sha1(pw).hexdigest() == sys.argv[2]:
                concat = str(pw)

        # Concatenate the salt plaintext to the end of the passwords. Then, hash the combined plaintext and compare
        # with the hash passed as the 1st argument (sys.argv[1]). If there is a match, print the password and the
        # number of comparisons needed before finding a match.

        for pw in pw_stream:
            if hashlib.sha1(concat + pw).hexdigest() == sys.argv[1]:
                print("Password is " + str(pw) + ". Tries: " + str(count))
                found = True
            elif hashlib.sha1(pw + concat).hexdigest() != sys.argv[1]:
                count += 1

            # If found is still False, then the code concatenates the salt plaintext to the front of the passwords.
            # The code then hashes the combined plaintext and compare with the hash passed as the 1st
            # argument (sys.argv[1]). If there is a match, print the password and the number of comparisons needed
            # before finding a match.

        if not found:
            for pw in pw_stream:
                if hashlib.sha1(pw + concat).hexdigest() == sys.argv[1]:
                    print("Password is " + str(pw) + ". Tries: " + str(count))
                    found = True
                elif hashlib.sha1(pw + concat).hexdigest() != sys.argv[1]:
                    count += 1

    # If found is still False, then the password is likely not in the list used. Terminate the program.

    if not found:
        print("Password is not in this list. Please try another.")
        quit()


def main():

    # This marks the time the program starts

    start = time.time()

    # If there are less than 2 or more than 3 arguments passed, then print error message and terminate program.

    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Please enter a valid number of arguments")
        quit()

    # Calls the user-defined function brute_hash

    brute_hash()

    # Prints the how long the program ran for. Current time - start time.

    print("Program ran for " + str(time.time() - start) + " seconds")


main()