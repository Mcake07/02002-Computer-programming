def punctuation_check(text):
    punctuation = False
    errors = 0
    punctuators = ',.?!:;'
    for character in text:
        if punctuation and character != ' ':
            errors += 1
            punctuation = False
        punctuation = character in punctuators
    return errors

print(punctuation_check("This is:a text, a text with many,many errors! But,who cares?"))
print(punctuation_check("Here we have no errors.Or do we?!"))
print(punctuation_check("No,I am sure this is error-free!"))
print(punctuation_check("Whataboutonlyasingleword? "))
print(punctuation_check("       almost   empty    ?     "))
print(punctuation_check("3 times.is.not enough"))
print(punctuation_check("!Whou, this is strange!"))
print(punctuation_check("A,B,C,D,E,F,G,H,I"))
print(punctuation_check("Number nine is a good example, almost no problems there-I think."))
print(punctuation_check("But!The last text is bad.Really,really bad.No space at all.Squeezed!"))