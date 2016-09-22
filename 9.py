'''
##1.Write a program that reads words.txt and prints only the words with more than 20 characters
#(not counting whitespace).
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
    if len(word)>20:
        print (word)


##2.Write a function called has_no_e that returns True if the given word
#doesn’t have the letter “e” in it.

fin = open('words.txt','r')
i = 0
crt = 0
for line in fin:
    word = line.strip()
#    print(word)
    i+=1
    if not ('e' in word or 'E' in word):
        crt+=1
print (crt, i)
print "There is %d words that do not contain in the letter 'e' or 'E' out of %d words"%(crt,i)
print"That is %.2f%%"%(100.0*(float(crt)/float(i)))

fin.close()
'''
##3.Write a function named avoids that takes a word and a string of forbidden letters, and that
#returns True if the word doesn’t use any of the forbidden letters
Test=False
def avoids (word, strings):
    for c in strings:
        if  c in word:
            return False
        return True     
if Test:
    def test_avoids(word, strings, expected):
        r=avoids(word, strings)
        if r==expected:
            print("word %s with forbidden set %s works"%(word, strings))
        else:
            print('word %s with forbidden set %s FAILS returned %s expected %s' %(word, strings, str(r),str(expected)))
    test_avoids ( "apple", "wksvQ", True )
    test_avoids ( "apple", "wksva", False )
    test_avoids ( "apple", "eksvQ", False )
else:                 
    strings=raw_input('what words you want to be forbidden')
    i = 0
    crt = 0
    fin = open('words.txt','r')
    for line in fin:
        word = line.strip()
        i+=1
        if avoids (word, strings):
            crt+=1
    print (i, crt, word, strings)
    print ('Out of %d words, %d did not contain any forbidden characters %s' % ( i, crt, strings ))

