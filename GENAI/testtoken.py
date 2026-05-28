import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Encode (text -> token IDs)
x = enc.encode("hello world")
print(x)   # [15339, 1917]

# Decode (token IDs -> text)
y = enc.decode(x)
print(y)   # hello world