# a= 23
# # b=-247


# print(bin(a ))

# print(bin(-a&0xFFFFFFFF))

user_input = "<script>alert('XSS');</script>"
escaped_input = "%s" % user_input
result = "Hello, %s!" % escaped_input

print(escaped_input)
print(result)