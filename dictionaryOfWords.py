"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["revert"] = "to go back"
word_definitions["cosset"] = "to treat as a pet"
word_definitions["hero"] = "a person noted for courageous acts or nobility of character"
word_definitions["force majeure"] = "an unexpected and disruptive event that may operate to excuse a party from a contract"
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# print(word_definitions["revert"])
# print(word_definitions["cosset"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
# for (word, definition) in word_definitions.items():
#     print(f'The definition of {word} is {definition}')

for word in word_definitions:
    print(f'The definition of {word} is {word_definitions[word]}')