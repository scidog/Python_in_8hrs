#Ex2.4.py
for str in 'Bax has this.':
    print ("Current Character is:", str)
print()
print ("multi-string triple quotes work, but can make for odd results.")
print()
for str2 in '''a b c''':
    print ("Current str2 Character is:", str2)
print()
for str3 in '''multi
                string
                print''':
    print ("Current str3 Character is:", str3)

multistring = '''
                This
                is
                how
                a
                multistring
                prints
                via
                the
                print
                command.'''
print()
print ("multistring prints out like so:")
print(multistring)

