# sum_of_evens 
def sum_of_evens(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

# count_vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# count_words
def count_words(text):
    words_dict = {}
    for word in text:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict

# print_triangle
def print_triangle(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("*", end = "")
        print()

assert sum_of_evens([2, 3, 4, 6]) == 12
assert sum_of_evens([]) == 0
assert count_vowels("HELLO World") == 3
assert count_words(["a", "b", "a"]) == {"a": 2, "b": 1}