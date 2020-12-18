#Implement an algorithm to determine if a string has all unique characters.

def contains_no_duplicates(string):
  letters = {}
  for letter in string:
    print(letter)
    if letter in letters:
      return False
    letters[letter] = True
  print(letters)
  return True

if __name__ == "__main__":
  import sys
  print(contains_no_duplicates('safk'))