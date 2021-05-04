from code_challenges.array_binary_search.array_binary_search import binarysearch

def test_binarysearch():
    input = 15
    actual = binarysearch([4,8,15,16,23,42],input)
    expected = 2
    assert actual == expected

def test_binarysearch_two():
    input = 90
    actual = binarysearch([11,22,33,44,55,66,77],input)
    expected = -1
    assert actual == expected
