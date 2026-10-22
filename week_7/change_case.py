def change_case(text):
    if '_' in text: case = 'snake'
    else: case = 'camel'
    if case == 'snake':
        result = ''
        next_upper = False
        for symbol in text:
            if symbol == '_':
                next_upper = True
            else:
                if next_upper:
                    symbol = symbol.upper()
                next_upper = False
            result += symbol
        result = result.replace('_','')
        return result
    else: 
        result = ''
        for symbol in text:
            if symbol.isupper():
                symbol = '_' + symbol.lower()
            result += symbol
        return result


tests = []
tests.append(change_case('thisIsIdentifierName') == 'this_is_identifier_name')
tests.append(change_case('this_is_an_identifier_name') == 'thisIsAnIdentifierName')
tests.append(change_case('justChecking') == 'just_checking')
tests.append(change_case('just_checking') == 'justChecking')
tests.append(change_case('one_two_three_words') == 'oneTwoThreeWords')
tests.append(change_case('oneTwoThreeWords') == 'one_two_three_words')
tests.append(change_case('singleword') == 'singleword')
tests.append(change_case('this_is_a_valid_name') == 'thisIsAValidName')
tests.append(change_case('thisIsAlsoValidName') == 'this_is_also_valid_name')
tests.append(change_case('nowWhat') == 'now_what')
tests.append(change_case('we_are_done') == 'weAreDone')

print("All tests passed:", all(tests))