#def concatenate(strings):
    
    #initialize an empty string 
    #str1 = ""
    #if strings:
          
        #new_string = '"' + str1.join(strings) + '"'
            
    #else:
        #new_string = '""'
    
    #return (new_string)

#print(concatenate(["a", "b", "c"]))


#def all_but_last(seq):
"""
Returns a new list containing all but the last element in the given list.
If the list is empty, returns None.

For example:
- If we call all_but_last([1,2,3,4,5]), we'll get [1,2,3,4] in return
- If we call all_but_last(["a","d",1,3,4,None]), we'll get ["a","d",1,3,4] in return
- If we call all_but_last([]), we'll get None in return
"""

    #if seq:
     #   my_list = seq[:]
      #  return my_list

        
#print(all_but_last([1, 2, 4, 5, 7, 8]))

#def remove_duplicates(lst):
"""
Returns the given list without duplicates.
The order of the returned list doesn't matter.

For example:
- If we call remove_duplicates([1,2,1,3,4]), we'll get [1,2,3,4] in return
- If we call remove_duplicates([]), we'll get [] in return

Hint(s):
- Remember, you can create a set from a string, which will remove the duplicate elements
"""
    #new_list = []
    
    #list_set = set(lst)
    #for elements in list_set:
        #new_list.append(elements)
    #return new_list


#print(remove_duplicates([1,2,1,3,4]))

#def reverse_word(word):
"""
Reverses the order of the characters in the given word.

For example:
- If we call reverse_word("abcde"), we'll get "edcba" in return
- If we call reverse_word("a b c d e"), we'll get "e d c b a" in return
- If we call reverse_word("a  b"), we'll get "b  a" in return
- If we call reverse_word(""), we'll get "" in return

Hint(s):
- You can iterate over a word in reverse and access each character
"""
#return word[::-1]
    
    
#print(reverse_word('Jib'))
#def divisors(n):
"""
Returns a list with all divisors of the given number n.
As a reminder, a divisor is a number that evenly divides another number.
The returned list should include 1 and the given number n itself.
The order of the returned list doesn't matter.

For example:
- If we call divisors(10), we'll get [1,2,5,10] in return
- If we call divisors(1), we'll get [1] in return
"""

'''return a list of factors for the given number'''
    #factors = []
    #iterate over range from 1 to x number itself.
    #for i in range(1, n + 1):
        #check if i divide x evenly
     #   if (n % i == 0):
      #      factors.append(i)
    #return factors
#print(divisors(10))
def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word in the sentence,
    and returns the sentence without *.
    Else, joins all the words in the given sentence, separating them with a comma, and returns the result.

    For example:
    - If we call capitalize_or_join_words("*i love python"), we'll get "I LovE PythoN" in return.
    - If we call capitalize_or_join_words("i love python"), we'll get "i,love,python" in return.
    - If we call capitalize_or_join_words("i love    python  "), we'll get "i,love,python" in return.

    Hint(s):
    - The startswith() function checks whether a string starts with a particualr character
    - The capitalize() function capitalizes the first letter of a string
    - The upper() function converts all lowercase characters in a string to uppercase
    - The join() function creates a single string from a list of multiple strings
    """
    sentence.startswith('*')
    sentence.capitalize()
    return sentence
print(capitalize_or_join_words("*jib"))

