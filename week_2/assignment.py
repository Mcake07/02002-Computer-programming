side_length = 4
surface_area = 6 * side_length ** 2
volume = side_length ** 3

print(side_length)
print(surface_area)
print(volume)


val1 = (2 + 8) * 10
val2 = 2 + 8 * 10
print(val1)
print(val2)

val3 = 100 / 5 / 2
val4 = (100 / 5) / 2
val5 = 100 / (5 / 2)
print(val3)
print(val4)
print(val5)


a = "42"
print(a)
print(type(a))


first_part = "Hello"
second_part = "World"
print(first_part, second_part)


my_var = 42
print(my_var, type(my_var))
my_var = 128
print(my_var, type(my_var))

a = 2
print(a)
a += 100
print(a)
a *= 3
print(a)
a -= 50
print(a)
a **= 2
print(a)
a /= 4
print(a)
a //= 2
print(a)
a %= 10
print(a)


a = "10.0"
b = "5"
result = a + b
print(result, type(result))


first_name = "John"
last_name = "Doe"
age = 29
full_name = first_name + " " + last_name
print(full_name)
sentence = "My name is " + full_name + " and I am " + str(age) + " years old."
print(sentence)

age = 31
print("I am", age, "years old.")

start = "I am " 
middle = "really "
end = "happy to see you!"

message = start + 4 * middle + end
print(message)

a = [42, 51, 3]
print(a)
print(type(a))

a = ["Hello", 49, 3.14159]
print(a)
print(type(a))


a = ["Hello"]
b = ["World!"]
result = a + b
print(result, type(result))


my_list = ["Three", 4, 5.0]
result = my_list * 3
print(result)


a = "Hi there, this is a string!"
b = ["And", "this", "is", "a", "list", "of", "strings"]
print(len(a))
print(len(b))


bool_true = True
bool_false = False
test = "True"
print(bool_true, type(bool_true))
print(bool_false, type(bool_false))
print(test, type(test))


a = 10
b = 2
c = 5
result = a > b
print(result, type(result))

test1 = "test1"
test2 = "test2"
print("test", test1 > test2, test1 < test2)


lie = False
fact = True

exp1 = lie == fact
print(exp1)

exp2 = fact >= lie
print(exp2)

exp3 = fact - fact == lie - lie
print(exp3)


print('Yes' == 'Yes')
print('Yes' == 'yes')
print('Yes' != 'yes')


true_value = 18
guessed_value = 18
number_of_tries = 5
maximal_number_of_tries = 20

win = (number_of_tries <= maximal_number_of_tries) and (true_value == guessed_value)
print(win)


number = 1000
print(number % 100 == 0)


x = 17
y = 4

result_min = min(x, y)
print("When using min we get", result_min)

result_max = max(x, y)
print("When using max we get:", result_max)