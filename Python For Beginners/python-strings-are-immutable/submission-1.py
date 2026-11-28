def remove_fourth_character(word: str) -> str:
    changed_word1 = word[:3]
    changed_word2 = word[4::]
    new_word = changed_word1 + changed_word2
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
