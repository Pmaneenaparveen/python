words = input("Enter a list of words: ").split()
longest = max(words, key=len)
print("Longest word:", longest)
print("Length of the longest word:", len(longest))
