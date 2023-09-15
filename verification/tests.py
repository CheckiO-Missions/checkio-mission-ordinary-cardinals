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
            "input": [[99, 123456789, 10**10]],
            "answer": [10000000000, 123456789, 99],
        },
        {
            "input": [[9876, 19, 4321, 99, 73, 241, 111111, 563, 33]],
            "answer": [111111, 33, 241, 4321, 563, 73, 19, 9876, 99],
        },
        {
            "input": [[111, 19, 919, 1199, 911, 999]],
            "answer": [111, 19, 911, 919, 1199, 999],
        },
        {
            "input": [[1234, 4321, 3214, 2413]],
            "answer": [1234, 2413, 3214, 4321],
        },
    ],
    "Extra": [
        {
            "input": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
            "answer": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        },
        {
            "input": [[125, 789, 4502, 17, 8936, 621, 98, 3567, 42, 7219]],
            "answer": [42, 125, 4502, 621, 17, 3567, 7219, 98, 8936, 789],
        },
        {
            "input": [[245, 879, 63, 5121, 78, 932, 756, 42, 9034, 654]],
            "answer": [42, 5121, 245, 63, 654, 756, 78, 932, 9034, 879]
        },
        {
            "input": [[158, 27, 6034, 9, 472, 835, 7261, 54, 3189, 682]],
            "answer": [54, 6034, 27, 472, 7261, 158, 835, 682, 9, 3189]
        },
    ]
}
