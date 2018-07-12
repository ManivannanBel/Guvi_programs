alp = raw_input()
vowels = ['a','e','i','o','u']
if len(alp)>1 or not alp.isalnum():
    print ('invalid')
else:
    alp.lower()
    if alp in vowels:
        print ('Vowel')
    else:
        print ('Consonant')




