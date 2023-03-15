import re

def replace_chars_and_strip(text):
    # Замінюємо всі символи крім букв та цифр на "-"
    text = re.sub(r"[^\w\d]", "-", text)
    # Видаляємо "-" з кінця до першого символу букви або цифри
    text = re.sub(r"[-]+(?=[\w\d])", "", text)
    return text


# Приклад використання:
text = "*+   aviatro avasddsdf sdf sdf s+df* - / sdf sd/*-+."
new_text = replace_chars_and_strip(text)
print(new_text) # "Hello-world-123"


# text = "*+   aviatro avasddsdf sdf sdf s+df* - / sdf sd/*-+"

# text = clean_string(text)
# print(text)




# def remove_trailing_hyphens(s):
#     # Знаходимо індекс останнього символу букви або цифри
#     last_alpha_or_digit_index = len(s) - 1
#     for i in range(len(s) - 1, -1, -1):
#         if s[i].isalpha() or s[i].isdigit():
#             last_alpha_or_digit_index = i
#             break

#     # Видаляємо "-" з кінця рядка до першого символу букви або цифри
#     s = s[:last_alpha_or_digit_index + 1]
#     while s.endswith("-"):
#         s = s[:-1]

#     return s
