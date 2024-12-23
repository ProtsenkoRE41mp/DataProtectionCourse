import string  

# Функція для шифрування та дешифрування тексту за допомогою шифру Цезаря
def caesar_cipher(text, shift):
    result = []  
    for char in text:  
        if char.isalpha():  
            base = ord('a') if char.islower() else ord('A')  
            shifted = (ord(char) - base + shift) % 26  
            result.append(chr(shifted + base))  
        else:
            result.append(char)  
    return ''.join(result)  

def evaluate_english_score(text):
    english_frequencies = {
        'a': 8.08, 'b': 1.67, 'c': 3.18, 'd': 3.99, 'e': 12.56,
        'f': 2.17, 'g': 1.80, 'h': 5.27, 'i': 7.24, 'j': 0.14,
        'k': 0.63, 'l': 4.04, 'm': 2.60, 'n': 7.38, 'o': 7.47,
        'p': 1.91, 'q': 0.09, 'r': 6.42, 's': 6.59, 't': 9.15,
        'u': 2.79, 'v': 1.00, 'w': 1.89, 'x': 0.21, 'y': 1.65, 'z': 0.07
    }
    text = text.lower()  
    total_letters = sum(char.isalpha() for char in text)  
    if total_letters == 0:
        return float('inf')  

    score = 0  # Ініціалізація оцінки
    for char, freq in english_frequencies.items():
        actual_freq = text.count(char) / total_letters * 100  
        score += abs(freq - actual_freq)  
    return score

# Основна функція програми
def main():
    encrypted_text = input("Введіть зашифрований текст: ")  
    best_shift = 0  
    best_score = float('inf')  
    decoded_text = ""  

    for shift in range(26):  
        candidate = caesar_cipher(encrypted_text, shift)  
        score = evaluate_english_score(candidate)  

        if score < best_score:  
            best_score = score  
            best_shift = shift  
            decoded_text = candidate  

    print(f"Кращий результат досягнуто при зсуві {best_shift}: {decoded_text}")


if __name__ == "__main__":
    main()
