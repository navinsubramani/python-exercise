# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib

text = "hello world!hello world!hello world!hello world!"
text_byte = bytes(text, 'utf-8')

compressed_text = zlib.compress(text_byte)
print(compressed_text)

decompressed_text = zlib.decompress(compressed_text)
print(decompressed_text)