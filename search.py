import time, os
exec(open('/Users/devleo/Desktop/project/wordmaster-quizlet-auto/wordlist.py').read())
wordlist = word_dict
print("Search Wordlist")
while 1:
    print(wordlist[input("> ")])
    time.sleep(0.3)
    os.system("clear")