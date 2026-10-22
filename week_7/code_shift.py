def code_shift(code, turn):
    code_list = list(code)
    answer = []
    for i in range(len(code)):
        if int(code_list[i]) + (turn % 10) <= 9:
            answer.append(str(int(code_list[i]) + (turn % 10)))
        else:
            answer.append(str((int(code_list[i]) + (turn % 10) - 10)))
    answer = ''.join(answer)
    return answer

tests = []
tests.append(code_shift('2638', 3) == '5961')
tests.append(code_shift('0120', -3) == '7897')
tests.append(code_shift('9165', 1) == '0276')

print("All tests passed:", all(tests))