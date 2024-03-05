"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["ADOBECODEBANC", "ABC"],
            "answer": (9, 13),
        },
        {
            "input": ["ab", "a"],
            "answer": (0, 1),
        },
        {
            "input": ["ab", "A"],
            "answer": (-1, -1),
        },
        {
            "input": ["abcdef", "ace"],
            "answer": (0, 5),
        },
        {
            "input": ["MixEdCaSeScRiNgTrIcKy", "cSeR"],
            "answer": (8, 12),
        },
    ],
    "Extra": [
        {
            "input": ["aa", "a"],
            "answer": (0, 1),
        },
        {
            "input": ["abc", "xyz"],
            "answer": (-1, -1),
        },
        {
            "input": ["a", "a"],
            "answer": (0, 1),
        },
        {
            "input": ["ThisIsAComplexString", "tps"],
            "answer": (5, 16),
        },
        {
            "input": ["racecar", "race"],
            "answer": (0, 4),
        },
        {
            "input": ["xyzyx", "zyx"],
            "answer": (0, 3),
        },
        {
            "input": ["abacdbabc", "abcd"],
            "answer": (1, 5),
        },
        {
            "input": ["aabbcc", "abc"],
            "answer": (1, 5),
        },
        {
            "input": ["aaabbbccc", "abc"],
            "answer": (2, 7),
        },
        {
            "input": ["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"],
            "answer": (0, 26),
        },
        {
            "input": ["abcfdsalghioxdhun", "asdh"],
            "answer": (4, 10),
        },
        {
            "input": ["abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy", "xywvutsrqponmlkjihgfedcba"],
            "answer": (0, 25),
        },
        {
            "input": ["AbCdEfGhIjK", "EgI"],
            "answer": (-1, -1),
        },
        {
            "input": ["lowerUPPER", "ErU"],
            "answer": (4, 9),
        },
    ]
}
