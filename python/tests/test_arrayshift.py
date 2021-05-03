from code_challenges.array_shift.array_shift import shiftarray

def test_shiftarray():
    input = 5
    actual = shiftarray([2,4,6,8],input)
    expected = [2,4,5,6,8]
    assert actual == expected
