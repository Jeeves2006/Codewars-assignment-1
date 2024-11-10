# Even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Coverting an integer to a string
def number_to_string(num):
    str_num = str(num)
    return str_num

#Vowel count
def get_count(string):
    vowels = "a,e,i,o,u"
    count = sum(1 for char in string if char in vowels)
    return count