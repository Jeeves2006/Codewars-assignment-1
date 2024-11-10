# Even or odd
def even_or_odd(number): # defines a function and takes one parameter (number)
    if number % 2 == 0: # divides the number by 2, if it equals 0 it's even
        return "Even"
    else:
        return "Odd"
    
# Coverting an integer to a string
def number_to_string(num):
    str_num = str(num)
    return str_num

#Vowel count
def get_count(string): # function that counts vowels from the sting input
    vowels = "a,e,i,o,u" # defines the vowels
    count = sum(1 for char in string if char in vowels) # for every vowel found in the string it's given a 1, then the (sum) is added up
    return count