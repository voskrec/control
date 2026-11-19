text = input("Введите текст (можно несколько предложений): ")

words = text.split()
a= "аеёиоуыэюяaeiouy"

c_g = 0  
c_c = 0 

for i in words:
    # Берем первую букву, делаем маленькой
    first= i[0].lower()
    
    # Если это буква (а не кавычка или другой символ)
    if first.isalpha():
        if first in a:
            c_g += 1
        else:
            c_c += 1

print(f"\n1. Слов с гласной: {c_g}, а с согласной: {c_c}")

#самое частое слово
clean_words = []
for word in words:
    clean_w = ""
    for char in word:
        if char.isalpha():
            clean_w += char.lower()
    if clean_w != "":
        clean_words.append(clean_w)

# Ищем самое частое слово (двойной цикл)
most_common_word = ""
max_count = 0

for i in range(len(clean_words)):
    current_word = clean_words[i]
    current_count = 0
    
    # Считаем, сколько раз текущее слово встречается в списке
    for w in clean_words:
        if w == current_word:
            current_count += 1
            
    if current_count > max_count:
        max_count = current_count
        most_common_word = current_word

print(f"2. Самое частое слово: '{most_common_word}' (встречается {max_count} раз)")

#удаляем повторяющиеся символы
compressed_text = ""
if len(text) > 0:
    compressed_text = text[0] # Первый символ оставляем всегда
    for i in range(1, len(text)):
        # Если текущий символ не равен предыдущему — добавляем его
        if text[i] != text[i-1]:
            compressed_text += text[i]

print(f"3. После сжатия повторов: \"{compressed_text}\"")
#проверяем на анаграмму
second_text = input("\nВведите вторую строку для проверки анаграммы: ")

# Очищаем обе строки от всего, кроме букв (и делаем маленькими)
clean_text1 = ""
for char in text:
    if char.isalpha():
        clean_text1 += char.lower()

clean_text2 = ""
for char in second_text:
    if char.isalpha():
        clean_text2 += char.lower()

# Сортируем буквы (sorted превращает строку в список и сортирует)
sorted_text1 = sorted(clean_text1)
sorted_text2 = sorted(clean_text2)

if sorted_text1 == sorted_text2:
    print("4. Строки являются анаграммами.")
else:
    print("4. Строки НЕ являются анаграммами.")
#извлекаем текст из ковычек
quotes_list = []
inside_quotes = False # Флаг: мы внутри кавычек или нет
current_quote = ""

for char in text:
    # Если встретили открывающую кавычку (обычную или «)
    if (char == '"' or char == '«') and inside_quotes == False:
        inside_quotes = True
        current_quote = "" # Начинаем собирать текст заново
    # Если встретили закрывающую кавычку (обычную или »)
    elif (char == '"' or char == '»') and inside_quotes == True:
        inside_quotes = False
        quotes_list.append(current_quote)
    # Если мы внутри кавычек, добавляем символ к тексту
    elif inside_quotes == True:
        current_quote += char

print(f"5. Текст в кавычках: {quotes_list}")
#ищем быков и коров
print("\n--- 6. Игра 'Быки и коровы' ---")
secret = input("Введите первое слово: ")
guess = input("Введите второе слово: ")

if len(secret) != len(guess):
    print("Ошибка: слова должны быть одинаковой длины!")
else:
    secret = secret.lower()
    guess = guess.lower()
    
    bulls = 0
    cows = 0
    
    # Превращаем строки в списки, чтобы можно было "вычеркивать" буквы
    secret_list = list(secret)
    guess_list = list(guess)
    
    # 1. Ищем БЫКОВ (буква на своем месте)
    for i in range(len(secret_list)):
        if secret_list[i] == guess_list[i]:
            bulls += 1
            # Заменяем найденные буквы на '_', чтобы не считать их снова
            secret_list[i] = '_'
            guess_list[i] = '_'
            
    # 2. Ищем КОРОВ (буква есть, но не на своем месте)
    for i in range(len(guess_list)):
        if guess_list[i] != '_': # Если эта буква не была быком
            if guess_list[i] in secret_list:
                cows += 1
                # Находим индекс этой буквы в секретном слове и зачеркиваем её
                index_in_secret = secret_list.index(guess_list[i])
                secret_list[index_in_secret] = '_'
                
    print(f"Быки={bulls}, Коровы={cows}")