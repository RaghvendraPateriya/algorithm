# def find_unique_combinations(string):
#     """
#     Finds all unique combinations of characters in a given string.

#     Args:
#         string: The input string.

#     Returns:
#         A list of unique combinations.
#     """

#     unique_chars = set(string)
#     combinations = []

#     def generate_combinations(current_combination, remaining_chars):
#         if not remaining_chars:
#             combinations.append(current_combination)
#             return

#         for i in range(len(remaining_chars)):
#             new_combination = current_combination + remaining_chars[i]
#             new_remaining_chars = remaining_chars[:i] + remaining_chars[i+1:]
#             generate_combinations(new_combination, new_remaining_chars)

#     generate_combinations("", "".join(unique_chars))
#     return combinations

# if __name__ == "__main__":
#     string = input("Enter a string: ")
#     unique_combinations = find_unique_combinations(string)
#     print(unique_combinations)



# ======================================================

# import itertools

# def find_unique_combinations(string):
#     """
#     Finds all unique combinations of characters in a given string.

#     Args:
#         string: The input string.

#     Returns:
#         A list of unique combinations.
#     """

#     unique_chars = set(string)
#     combinations = []

#     for r in range(1, len(unique_chars) + 1):
#         for combination in itertools.combinations(unique_chars, r):
#             combinations.append(''.join(combination))

#     return combinations

# if __name__ == "__main__":
#     string = input("Enter a string: ")
#     unique_combinations = find_unique_combinations(string)
#     print(unique_combinations)

# ======================================================

def get_all_conbinations(s):

    l = set()
    for i in range(len(s)):
        l.add(s[i])
        for j in range(1, len(s)):
            l.add(''.join([s[i], s[j]]))
            l.add(s[i:j])
    print(l)

get_all_conbinations('CCB')            