import re

text = r"AmardipGhodichor"

# re.search(pattern, string, flags)
# pattern : regular expression
# string : where the pattern shall search
# flags : special meaning
# re.search same syntax:
# only search @ beginning of the string
print(re.match(r"Gh", text))

# .group() to print matched string
print(re.match("Ama",text).group())
# start and end will print indexes
print(re.match("Ama",text).start())
print(re.match("Ama",text).end())

print(re.search("Gh.+", text).group())

## Literal Meaning

print(re.search("A|G", text))

# re findall
print(re.search("abcd", "abcd efgh abcd"))
print(re.findall("abcd", "abcd efgh abcd"))

#character set

# \w: matches alphanumeric numbers [a-zA-z0-9_\]

print(re.search(r"\w\w\w\w", "abcddeddde"))
print(re.search(r"\w\w\w\w", "abc.e"))

# \W is apposite of \w
print(re.search(r"\w\w\w\W", "abc e"))


# Quantifiers
'''
'+' 1 or more
'?' 0 or 1
'*' 0 or more
'{n,m}' n to m repits 
'''

print(re.search(r"\w+", "abcddeddde gyugu"))
print(re.search(r"\w+\W+\w+", "abcddedddegyugu"))
print(re.search(r"\w+\W?\w+", "abcddeddde  gyugu"))


## charcter sets
# '\d' : Matches any digit 0-9
#  \D : opposite

# \s : any whitespace charachter like tabs, space and nect line
# \S

string = "Do you merely want to print the string that way, or do you want that to be the internal representation of the string? \
         If the latter, create it as a raw string by prefixing it with r"

print(re.findall("\S+", string))
print(' '.join(re.findall(r'\S+', string)))

# '.' all except new line

# create ur own char set
# [A-Z] '-' is also special meta chars
# [^A-X] negates text after it but if its outside it means at the start

num = "1808850254"

print(bool(re.match(r'7|8|9',num)))
