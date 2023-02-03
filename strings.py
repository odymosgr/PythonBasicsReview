# Strings: ordered, immutable

my_string = "Hello World"
print(my_string[0])

l_str = """this is multiline
that's how to keep writing on multiple lines \
but escape the new line character in the string"""
print(l_str)

newstr = 'how are you doing?'
print('_'.join(newstr.split(' ')))

var = 3.1415
my_string = "the variable is %.2f" % var
my_string = f"the variable is {var:.2f}"
print(my_string)