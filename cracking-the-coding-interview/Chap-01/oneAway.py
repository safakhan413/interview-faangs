import unittest

def is_one_away(first: str, other: str) -> bool:
    """Given two strings, check if they are one edit away. An edit can be any one of the following.
    1) Inserting a character
    2) Removing a character
    3) Replacing a character"""

    skip_difference = {
        -1: lambda i: (i, i+1),  # Delete # e.g.(1,2)
        1: lambda i: (i+1, i),  # Add e.g. #(2,1)
        0: lambda i: (i+1, i+1),  # Modify e.g.(2,2)
    }
    #skip difference is a dictionay with func lambda stored for each case -1,0,1
    try:
        skip = skip_difference[len(first) - len(other)]
        # print('im skip fucn',skip(1))
    except KeyError:
        return False  # More than 2 letters of difference
                    # got no values from -1,0,1

    for i, (l1, l2) in enumerate(zip(first, other)):

        if l1 != l2:
            i -= 1  # Go back to the previous couple of identical letters
            break

    # At this point, either there was no differences and we exhausted one word
    # and `i` indicates the last common letter or we found a difference and
    # got back to the last common letter. Skip that common letter and handle
    # the difference properly.
    remain_first, remain_other = skip(i + 1)
    return first[remain_first:] == other[remain_other:]

class MyTest(unittest.TestCase):
    def test_is_one_away(self):
        self.assertEqual(is_one_away('pale', 'ale'), True)
        self.assertEqual(is_one_away('pales', 'pale'), True)
        self.assertEqual(is_one_away('pale', 'bale'), True)
        self.assertEqual(is_one_away('pale', 'bake'), False)
        self.assertEqual(is_one_away('ale', 'pale'), True)
        self.assertEqual(is_one_away('aale', 'ale'), True)
        self.assertEqual(is_one_away('aael', 'ale'), False)
        self.assertEqual(is_one_away('motherinlaw', 'womanhitler'), False)
        self.assertEqual(is_one_away('motherinlaw','motherinlow'), True)

if __name__ == '__main__':
    test = MyTest()
    test.test_is_one_away()
