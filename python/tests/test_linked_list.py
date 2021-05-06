import pytest
from linked_list.linked_list import *
from code_challenges.Data_Structures.linked_list.linked_list import *
from code_challenges.Data_Structures.linked_list.linked_list import Linked_list


def test_import():
    assert LinkedList

def test_one(list_test):
    excpected = "{a} -> {b} -> {c} ->  NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    actual = [list_test.includes("h"),list_test.includes("b")]
    excpected = [False, True]
    assert excpected == actual


@pytest.fixture
def list_test():
    linked = Linked_list()
    linked.insert("c")
    linked.insert("b")
    linked.insert("a")
    return linked

