value = input("Enter the value")
print(value)
print(type(value))

# Strings
name = "Saikiran"
# Bunch of char
c = 'C' # <class 'str'>
c1 = "C" # <class 'str'>
c2 = "dasda da das das dsd asd asd asd as dsa das das das d asd" # <class 'str'>
print(c)
print(type(c))
print(type(c1))
print(type(c2))

print(len(name)) #S, a, i, k, i, r, a, n
print(name.upper()) # Saikiran
print(name.lower()) # saikiran

#type casting string to integer
age = "90"
age1 = 90
print(type(age))
print(type(age1))
# str age -> int
age = int(age)
print(type(age))


#concatination
name = "This is a Big line"
print(type(name))
name = name + str(1)  # can only concatenate str (not "int") to str
print(name)

first_name = "Saikiran"
last_name = "Kalluri"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))

#Literals

# decimal system ->  base  -> 10
age = 89

# binary - base system ->  2
binary_number = 0b1010 # -> # 10 decimal system

# Octal  -> base 8
o = 0o130

# Hex  -> base 16
d = 0x12c

pi = 3.14  # float


# String , str
name = "Saikiran"


is_earth_round = True  # bool

# complex
complex_number = 1 + 7j

