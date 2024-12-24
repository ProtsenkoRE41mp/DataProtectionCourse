input_binary = "000111111000111000000000000111111000000111000111000111111111111000000111"

def triple_string(char):
    bin_str = format(ord(char), '08b')  
    tripled = ''
    index = 0
    while index < len(bin_str):  
        tripled += bin_str[index] * 3
        index += 1
    return tripled

def encode(string):
    encoded = ''
    index = 0
    while index < len(string):  
        encoded += triple_string(string[index])
        index += 1
    return encoded

def parse_triple_string(bin_string):
    result = ''
    index = 0
    while index < len(bin_string): 
        triplet = bin_string[index:index + 3]
        result += '1' if triplet.count('1') >= 2 else '0'
        index += 3
    return result

def decode(bits):
    recovered_bits = parse_triple_string(bits)
    recovered_text = ''
    byte_start = 0
    while byte_start < len(recovered_bits): 
        byte = recovered_bits[byte_start:byte_start + 8]
        if len(byte) == 8: 
            recovered_text += chr(int(byte, 2))  
        byte_start += 8
    return recovered_text

# Тестові дані
test_str = "hey"
disrupted_data = "010110110000111010000010000111111001000111000111000111111110011000000111"
print(decode(disrupted_data))
