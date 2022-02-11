"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring,
    "pwke" is a subsequence and not a substring.
"""


def longest_non_repeat_str(string):
    if string is None:
        return 0

    occur = {}
    start, max_len = 0, 0
    result_str = ""
    for i, c in enumerate(string):
        occur_pos = occur.get(c, None)
        if occur_pos is not None and occur_pos >= start:
            start = occur_pos + 1
        else:
            if i - start + 1 > max_len:
                max_len = max(max_len, i - start + 1)
                result_str = string[start:i+1]
        occur[c] = i

    return max_len, result_str
