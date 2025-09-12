'''
CamelCase Method
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:

'hello case'.camelcase  = > HelloCase
'camel case word'.camelcase  = > CamelCaseWord
'''


def camel_case(st):
    a = map(str,st.title().split())
    return (''.join(a))
