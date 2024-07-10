import string

import enchant


def bubbleSort(lst):
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] > lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)

        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


english_dict = enchant.Dict("en_US")


def spell_check(words):
    misspelled = []
    for word in words:
        if not english_dict.check(word):
            misspelled.append(word)
    return misspelled


def suggest_corrections(misspelled_words):
    suggestions = {}
    for word in misspelled_words:
        suggestion = english_dict.suggest(word)
        suggestions[word] = suggestion
    return suggestions


str = input("enter paragraph in which you want to implement Sorting Algo: ")
str1 = str.maketrans('', '', string.punctuation)
str_with_punctuation = str.translate(str1)
key = input("Enter keyword to search: ")

lst = str_with_punctuation.split(" ")

merge_sort(lst)
print(lst)

for i in lst:
    if key in lst:
        print("Keyword found")
        break
else:
    print("Keyword not found")

misspelled_words = spell_check(lst)

if misspelled_words:
    suggestions = suggest_corrections(misspelled_words)
    for word, suggestion in suggestions.items():
        print(f"The word '{word}' is misspelled. Suggestions: {', '.join(suggestion)}")
else:
    print("No misspelled words found.")

