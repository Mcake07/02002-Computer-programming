def is_palindrome(text):
    text = text.replace(',','')
    text = text.replace('.','')
    text = text.replace('?','')
    text = text.replace(':','')
    text = text.replace(';','')
    text = text.replace('!','')
    text = text.replace(' ','')
    text = text.lower()
    reversed = list(text)[::-1]
    reversed = ''.join(reversed)
    return reversed == text


tests = []
tests.append(is_palindrome('racecar'))
tests.append(is_palindrome('A man, a plan, a canal: Panama!'))
tests.append(is_palindrome('Was it a car or a cat I saw?'))
tests.append(is_palindrome('Damejer nis berg greb sin rejemad.'))
tests.append(is_palindrome('A Santa at NASA.'))
tests.append(not is_palindrome('Morten'))
tests.append(not is_palindrome('Not a palindrome'))
tests.append(is_palindrome('Madam'))
tests.append(not is_palindrome('Palindromes are cool'))
tests.append(not is_palindrome('Level and level'))
tests.append(not is_palindrome('Sequence of letters.'))

print("All tests passed:", all(tests))