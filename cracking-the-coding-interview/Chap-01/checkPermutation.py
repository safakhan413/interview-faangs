#Given two strings, write a method to decide if one is a permutation of the other

def check_s1_s2_permutable(s1, s2):
    return sorted(s1) == sorted(s2)

print(check_s1_s2_permutable('safk', 'kfsaa'))