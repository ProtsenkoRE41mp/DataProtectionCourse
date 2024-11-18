# Запрос параметров у пользователя
operation = input("Введіть '+' для шифрування або '-' для дешифрувания: ").strip()
n = int(input("Введіть значення сзуву (n): "))

rotors = ['BDFHJLCPRTXVZNYEIWGAKMUSQO', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ']
message = input("Введіть данні для обробки (літери A-Z): ").strip().upper()

shift = ord('A')
alphabetLen = len(rotors[0])

if operation == '-':  # Розшифровка
    # Зворотний прохід через ротори
    rotors.reverse()
    for rotor in rotors:
        message = ''.join(chr(ord('A') + rotor.index(symbol)) for symbol in message)

    # Зворотний прохід алфавітного зсуву
    decoded = ''.join(
        chr((ord(symbol) - (n + index) % alphabetLen - ord('A')) % alphabetLen + ord('A'))
        for index, symbol in enumerate(message)
    )
    print("Розшифроване повідомлення:", decoded)

elif operation == '+':  # Шифрування
    # Прямий алфавітний зсув
    encoded = ''.join(
        chr((ord(symbol) + (n + index) % alphabetLen - ord('A')) % alphabetLen + ord('A'))
        for index, symbol in enumerate(message)
    )

    # Прохід через ротори
    for rotor in rotors:
        encoded = ''.join(rotor[ord(symbol) - ord('A')] for symbol in encoded)

    print("Зашифроване повідомлення:", encoded)

else:
    print("Помилка вибору операції. Повторіть спробу.")
