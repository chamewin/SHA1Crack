# James Nguyen
# CSC 4980/6980 Blockchains & Applications
# Assignment 2
# February 25, 2019
# This program attempts to brute force SHA1 hashes by hashing each password and comparing it with the hash it is trying
# to crack. This program also has the option to crack salted hashes if the salt is known. To find the salt's string,
# the same process of brute forcing an unsalted hash is used on the salt to find its string. If found, the salt's
# string will be concatenated to the front and the end of each password, hashed, and compared to the hash the program
# is attempting to crack.
#
# Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
# Answer: 'letmein', attempts: 15
#
# Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
# Answer: 'vjhtrhsvdctcegth', attempts: 999967
#
# Leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
# Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
# Answer: 'harib', attempts: 1546153

import hashlib, urllib, time


def brute_hash():
    # Prompts the user for the desired hash to brute force (assuming user is trying to brute force a SHA1 hash)
    hash = raw_input("Enter hash.\n> ")
    # Prompts the user to enter the salt hash if known
    salt = raw_input("Enter salt (If no salt, press enter again.)\n> ")
    # This is an array of passwords obtained by separating a list of passwords using newline as the delimiter
    pw_stream = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-'
                                   'Credentials/10-million-password-list-top-1000000.txt').read()).split()

    # 'count' variable of type Int used to keep track of the number of comparisons the program does
    count = 0
    # 'concat' variable of type String used to store the string form of the salt
    concat = ""
    # This code starts a timer. Its function is to keep track of the time it takes to brute force the hash.
    start = time.time()
    # If there is a salt, brute force the salt and store the string in 'concat' variable
    if salt != "":
        for pw in pw_stream:
            if hashlib.sha1(pw).hexdigest() == salt:
                concat = str(pw)
    # This next section of code will concatenate what's stored in 'concat' variable, the reverse of the salt hash, to
    # the front and the end of each password separately, and check to see if
    for pw in pw_stream:
        if hashlib.sha1(pw+concat).hexdigest() == hash:
            end = time.time()
            print("Password is ", str(pw), "Tries: ", count, "Time: ", str(end-start))
            quit()
        elif hashlib.sha1(pw+concat).hexdigest() != hash:
            count += 1
    for pw in pw_stream:
        if hashlib.sha1(concat+pw).hexdigest() == hash:
            end = time.time()
            print("Password is ", str(pw), "Tries: ", count, "Time: ", str(end-start))
            quit()
        elif hashlib.sha1(pw+concat).hexdigest() != hash:
            count += 1


brute_hash()