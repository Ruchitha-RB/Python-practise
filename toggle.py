a = 'hello'
tog_case = a.upper()
lower_case = a.lower()
print(tog_case)
print(lower_case)


'''c = 'ruchitha'
to_case = chr(ord(c) - 32)
print(to_case)'''


d = 'rUCHiThA123' #mixed case string
swap = d.swapcase() #Built-in for toggle
print(swap)


e = 'rUChitha123'
result = ''
for ch in e:
  if ch.isupper():
     result += ch.lower()
  elif ch.islower():
     result += ch.upper()
  else:
     result += ch
print(result)


