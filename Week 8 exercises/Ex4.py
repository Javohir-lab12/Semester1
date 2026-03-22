def decompress_rle(encoded_string):
    result = []
    multiplier = ""
    for i in range(len(encoded_string)):
        c = encoded_string[i]
        if c in "0123456789":
            multiplier = multiplier + c
        else:
            result.append(c*int(multiplier))
            multiplier =""

    return "".join(result)
    
print(decompress_rle("3A2B4C"))
print(decompress_rle("1W4B1W"))
print(decompress_rle("10X1Y"))
print(decompress_rle("1A1B1C1D1E"))
print(decompress_rle("12Z"))