byte_array=[111, 12, 45, 67, 109]




result = ' '.join('{:02x}'.format(x) for x in byte_array)
print(result)