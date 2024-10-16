import re

# Some Wild-Card Character
# ^ Matches the expression to its right, at the start of a string before it experiences a line break
# $ Matches the expression to its left, at the end of a string before it experiences a line break
# . Matches any character except newline
# a Matches exactly one character a
# xy Matches the string xy
# a|b Matches expression a or b. If a is matched first, b is left untried.

# Example:
#   ^X.*:  (Buscar al inicio de cada linea los que empiece con X + varios caracteres hasta llegar a ":")
# Example:
# X-Sieve: CMU Sieve 2.3
# X-DSPAM-Result: Innocent
# X-DSPAM-Confidence: 0.8475
# X-Content-Type-Message-Body: text/plain
# Example:
file = open('stringsPy.txt')
for line in file:
  line = line.rstrip()
  if(re.search('^X.*:', line)):
    print(line) 
print("*******2********")
# The same but not consider whether exists non-whitespace character in-middle
file2 = open('stringsPy.txt')
for line in file2:
  line = line.rstrip()
  if(re.search('^X-\S+:', line)):
    print(line) 
