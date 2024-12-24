def XOR(hex1, hex2):
    # XOR двох рядків у шістнадцятковому форматі
    result = []
    for i in range(0, len(hex1), 2):
        b1 = int(hex1[i:i+2], 16)
        b2 = int(hex2[i:i+2], 16)
        result.append(b1 ^ b2)
    return result

def Decode(InputEncoded, Key):
    # Декодуємо повідомлення за допомогою ключа
    decoded = ''
    for i in range(0, len(InputEncoded), 2):
        byte = int(InputEncoded[i:i+2], 16)
        decoded += chr(byte ^ Key[i // 2])
    return decoded

# Вхідні дані
message1 = "72d0954e354045f09461dc4c911d0b58ff8963efb12c34303f"  # M1 xor K1
message2 = "391813c092a2d5ac9acb705dfe41be3df08de67d1145cbcc3f"  # M2 xor K1 xor K2
message3 = "03adeae2c8c2f2336c8a8d312733c2456e76e0b2d9068adc3f"  # M3 xor K2

# Отримуємо K2
K2 = XOR(message1, message2)  # M1 xor M2 xor K2 -> видає K2, якщо M1=M2 частково
print(f"Key K2: {K2}")

# Отримуємо K1
K1 = XOR(message2, message3)  # M2 xor M3 xor K1 -> видає K1, якщо M2=M3 частково
print(f"Key K1: {K1}")

# Декодуємо всі повідомлення
decoded_message1 = Decode(message1, K1)
decoded_message2 = Decode(message2, [k1 ^ k2 for k1, k2 in zip(K1, K2)])  # K1 xor K2
decoded_message3 = Decode(message3, K2)

print(f"Розшифроване повідомлення 1: {decoded_message1}")
print(f"Розшифроване повідомлення 2: {decoded_message2}")
print(f"Розшифроване повідомлення 3: {decoded_message3}")
