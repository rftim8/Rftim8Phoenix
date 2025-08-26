# region Imports
import os
from typing import List
import unittest
import sys

cwd = os.getcwd()
sys.path.append(cwd)
import rft_stl

# endregion


# region Data Gethering
input = (
    open(f"{cwd}/Data/CP/LeetCode/IO/_01408_StringMatchingInAnArray_Input.txt")
    .read()
    .strip()
    .splitlines()
)
output = open(
    f"{cwd}/Data/CP/LeetCode/IO/_01408_StringMatchingInAnArray_Output.txt", "w"
)


ngridparams = 2
ncases = int(input[0])
nparams = int(input[1])
v = []
v0 = []


def data_collector():
    for i in range(ngridparams, ncases * nparams + ngridparams, nparams):
        v.append(rft_stl.string_to_1D_list_of_string(input[i]))
        v0.append(rft_stl.string_to_1D_list_of_string(input[i + 1]))


# endregion


# region Solutions
"""
Brute Force
"""


def _01408_StringMatchingInAnArray_0(words: List[str]) -> List[int]:
    n = len(words)

    r = set()
    for i in range(n):
        for j in range(n):
            if i != j:
                if words[j] in words[i]:
                    r.add(words[j])

    return list(r)


"""
KMP Algorithm
"""


def _compute_lps_array(sub: str) -> List[int]:
    lps = [0] * len(sub)
    current_index = 1
    length = 0

    while current_index < len(sub):
        if sub[current_index] == sub[length]:
            length += 1
            lps[current_index] = length
            current_index += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                current_index += 1
    return lps


def _is_substring_of(sub: str, main: str, lps) -> bool:
    main_index = 0
    sub_index = 0

    while main_index < len(main):
        if main[main_index] == sub[sub_index]:
            main_index += 1
            sub_index += 1
            if sub_index == len(sub):
                return True
        else:
            if sub_index > 0:
                sub_index = lps[sub_index - 1]
            else:
                main_index += 1
    return False


def _01408_StringMatchingInAnArray_1(words: List[str]) -> List[int]:
    matching_words = []

    for current_word_index in range(len(words)):
        lps = _compute_lps_array(words[current_word_index])

        for other_word_index in range(len(words)):
            if current_word_index == other_word_index:
                continue

            if _is_substring_of(
                words[current_word_index], words[other_word_index], lps
            ):
                matching_words.append(words[current_word_index])
                break

    return matching_words


"""
Suffix Trie
"""


class TrieNode:
    def __init__(self):
        self.frequency = 0
        self.child_nodes = {}


def _insert_word(root: "TrieNode", word: str) -> None:
    current_node = root
    for char in word:
        if char not in current_node.child_nodes:
            current_node.child_nodes[char] = TrieNode()
        current_node = current_node.child_nodes[char]
        current_node.frequency += 1


def _is_substring(root: "TrieNode", word: str) -> bool:
    current_node = root
    for char in word:
        current_node = current_node.child_nodes[char]
    return current_node.frequency > 1


def _01408_StringMatchingInAnArray_2(words: List[str]) -> List[int]:
    matching_words = []
    root = TrieNode()

    for word in words:
        for start_index in range(len(word)):
            _insert_word(root, word[start_index:])

    for word in words:
        if _is_substring(root, word):
            matching_words.append(word)

    return matching_words


def solve():
    for i in range(ncases):
        res0 = _01408_StringMatchingInAnArray_0(v[i])
        output.writelines(str(res0) + "\n")

        res1 = _01408_StringMatchingInAnArray_1(v[i])
        output.writelines(str(res1) + "\n")

        res2 = _01408_StringMatchingInAnArray_2(v[i])
        output.writelines(str(res2) + "\n")


# endregion


# region Problem Description
"""
Given an array of string words, return all strings in words that is a substring of another word. 
You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
"""


def _01408_StringMatchingInAnArray():
    os.system("cls")
    data_collector()
    solve()


_01408_StringMatchingInAnArray()
# endregion


# region Unit Testing
class _01408_StringMatchingInAnArray_Test(unittest.TestCase):
    def test_01408_StringMatchingInAnArray_0(self):
        for i in range(ncases):
            actual = sorted(_01408_StringMatchingInAnArray_0(v[i]))
            expected = sorted(v0[i])
            self.assertEqual(
                actual,
                expected,
            )

    def test_01408_StringMatchingInAnArray_1(self):
        for i in range(ncases):
            actual = sorted(_01408_StringMatchingInAnArray_1(v[i]))
            expected = sorted(v0[i])
            self.assertEqual(
                actual,
                expected,
            )

    def test_01408_StringMatchingInAnArray_2(self):
        for i in range(ncases):
            actual = sorted(_01408_StringMatchingInAnArray_2(v[i]))
            expected = sorted(v0[i])
            self.assertEqual(
                actual,
                expected,
            )


unittest.main(argv=[""], verbosity=1, exit=False)
# endregion
